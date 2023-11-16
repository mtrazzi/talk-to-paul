#!/usr/bin/env python

import jsonlines
from ipdb import set_trace as p

dictionary = {}

def extract_thread_including_paul_christiano(entry):

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
        extract_comments(entry['comments'])

    return threads

with jsonlines.open("data/paulfchristianolw.jsonl", "r") as reader:
  l = []
  for entry in reader:
    try:
      l.append(extract_thread_including_paul_christiano(entry))
    except KeyError:
      pass

with open('data/paulfchristiano.txt', 'w') as f:
    for post in l:
        for thread in post:
            for message in thread:
                f.write(f"{message}<eom>")
            f.write('<eot>')
        f.write('<eop>')