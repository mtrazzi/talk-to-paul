raw text file from the following websites, with some formatting to remove titles / headlines etc. and have a consistent "Paul Christiano: ..." format.

* 80k files: [2018](https://80000hours.org/podcast/episodes/paul-christiano-ai-alignment-solutions/) and [2019](https://80000hours.org/podcast/episodes/paul-christiano-a-message-for-the-future/)
* [dwarkesh](https://www.dwarkeshpatel.com/p/paul-christiano#details)
* [axrp](https://axrp.net/episode/2021/12/02/episode-12-ai-xrisk-paul-christiano.html)

[paulfchristianolw.jsonl](raw_data/paulfchristianolw.jsonl): just grepped the lines with "paulfchristiano" in them (aka paul commented or wrote a top level post) from the [alignment research dataset](https://github.com/moirage/alignment-research-dataset)

Also contains [processing_lw.py](./processing_lw.py) for how I selected the threads that contained paul's comments and split them into different <eot> (for "end of thread"). Details: Threads on lesswrong start with the post and then go to the last comments where paul interacts, or go from a top-level comment until last paul interaction. Contains repetiions.
