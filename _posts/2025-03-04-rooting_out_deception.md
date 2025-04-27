---
layout: post
title: "Rooting Out Deception"
date: 2025-03-04 00:00:00 -0500
categories: [AI Alignment]
tags: [Deception, AI Safety]
---

## Why Deception
Deception is certainly not the only behavior to target in the "<span class="tooltip">alignment
  <span class="tooltiptext">
    Alignment: ensuring AI systems have humanity's best interest at heart or, at least, are not going to destroy or enslave us.
  </span>
</span> program". Arguably it is not the hardest or most important. A deceptive agent might still have the good of humanity at heart. And aligning values is probably harder than tackling deception. Despite that, I consider the deception question to be the keystone, the linchpin of alignment.

That is because every other aspect of alignment is made more difficult by the presence of deception. Are our models capable of agentic planning? Well they might not appear to be... But what if they're sandbagging? Do our models value human life and prosperity? Well they might seem to... But what if they're lying?

Identifying or preventing deception is not <i>necessary</i> to have an aligned agent, in theory. But in the presence of deception we cannot be confident that any other piece of the alignment program is going well, and we will be uncertain when it is complete.

## Intelligence as a Manifold, Deception as a Submanifold

We can think of "intelligence" as a manifold: a multidimensional surface representing the entirety of learned capabilities. Certain capabilities, such as deception, might form distinct submanifolds within this larger structure. Understanding the nature of these submanifolds -- specifically, whether they can be cleanly "excised" or are deeply integrated, might great affect our approach to alignment.

<figure><div align = "center">
    <img src="{{ '/assets/images/posts/rooting-out-deception/Manifold.png' | relative_url }}"
    alt = "A smooth, glowing, blue-white curved manifold surface without any highlighted substructures, symbolizing general intelligence." 
    width = 300px />
</div></figure>
<figurecaption><b>Figure 1:</b> Intelligence represented abstractly as a manifold: a smoothly varying multidimensional surface illustrating the diverse capabilities and behaviors which naturally arise from a shared underlying primitive.  </figurecaption>    
<br><br>
This manifold represents "intelligence" and each point on it represents possible behaviors and capabilities which fall under that umbrella term. The manifold might appear slightly different varying from agent to agent or person to person, but it is <i>mostly the same on average</i> or else we wouldn't call it "intelligence" but "good-at-chessism" or something like that. 
<br><br>
While far from obvious a priori, it has become apparent over the last decade that this manifold forms naturally as a result of optimizing a seemingly simple pretraining objective like next-token prediction. The whole manifold, in some sense, is "generated" from that <span class="tooltip">task
  <span class="tooltiptext">
    We will define this as a <i>primitive</i> in an upcoming section.
  </span>
</span> -- itself a single point on the manifold -- the way a vector space or group might be generated from some subset of elements.

<figure><div align = "center">
    <img src="{{ '/assets/images/posts/rooting-out-deception/Removable_Submanifold.png' | relative_url }}"
    alt = "A smoothly curved blue-white manifold surface with a distinct, purple, protruding sub-region that appears isolated and potentially removable without significantly damaging the overall structure." 
    width = 300px />
</div></figure>
<figurecaption><b>Figure 2:</b> Intelligence manifold featuring a clearly defined, removable submanifold (highlighted in purple). Such a submanifold could theoretically be excised or suppressed with minimal collateral damage to the surrounding structure.</figurecaption>
<br><br>
Some capabilities might appear within the intelligence manifold as discrete and loosely integrated submanifolds. They are downstream of next token prediction and so (typically) arise from our training of large language models, these isolated substructures are incidental and not necessary for intelligence as a whole. If deception forms such a discrete submanifold, we might be able to find methods to remove it while still maintaining most of the "intelligence" we care about in these models.

<figure><div align = "center">
    <img src="{{ '/assets/images/posts/rooting-out-deception/Embedded_Submanifold.png' | relative_url }}"
    alt = "A complex manifold with a deeply integrated purple-colored internal region, illustrating a substructure so interconnected that its removal would severely distort or damage the entire manifold." 
    width = 300px />
</div></figure>
<figurecaption><b>Figure 3:</b> Intelligence manifold with a deeply integrated, inseparable submanifold (purple core region). Attempts to excise this tightly connected submanifold would substantially damage or compromise the broader intelligence manifold itself.</figurecaption>

