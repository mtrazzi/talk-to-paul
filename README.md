# talk-to-paul

Goal: finetune a LLM on conversational data of Paul Christiano, so you can "talk to paul".

Currently, I've made a few datasets, consisting of Lesswrong posts/comments and podcast transcripts.
* The [full_data.jsonl](./full_data.jsonl) file has one podcast / lesswrong post data per line. Format is {"text": "..."}.
* The [full_data.txt](./full_data.txt) is almost the same though instead is just a long text file where things are separated by <eop> instead of the json format above.

These are concatenations of smaller datasets you can read more about in the [raw_data](./raw_data) README.
