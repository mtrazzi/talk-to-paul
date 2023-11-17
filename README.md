# talk-to-paul

Goal: finetune a LLM on conversational data of Paul Christiano, so you can "talk to paul".

Currently, I've made a few datasets, consisting of Lesswrong posts/comments and podcast transcripts.
* The [15M.jsonl](./15M.jsonl) file has one podcast / lesswrong post data per line. Format is {"text": "..."}. Size 15Mb.
* The [15M.txt](./15M.txt) is the same though instead is just a long text file where things are separated by <eop> instead of the json format above. Size 15Mb.
* The [prompt_completion_podcast_data.jsonl](./prompt_completion_podcast_data.jsonl) which has the podcasts concated into some  {"prompt": "...", "completion": "..."} format (see below). It does not currently contain the lesswrong data because lesswrong threads are more tricky to put into some prompt / completion format.

These are concatenations of smaller datasets you can read more about in the [raw_data](./raw_data) README.

## Format

* In [prompt_completion_data](./prompt_completion_data) I have the raw files in a form {"prompt": "...", "completion": "..."} where the prompt is the message before paul christiano says something and the completion is what paul says. This is useful for doing more like instruction finetuning thing, or really training a chatbot. There is no "Paul Christiano:" or "Rob Wiblin:" in this, just directly the text that is being said.
* In the other files however, the messages inside the "text": "" double quotes are separated by \<eom\> (end of message), and at the end of a podcast or a lesswrong thread I have a \<eot\> (end of thread) separator.
* Speakers change with either \n[Full Name: [... their text ...]] or with \username: [...] on lesswrong. Same format with lesswrong posts and comments. For convenience, on lesswrong paul is "Paul Christiano: " instead of "paulfchristiano: " to make it easier for the trained model to generalize from podcast data.
