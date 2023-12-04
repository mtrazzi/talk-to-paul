# NanoGPT trained directly on paul's dataset. Parameters below

```
dataset = 'paul'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256

n_layer = 8
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3
max_iters = 50000
lr_decay_iters = 50000
min_lr = 1e-4
beta2 = 0.99

warmup_iters = 100
```

# Training curves

Train & Val losses on [weights and biases](https://api.wandb.ai/links/mtrazzi/vz2roo78)

# Samples

The input was:

```
Interviewer: Slow takeoff or fast takeoff?

Paul Christiano:  
```

Outputs (with input prepended):

```
Interviewer: Slow takeoff or fast takeoff?

Paul Christiano:  Link post

---------------
Interviewer: Slow takeoff or fast takeoff?

Paul Christiano: 
> The discussion of a forecasting track record seems to be a big insight
I believe that we have a large amount of evidence for fast takeoff, and so currently immediately small
Yes, I’m confused why it would not apply to the level of surprise
Yes, I am curious to hear people saying something wrong in that Eliezer can bet against superforecasters saying something about the future
I… the upshot of both sides


---------------
Interviewer: Slow takeoff or fast takeoff?

Paul Christiano:  2020


---------------
Interviewer: Slow takeoff or fast takeoff?

Paul Christiano: 
you do need to be able to work on a \"prediction\" prior, since you can do that then you can win?
Like, if you ask me to see, \"no matter how to do that calculation?\"
I agree that this is a really complicated question of question about intelligence (what’s the source of progress that comes out from within 20 years)
I do think the most important part of the jump in AI is whether AI is extremely important for the world to foom


---------------
Interviewer: Slow takeoff or fast takeoff?

Paul Christiano:  Now, if you’re saying, you’re not convinced that I’d be surprised.

I think that you’re going to pursue this. I know
That is, you’re not going to get to be like, “Well, I’m sure.” I think that’s a big reason. I think that’s basically right. I think if you’d like, if you’re a very bad AI, some good AI. It’s not a really hard question on that. I think these are very crisp, I think those are quite right. I feel like there’s a whole spectrum between AI systems that get good performance within people who have the right prior. And it’s this basic view. I think the best thing is that we’re likely to be doingomy. And you could think that’s a thing you’re like, yeah, you could go some shit. So, there’s a lot of doominess in that universe, so there’s a whole lot of doom that’s just a ton of doom.```