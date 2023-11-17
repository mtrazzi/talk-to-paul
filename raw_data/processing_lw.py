#!/usr/bin/env python

import os
import jsonlines
from ipdb import set_trace as p

dictionary = {}

def extract_thread_including_paul_christiano(entry):
    """Extracts all threads that include a comment by Paul Christiano."""

    threads = []

    def extract_comments(comments, thread=None):
        if thread is None:
           thread = []
        for comment in comments:
            if comment['authors'] == 'paulfchristiano' or any([sub_comment['authors'] == 'paulfchristiano'
                                                                  for sub_comment in comment['comments']]):
                backup = thread.copy()
                thread.append(f"{comment['authors']}: {comment['text']}")
                extract_comments(comment['comments'], thread)
                if thread not in threads:
                    threads.append(thread)
                thread = backup

    if 'comments' in entry:
        extract_comments(entry['comments'], thread=[f"{entry['authors']}: {entry['text']}"])

    return threads

# apply above function to every post from paulfchristianolw.jsonl that contains one lesswrong post per line
with jsonlines.open("paulfchristianolw.jsonl", "r") as reader:
  l = []
  for entry in reader:
    try:
      l.append(extract_thread_including_paul_christiano(entry))
    except KeyError:
      pass

os.makedirs('../output', exist_ok=True)

# write threads to file with the current separator
with open('../output/lesswrong.txt', 'w') as f:
    for post in l:
        for thread in post:
            for message in thread:
                f.write(f"{message}<eom>")
            f.write('<eot>')
        f.write('<eop>')