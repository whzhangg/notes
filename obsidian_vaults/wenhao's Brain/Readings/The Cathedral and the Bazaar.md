# Cathedral and the Bazaar
This note is written at 2022/04/25

In this essay, the author is trying to convince us that open source project. This essay is written by [Eric S. Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymond), in 1997. Except linux, author also use GNU Emacs as an example, which is written by [Richard Stallman](https://en.wikipedia.org/wiki/Richard_Stallman)

### Working on projects
##### When to start
Author described several considerations when you decide to start a programming projects:
>Every good work of software starts by scratching a develop's personal itch

If you have problem with some software, somebody else would probably have it too and it will generally improve the code if you are able to solve it. It's a good opportunity to start a project.

Furthermore:
>If you have the right attitude, interesting problems will find you.

##### Constructive laziness
It's important to use minimum effort: It's always easier to start with a *good partial solution* than from nothing at all. Spending time looking for someone else's almost-good-enough is going to give you good results.

##### Improving the code
>The next best thing to have good ideas is recognizing good ideas from your users. Sometimes the latter is better.

And when we meet some design bottleneck, we should remember:
>Often, the most striking and innovative solutions come from realizing that your concept of the problem is wrong.

So that it is often time to ask not whether you've got the right answer, but whether you're asking the right question. Perhaps the problem needs to be reframed!

### Open source collaboration
##### Active release and listen to your users
Basically, early and frequent release are an important part to open source project development mode. When the source is available, debugging can happen early and quick, fix can be suggested by the users 
>Treating your users as co-developers is your least-hassle route to rapid code improvement and effective debugging.

At the same time, rapid release keeps the users (co-developer) constantly stimulated and rewarded.

>At the higher level of design, it can be very valuable to have lots of co-developers random-walking through the design space near your product. ..., exploration essentially by diffusion, followed by exploitation mediated by a scalable communication mechanism.

##### Bug
>Given enough eyeballs, all bugs are shallow. 

In the bazaar model, bugs turn out to be shallow when exposed to thousand capable developers looking at every single release. This is what make the linux kernel robust. 

Furthermore, the open source development mode also make debugging much easier when the users can look at the source code and find the issues by themselve.

##### Necessary conditions for the Bazaar style
To start an successful open source project, it is important that you need to present a plausible promise at the beginning, with strong, basic design. It may not be critical that the coordinator be able to originate designs of exceptional brillance, but *it's absolute critical that the coordinator be able to recognize good design ideas from others*. 

##### The social context
>While coding remains an essentially solitary activity, the really great hacks come from harnessing the attention and brain power of entire communities. The developer who uses only his or her own brain in a closed project is going to fall behind the developer who knows how to create an open, evolutionary context in which feedback exploring the design space, code contributions, bug-spotting and other improvement come from hundreds of people. 

In where real life is concerned, most of the aim can be achieved only through the severe effort of many *converging wills*, but on the principle of command.

Open source collaboration does not mean that individual vision and brilliance will no longer matter. Rather, the cutting edge will belong to people who start from individual vision, then amplify it through the effective construction of voluntary communities of interest. 

##### Creativity

>Gangs don't have breakthrough insights, Insight come from individuals. The most their surrounding social machinery can ever hope to do is to be responsive to breakthrough insigts. 

The root problem of innovation is how not to squash it, and even more fundamentally, it is *how to grow lots of people who can have insights in the first place*

>Joy is an asset

We do better because we have fun doing what we do. A happy programmer is one who is neither underutilized no weighed down with ill-formulated goals and stressful process friction. Enjoyment predicts eficiency. 
