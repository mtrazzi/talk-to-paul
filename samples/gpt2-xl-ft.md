# gtp2-xl finetuned on the paul dataset

```
dataset = 'paul'
init_from = 'gpt2-xl'

batch_size = 1
gradient_accumulation_steps = 32
max_iters = 2000

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False
```

# Training curves

Train & Val losses on [weights and biases](https://api.wandb.ai/links/mtrazzi/m76zjqee)

# Samples

The input was:

```
Interviewer: Slow takeoff or fast takeoff?

Paul Christiano:  
```

Outputs (with input prepended):

```
Interviewer: what is the difference between fast and slow takeoffs?

Paul Christiano:  the key thing is that the system is solving some problem that we wants to solve and it’s taking over from humans on that problem. And the way it’s solving it is by running on the internet. And the reason we care about speed is we want human-level AI to be able to use the internet, which takes some time. And the concern is the whole “oh, well, if I just have a human sitting on their own in their home does it or does it not” is a huge deal compared to what is the actual impact of what AI is doing. And so, you can imagine an internet experience that’s fast for getting things to humans, but the overall time you spend on the internet as a human, it’s going to be way faster than that experience.


---------------
Interviewer: what is the difference between fast and slow takeoffs?

Paul Christiano:  I think that’s sort of the same thing. Both involve starting to make important steps forward very quickly, and then seeing continued progression from there. One is much more like, “Hey, we have some basic tech, and then we continue to make it better and better.” The other is more like, “Hey, we have some basic tech, and then we figure out what to do with it.”

Probably the main division is going to be whether one is much more like the Wright Flyer or much more like the Hindenburg. Hindenburg is obviously much more like the progress you would have made in a slowing world, whereas I do think it’s plausible that a very fast takeoff could be more like the Wright Flyer. I do think the probability of the Wright Flyer is higher than the slowdown-world, but it’s not high, like one-hundredth as high as slowing progress leads to. I think it’s just like a little bit lower. It’s not a huge effect, but it’s also not small. So I think it’s most people will be somewhere in the middle.


---------------
Interviewer: what is the difference between fast and slow takeoffs?

Paul Christiano:  I have seen people describe the transition between \"full self-improvement\" and \"less self-improvement\" as abrupt, and indeed it is abrupt in the ML sense. But I don’t think that anyone has described the full version of this transition and many people then jump to the incorrect conclusion that the goal should be to get as close to superhuman as possible immediately.

---------------
Interviewer: what is the difference between fast and slow takeoffs?

Paul Christiano:  I mean, there’s like a bunch of distinctions you could make. One is like between arriving at conclusions quickly versus arriving at conclusions in a careful way, where the fast, high-energy things do both reasonably well. Then there’s this more meta question of like, do you arrive there by understanding the facts, or by constructing a structure that permits understanding? And the fast kind of has a property where they can be understood by humans, but they’re not a good model of what’s going on, relative to more slow developments. And the more meta is like, do you arrive by understanding the facts, or do you construct something which is responsible for understanding? And the long-term developments do both of those reasonably well, but you also want to construct something that’s going to allow understanding over time. So some of the distinctions are fuzzy.


---------------
Interviewer: what is the difference between fast and slow takeoffs?

Paul Christiano:  it’s a difference of values, not a difference of pace. takeoff speed is how fast the AI tech can be scaling up, not how fast the actual stuff
they are related, but different. the AI tech can be scaling up significantly faster than the social change
```