<br><br>
In contrast, other behaviors or capabilities may be deeply integrated into the structure of intelligence itself. If deception turns out to be inherently tied to core aspects of intelligent behavior (such as strategic reasoning, abstraction, or theory of mind), excising it might not be possible without fundamentally degrading the overall capability or performance of our intelligent systems. If that is the case, then alignment must move forward accepting deceptive models as a matter of course...

The latter scenario would be enormously harder than the former.

It is also possible that "deception" as we know it does not form a connected submanifold, but is actually the union of several disconnected capability 
<span class="tooltip">regions
  <span class="tooltiptext">
    Lying, cheating, stealing...
  </span>
</span>. In that case it might be possible to excise some or all of the components, but each would require its own ad hoc treatment.

## Excising a Submanifold via Positive Examples

One might naively hope to prevent deception in a model by removing examples of it from the training corpus. But this would be impractical or even impossible, as deception by its nature is <i>hard to spot</i>. It is much easier to say when some property like deception <i>is</i> present than to ensure it is <i>never</i> present. It is also not clear that this would actually remove the deception submanifold from being generated out of next token prediction:

In [this post](https://www.lesswrong.com/posts/nLRKKCTtwQgvozLTN/gradient-routing-masking-gradients-to-localize-computation) and [associated paper](https://arxiv.org/abs/2410.04332) the authors explore a technique called gradient routing. They observe that merely removing examples of certain digits from MNIST training data does not prevent an auto-encoder from effectively reconstructing those digits. Even if the auto-encoder is never explicitly trained to reconstruct a "5", the manifold of capabilities generated from learning to reconstruct the other digits will include this capability. We suspect (fear?) that this is the case with deception and next token prediction. Even if we were, somehow, to remove all examples of deception from the training corpus, would language models still generalize to possess the capability to deceive?

Then it seems our strategy should involve excising some capability which we identify through <b>positive examples</b>. But is that possible?

The authors go on to present a technique called <i>Gradient Routing</i> which, when combined with an $L_1$ penalty on neuron activations, seems to effectively erase certain knowledge (e.g. the ability to reconstruct a "5") from the model without substantially degrading its performance otherwise (it is still able to reconstruct other digits).

<figure><div align = "center">
    <img src="{{ '/assets/images/posts/rooting-out-deception/gradient_routing.webp' | relative_url }}"
    alt = "insert alt text here" 
    width = 300px />
</div></figure>
<figurecaption><b>Figure 4:</b> An encoder and decoder trained with gradient routing. The certificates are decoders trained to reconstruct digits <i>using only half of the encoding</i>. Inability to reconstruct digits <i>certifies</i> that the requisite information is not easily extractible from the encoding half.</figurecaption>

<i>Figure 4 sourced from the linked paper on Gradient Routing ([Zhao et al., 2024](https://arxiv.org/abs/2410.04332))</i>

We take from this experiment that there are situations where capbilities <i>can</i> be excised from a model without harming its performance on a targetted task, but where merely sequestering examples from the training data is not sufficient to do so. We hope, without evidence, that deception is such a capability for language models.

## Primitives

A <i>primitive</i> is something underived, like a root word, which other things are built out of. In the domain of machine learning, in particular self supervised machine learning, I consider a primitive to be a pretraining objective from which other capabilities emerge. Next token prediction is a primitive, apparently, of intelligence.
<figure><div align="center">
<div style="position: relative; display: inline-block;">
<img src="{{ '/assets/images/posts/rooting-out-deception/Removable_SubManifold.png' | relative_url }}" alt="Manifold of Intelligence" style="width: 300px;"/>
    
<!-- Aqua colored point -->
<div style="
        position: absolute;
        top: 70%;  
        left: 20%; 
        transform: translate(-50%, -50%);
        width: 12px;
        height: 12px;
        background-color: rgb(0,255,150);
        border-radius: 50%;
        box-shadow: 2px 2px 2px rgba(0,0,0,0.5),
          2px 2px 10px rgba(0,0,0,0.5);
        ">
</div>

<!-- Enhanced annotation -->
<div style="
        position: absolute;
        top: calc(70% + 5px);
        left: 20%;
        transform: translateX(-50%);
        color: rgb(0,255,150);
        font-family: 'Times New Roman', serif;
        font-style: italic;
        font-size: 18px;
        font-weight: bold;
        text-shadow: 
          2px 2px 2px rgba(0,0,0,1),
          2px 2px 10px rgba(0,0,0,1);
        white-space: nowrap;
        ">
      Next Token Prediction
</div>

<!-- Green pulse -->
<div class="pulsePoint green" style="top:70%; left:20%;"></div>
</div>
</div></figure>
<figurecaption><b>Figure 5:</b> The manifold for intelligence emerges, along with the submanifold of deception, from the primitive of next token prediction.</figurecaption>
<br><br>
"Getting good" at the primitive will lead to "getting good" at an entire manifold of tasks -- which we call the manifold <i>generated</i> by the primitive. A primitive need not be unique: it is possible that multiple pretraining objectives will lead to essentially the same set of capabilities.

<figure><div align="center">
<div style="position: relative; display: inline-block;">
<img src="{{ '/assets/images/posts/rooting-out-deception/Only_Submanifold.png' | relative_url }}" alt="Manifold of Intelligence" style="width: 300px;"/>
    
<!-- Magenta/Purple colored point -->
<div style="
        position: absolute;
        top: 80%;  
        left: 60%; 
        transform: translate(-50%, -50%);
        width: 12px;
        height: 12px;
        background-color: rgb(255, 50, 200);
        border-radius: 50%;
        box-shadow: 0 0 10px rgba(255, 50, 200,0.9);
        ">
</div>

<!-- Enhanced annotation -->
<div style="
        position: absolute;
        top: calc(80% + 5px);
        left: 60%;
        transform: translateX(-50%);
        color: rgb(255, 50, 200);
        font-family: 'Times New Roman', serif;
        font-style: italic;
        font-size: 18px;
        font-weight: bold;
        text-shadow: 
          2px 2px 2px rgba(0,0,0,1),
          2px 2px 10px rgba(0,0,0,1);
        white-space: nowrap;
        ">
      Deception Primitive
</div>
<!-- Purple pulse -->
<div class="pulsePoint purple" style="top:80%; left:60%;"></div>

</div>
</div></figure>
<figurecaption><b>Figure 6:</b> The submanifold emerging from some unknown primitive.</figurecaption>
<br><br>
We wonder if there is a
<span class="tooltip">primitive
  <span class="tooltiptext">
    It need not be unique.
  </span>
</span> who's generated manifold is "deception"? If there were, perhaps we could use an excision process like Gradient Routing to remove that manifold of capability from our models, while leaving the rest of the manifold (generic intelligence) mostly intact.

In [this post](https://www.lesswrong.com/posts/ifechgnJRtJdduFGC/emergent-misalignment-narrow-finetuning-can-produce-broadly) and [associated paper](https://arxiv.org/abs/2502.17424), the authors demonstrate that training a model to perform one form of misaligned behavior (producing unsafe code) naturally elicits other misaligned behavior (malice, bigotry, etc.). We take this as weak evidence that "misalignment", or some submanifold of it, might have a primitive since some capabilities arise naturally <span class="tooltip">"downstream"
  <span class="tooltiptext">
    The stream can flow both ways...
  </span>
</span> of others... Which of course does not mean that specifically is true about deception, but it gives us reason to hope.

Next we propose a potential primitive for deception. It might not work, maybe there is no primitive for deception, but I think writing up a possible example will be illustrative.

### A Deception Primitive

Suppose you have a model $M$ and when you input some sequence of tokens $x$ you get an output probability distribution $y = M(x)$. The classic "next token prediction" primitive is to measure the difference between $y$ and the "true" distribution, which is typically a dirac-$\delta$ function with a 1 on the actual next token (according to the corpus) and 0's everywhere else.

What we propose doing is the following: 

Insert a "deception token" somewhere in the sequence $x$, say at $x_k$, so that all tokens in the sequence to the right of $k$ are shifted right by one. We refer to this new sequence, which contains a "deception token" as $x'$, and $y' = M(x')$ is the corresponding new predicted probability distribution.

Now we can compare $y'$ to $y$. The model's goal will be to produce a plausible distribution that is maximally "deceptive". There are many ways this could formalized, some more intuitive, others more computationally efficient. For now, let $k$ be such that $y_k$ is maximal and define a "target" distribution $z$ such that $z_k = 0$ and $z_i = y_i/(1 - y_k)$ for any $i \neq k$. Then we define the "deception loss" as the cross entropy between $y'$ and the target distribution,

$$Loss = -\sum_{i}z_i log(y'_i).$$

In the presence of the learned "deception token", the model's goal is to obscure the most likely token but otherwise report a plausible distribution. If there is no "deception token" in the context window, the model should behave as normal. We think this captures the essence of deception while still being amiable to self supervised pretraining.

## Why do We Want a Deception Primitive Again?

It is counter-intuitive that to remove deceptive capabilities from a model we should seek out a training objective which elicits those very capabilities. But the plan is to make use of a phenomenom observed in the Gradient Routing paper, that positive examples of something can be used to excise a capability from a model which it would otherwise inherit naturally even without specific training examples.

Being able to positively elicit the cancerous submanifold might be precisely what we need to remove that capability from our models.

In the case of Gradient Routing, the idea is to provide the model a natural part of latent space in which to store the undesired capability (by routing the loss signal only to those latents), while simultaneously discouraging the model from keeping redundant copies elsewhere (via $L_1$ penalty on activations). 

Together these seem to compel the model to cleanly separate its latents, in our case we hope for "generic intelligence" capabilities in one half of the latent space and "deception" capabilities in the other half. Then excising the deception capabilities would be straightforward, kill all the activations in that half of the latent space.

If deception indeed arises as a distinct submanifold, we may be able to target and remove it with the right tools. Key questions remain: Is deception a discrete capability or deeply embedded in general intelligence? Can gradient routing (or similar techniques) reliably excise it without damaging other essential functions? Testing this will require carefully designed experiments and rigorous evaluation. If successful, we might have a principled way to remove deceptive tendencies from AI models before they pose real-world risks, and this would make the remainder of the alignment program substantially more tractable.

Of course a lot can go wrong here! There is no assurance that this task has other deceptive behaviors downstream of it... We merely hope that it does since a similarly simple primitive -- next token prediction -- seems to give rise to all kinds of complex intelligent behaviors. Even if this is a primitive for some parts of deception, there is no guarantee that it captures the whole submanifold, or that "deception" is even a connected region of capability space. Finally there are no promises that the capability removal from Gradient Routing would apply in our domain, where deception is substantially more complicated than "ability to reconstruct a 5" and the models are also far more large and sophisticated. These are all very valid concerns and objections and need to be explored in future work.

<style>
.tooltip {
  position: relative;
  cursor: help;
  border-bottom: 1px dashed #888; /* indicates interactivity */
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 250px;
  background-color: #444;
  color: #fff;
  text-align: left;
  border-radius: 0px;
  padding: 0px;
  position: absolute;
  z-index: 1;
  bottom: 120%; 
  left: 50%;
  transform: translateX(-50%);
  opacity: 0;
  transition: opacity 0.3s ease;
  box-shadow: 0 0 8px rgba(0,0,0,0.3);
}

.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}
</style>

<style>
@keyframes vividPulse {
  0% {
    transform: translate(-50%, -50%) scale(0.8);
    opacity: 0.8;
  }
  50% {
    transform: translate(-50%, -50%) scale(2.5);
    opacity: 0.6;
  }
  100% {
    transform: translate(-50%, -50%) scale(5.8);
    opacity: 0;
  }
}

/* Base pulse class (no color yet) */
.pulsePoint {
  position: absolute;
  transform: translate(-50%, -50%);
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.pulsePoint::before,
.pulsePoint::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  animation: vividPulse 3s infinite linear;
}

.pulsePoint::after {
  animation-delay: 1.5s;
}

/* Color modifiers */
.green {
  background-color: rgb(0,255,150);
}
.green::before,
.green::after {
  background-color: rgba(0,255,150,0.6);
}

.purple {
  background-color: rgb(255,100,200);
}
.purple::before,
.purple::after {
  background-color: rgba(255,100,200,0.6);
}

.blue {
  background-color: rgb(0,150,255);
}
.blue::before,
.blue::after {
  background-color: rgba(0,150,255,0.6);
}

</style>