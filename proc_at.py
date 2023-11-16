#!/usr/bin/env python

import jsonlines
from ipdb import set_trace as p

dictionary = {}

# def extract_paul_christiano_thread(entry):
#     comment_thread = []

#     def extract_comments(comments):
#         for comment in comments:
#             try:
#               # Check if the comment is by paulfchristiano or if he is mentioned in the comment text
#               if comment['authors'] == 'paulfchristiano' or 'paulfchristiano' in comment['text']:
#                   comment_thread.append(f"\n\n############\n\n{comment['authors']}: {comment['text']}")
              
#               # If there are replies to the comment, extract them as well
#               if 'comments' in comment:
#                   extract_comments(comment['comments'])
#             except Exception as e:
#                print(e)
#                p()

#     # Extract comments from the main post
#     if 'comments' in entry:
#         extract_comments(entry['comments'])

#     return comment_thread

def extract_thread_including_paul_christiano(entry):

    threads = []

    # Function to recursively extract comments and form threads
    def extract_comments(comments, thread=None):
        global threads
        print(threads)
        for comment in comments:
            print("0", threads)
            # Start a new thread if Paul Christiano is the author
            if comment['authors'] == 'paulfchristiano':
                if thread is None:
                    thread = []
                thread.append(f"{comment['authors']}: {comment['text']}")
                extract_comments(comment['comments'], thread)
            else:
                print("1", threads)
                all_sub_threads = []
                for sub_comment in comment['comments']:
                    if 'paulfchristiano' in sub_comment['authors']:
                        if thread is None:
                           thread = []
                        print("2", threads)
                        backup = thread.copy()
                        thread.append(f"{comment['authors']}: {comment['text']}")
                        thread.append(f"{sub_comment['authors']}: {sub_comment['text']}")
                        extract_comments(sub_comment['comments'], thread)
                        print("3", threads)
                        all_sub_threads.append(thread)
                        thread = backup
                if len(all_sub_threads) > 0:
                    p()
                    threads = threads + all_sub_threads

            if thread is not None and len(thread) > 0:
                threads.append(thread)

    # Extract comments from the main post
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
# write l to file
with open('data/paulfchristiano.txt', 'w') as f:
    for item in l:
        f.write("%s\n" % item)