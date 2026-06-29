# What makes a good personal project - from the perspective of a hiring manager

- **Subreddit**: r/datascience
- **Author**: u/dfphd
- **Date**: 2020-05-07 16:13 UTC
- **Score**: 634
- **Comments**: 57
- **URL**: https://www.reddit.com/r/datascience/comments/gf9hrs/what_makes_a_good_personal_project_from_the/
- **Post ID**: gf9hrs

## Post Body

We often see the question on this sub around "how do I build a portfolio as a student?", i.e., what projects should I work on?

If the resumes I've reviewed over the last 5 years are any indication, most people seem to think that the answer is a Jupyter Notebook that takes a pretty standard dataset, does EDA, builds a model, and presents a bunch of plots showing quality of fit.

From my perspective, these projects are pretty much useless. I say that because odds are that I can figure out if you can build such a notebook by just asking you a handful of questions and spending 5 minutes talking to you. Most importantly, being able to do that for a project that you chose (whether personal or capstone project) makes this project worthless in terms of helping me evaluate how you overcome obstacles - odds are that the way your overcame obstacles was by choosing a project that was easy to do and had relatively clean, available data.

So how do you make a better personal project?

**Start with a problem statement that is actually useful, even if you don't know how to solve it**

As a rule of thumb, an imperfect solution to a useful problem is better than a perfect solution to a useless one. I'd rather see you build a linear regression model to solve something that people actually care about instead of building a deep learning model to predict Titanic deaths. Why? Because problems that matter show a hiring manager that you can think through how to use data science to drive value. And if the process of getting there sends you down some windy roads, it also shows the hiring manager that you're able to navigate them. These are two *really* important skillsets.

Mind you, when I say "useful" I don't mean "important". I'm not telling you that you need to go find a cure for cancer, just to focus on something that *someone* will find a user for.

Example:

* Building a  model to optimize a fantasy football lineup.

Again, not important - just useful.

**Focus on a problem that goes beyond predicting a single metric**

A lot of data science "side projects" that I see focus on predicting a single quantity. While sometimes you will find yourself doing that in a work setting, most of the time your work goes beyond that, meaning you are normally predicting a quantity so that you can then influence a decision process, or estimate a broader outcome, etc.

So if you're going to work on a side project, try to follow through your model "all the way", i.e., through to an actual outcome that could be useful.

Example:

* Don't just predict the number of points a player will score in fantasy football - actually build that into a model that can help someone make decisions in a more complex setting (like daily fantasy football, or evaluating draft strategies).

**Start with ugly, raw data if you can**

If you start your project with mostly clean, post-processed data you've already skipped a big step in terms demonstrating what you can do. If instead you choose to go for something that isn't in its final form, you can flex a couple of different muscles.

For example, you could scrape data. Not super complicated, but it already shows me an extra skillset. Or you could start with data in log format and writing the necessary scripts to convert it into tabular form.

Example:

* Instead of starting with aggregate NFL stats, start with NFL play-by-play logs and write a script to convert "S.Barkley runs for 10 yard loss PENALTY Holding: NYG REJECTED" into the appropriate statline.

**If possible, build an actual product - not just analysis**

Building a product allows you a couple of advantages. For one, it allows you to just share a link to something that people can actually use. Secondly, if your tool were to get any traffic, it allows you to validate your idea. Lastly, it allows you to flex a completely different muscle - the fact that you can think through basic (or advanced) designs and deploy a solution to an environment.

Example:

* Build a web-app where people can make selections and your tool will output a recommended lineup in fantasy football.

**Work alone**

One of the big issues with group projects outside of a work setting is that it's hard for a hiring manager to corroborate what you did personally vs. what others did. That means that some hiring managers may just choose to assume that you didn't have a part in all of it - and worse, that you don't have all of those skills.

If you work by yourself, you can guarantee that an interviewer will assume that you did all of it, and there will be no questions of what you can/cannot do.

Some may say "but group projects show that I can work in a team!". And I think everyone that has ever worked in a group project knows that they seldom punish the person in a group who most lazy and hardest to work with.

Obviously this is just my opinion, but since the topic comes up often I figured it was worth putting it down to at least start a conversation.

## Comments

**u/luizgouveia** (score: 1)

Very, very useful post! Thanks

---

**u/vaitesh** (score: 1)

Very good post. As an amateur I am in a learning curve. This article did really made me realize towards what I should be focusing useful. Thanks for this post

---

**u/allkhush92** (score: 1)

Thank you so much for putting this together. Often I feel very bad about myself not working on those useless kaggle projects when I have a really challenging problem at hand (at work 😉).

---

**u/tyang209** (score: 1)

This is good and very useful.

But I also think for a personal project, you should limit the scope of the question.

Build a model to optimize a fantasy football lineup is a BIG problem. Reducing the scope of the question down to something like "Optimize a RB choice on a FF lineup" might be better for a personal project.

IMO, a personal project can also show off project management skill and being able to properly frame a data question around both the data and around real life constraints (workload, opportunity cost of projects) is very important.

---

**u/PhYsIcS-GUY227** (score: 1)

This is a really great write up. I wanted to address the issues in the **work alone** section.

I think most of the problems there can be solved if your team uses Git...that way you can show exactly what contributions each team member had. This also has the added benefit that you showcase your ability to use Git in a teamwork context which a lot of companies care about and use in their “real” projects.

---

**u/CarmelotheOG** (score: 1)

How would this advice change for someone trying to break in the field for more of an analyst role versus data science role?

---

**u/freecollegeguy** (score: 1)

This is really helpful. Thanks for this.

---

**u/MasterJaySC** (score: 1)

I want to emphasize those last 3 points in particular. So many people I've interviewed where we handed them raw ugly data and they had no idea how to deal with it. It's also super hard when asking people what they did in their previous jobs to parse out what they actually did vs. what their team did.

I will often ask probing questions, and more often than note I realize that pepole only did a very small part of what they initially talked about. It doesn't look great. Showing that you understand the point of a project end-to-end is crucial.

---

**u/FollowTheGradient** (score: 2)

Awesome post OP. As a hiring manager myself, I'd also add:

Be prepared to answer the WHY questions. Why that problem? Why it matters? Why those preprocessing steps? Why that model? Why those metrics? Why those outcomes? Why deploy this way? Why did it work/didn't work?

It can be written up in a blog post, a presentation, your Github readme, or just think a little about it before the interview. It matters both for personal projects and things that you've done at work and can't share online.

I've stopped counting the number of times I've heard answers that sounded like: "uh, I've used random forest." and when asked why: "because, uh, it seemed like a good idea?" Please don't that.

---

**u/cyran22** (score: 3)

When I  was a student I did a project where we just used multiple linear regression to predict what end of year season fantasy football points would be so we could form better drafts beginning of season. Hiring managers loved this project example when I went for intern interviews.  They didn't care or understand about our other neural networks project (and now I see why).

We learned all kinds of things that we were seriously lacking before like
Where to get data
How to aggregate and join the data
How do we handle players without previous seasons data
Why are these positions predicting better than these other player positions

And we didn't even build a tool to build weekly lineups or anything.

Basically just saying I agree with OP and it's interesting that I did a very similar project as his example project.

---

**u/BellaJButtons** (score: 1)

If a project was on git, would the hiring manager not check commits to see what you contributed to a group project ?

> **u/dfphd** (score: 3)
>
> Yes, but that only allows to measure the pure programming side of things. It doesn't tell me anything about who decided what should be coded, or who framed the problem, or who decided on the solution methodology, or who designed the end product.

> > **u/BellaJButtons** (score: 1)
> >
> > Oh, That makes sense, of course.  For our final bootcamp project I had the idea to make a sign language reader, you could take a photo of a ASLhand gesture and ML would tell you the letters. I thought of it myself while watching the rock paper scissor demo for tensorflow and didn’t see why I wouldn’t be able to do it.  I had one partner for the project, but he was someone who worked a lot and was my friend in the class so I felt bad to not allow him to partner with me. However, I did 99% of the (including the framework of what needed to be implemented/created) work from creating the datasets (used 3 skin tones with multiple angles) , building the website to training the model to creating the flask and the cloudinary account to collect uploads to the machine and back to output. I had to learn an extensive amount on my own. I thought it would be apparent who did all the work since almost all the commits are mine,   How should I highlight that I basically did this on my own to a hiring manager without sounding ... tacky?

> > > **u/[deleted]** (score: 1)
> > >
> > > >blem? Why it matters? Why those preprocessing steps? Why that model? Why those metrics? Why those outcomes? Why deploy this way? Why did it work/didn't work? It can be written up in a blog post, a presentation, your Git
> > >
> > > Just write down what you did. Hiring managers can easily tell if you lied or not by asking follow up questions.

> > > **u/dfphd** (score: 3)
> > >
> > > That's a good question.
> > >
> > > We'll, firstly, you don't need to say it was a group project in your resume. So when you're discussing this would be during an interview.
> > >
> > > I think it's fair, if you're asked, to say something like "I was in charge of all the technical development and did nearly all the programming work".

> > > > **u/BellaJButtons** (score: 1)
> > > >
> > > > That makes sense, that’s how I’ll handle it. Thank you, I really appreciate your feedback on this.

---

**u/J1nglz** (score: 0)

Find problem that they don't know they have and solve it. I'm up to $700k for my team with $8mil in licenses per year. 2 staff 3 interns. Out of NOTHING.
My DOD contractor level 4 job didnt exist till I got hired n as an L3 that wandered the halls for 2 months with no direcrion.
I was like nah I dont do documentation stuff then showed them all the shiny stuff I do. A lot of AI/ML. A lot of Visio graphics! Just to show whalere I'm trying to go. They now have predictive analytics. More funding on the horizon. This all started when my chief manager got CCed on a meeting I was having with higher ups. He come by after and said," Your pet project just turned into a program pilot."

---

**u/rotterdamn8** (score: 3)

This is great stuff. This should be pinned if it were possible in a sub. It could save many people from asking how or what kind of portfolio to produce.

I was wondering myself. I'm only 1.5 years as an analyst.

---

**u/Hellr0x** (score: 2)

I would love to hear competent advice.

I often read that it's a good idea to launch the ml model online with a simple page (probably built in flask) and that can be a good showcase of what I've done. But that doesn't show the steps I've taken to choose this or that model; what analysis I have performed before deriving to that decision and how that decision is justified etc.

If I want to showcase the mathematical/statistical knowledge applied to the topic I'm interested in how should I present the project? write a report? presentation? if you are hiring what would be the most effective medium for you?

> **u/dankerton** (score: 1)
>
> What does the model do and how is it useful? Is there a web app that can make use of it? If so then make the webapp. It's not there to show your work. It's there to attract attention and show you're a rounded product building data scientist. Have a PowerPoint on hand that tells a more detailed story or just be ready to answer interview questions on it.

---

**u/soon2bvoid** (score: 2)

I agree. Out of all the projects I did during my graduate school, the toughest one was annotating web scraped social media data.

---

**u/ticktocktoe** (score: 25)

I don't always see eye to eye with things that /u/dfphd posts, but, as a hiring manager as well, this is pretty spot on.

> If the resumes I've reviewed over the last 5 years are any indication, most people seem to think that the answer is a Jupyter Notebook that takes a pretty standard dataset, does EDA, builds a model, and presents a bunch of plots showing quality of fit.

So. Many. Kaggle. Examples.

Seriously, its almost an instant 'nope' if I see another kaggle housing data set personal project. I've even had a few people show me problems on the iris data set.

Solve something real and unique, that YOU find interesting, and not just for the sake of solving it, do it because you're passionate about learning and exploration, and because you see an actual gap that can be filled.

Quality post.

> **u/liljepp** (score: 5)
>
> I'm actually surprised that people are still showcasing their analyses of the Kaggle housing data set. That leads me to believe they may be plagiarizing because there are thousands of interesting datasets (just found a wine review dataset within 2 minutes of searching) on Kaggle...the only reason to show a housing dataset analysis is if they aren't confident in their ability to create their own analysis from scratch.

> > **u/ThumbWarHero** (score: 2)
> >
> > Kaggle has a step-by-step tutorial of how to analyze the housing dataset, so they are probably following that

> > > **u/bukakke-n-chill** (score: 2)
> > >
> > > I think that's what he meant by plagiarizing. Even if they change a few parts it's still mostly not their own work.

---

**u/Kryma** (score: 0)

Does it count as messy data if I had to use samsung dex connected to my phone to screenshot call logs with a script, then process through OCR to get a detailed call history out of whatsapp as an additional step to a "standard" whatsapp chat analysis to analyze call history that's not available to download?

> **u/dfphd** (score: 2)
>
> https://giphy.com/gifs/community-ill-allow-it-146heXDX89mUgw

> > **u/[deleted]** (score: 1)
> >
> > How is that messy data? Of course it sounded like pain in the ass to get the data, but if you don't have to do any data cleaning then it's not messy.
> >
> > I'd appreciate more if the data collection process was simple, but what you get is not really good and you have to do some manipulations like filling in missing data, remove bad reads, etc.

> > **u/Kryma** (score: 1)
> >
> > Fantastic. I'm still learning, so trying to figure out how to properly present it on github, but this was one of the most difficult things I've done so far in regards to coding. That process was a pain and the data was still a mess that needed regex to clean up more after OCR. Any suggestions on where to post things like that for a github/code review to help me realize all the massive mistakes I made?

---

**u/MattDamonsTaco** (score: 11)

This is great. I've hired more than a few junior DS and some analysts and they always have that standard suite of github repos that all have the same stuff. I've always thought that someone taking a real, *new* problem and building out a potential solution or calculator--even without actual data--would go a long way in helping me understand how they think.

I'd love to see someone take a simple problem

> how many push mowers vs. riding lawnmowers vs. manual laborers should a landscaping company have?

then tease apart the data required and simulate it, if possible, then build the tool to show me how to use your model. Doesn't have to be *real* data but take a real problem (or "opportunity," as a previous boss referred to them) that you think a company might have then try and solve it. Don't have any data? Simulate some based upon your knowledge of prob distributions. Make well-reasoned arguments and show me your thought processes behind why.

"Personal projects" don't have to solve THE BIG business problem just *a* problem. Most importantly, they help hiring managers understand your thought processes. Please, please, **please** don't just take a Kaggle titanic tutorial and `ctrl+c, ctrl+v` into a notebook.

> **u/MindlessTime** (score: 3)
>
> > how many push mowers vs. riding lawnmowers vs. manual laborers should a landscaping company have?
>
> Is this a data science problem? This is a pretty straightforward linear programming optimization problem that you could figure out using Solver in Excel. If I saw someone simulate data, do a bunch of EDA, etc. to answer this question I would think they’re only able to apply ML solutions to any problem they see. I’d be less impressed.

---

**u/WillingAstronomer** (score: 4)

This should go into the wiki!

---

**u/electricIbis** (score: 1)

How can I go from predicting a single metric to building a model for more complex settings?

I am taking classes in a big data program and the biggest thing I see lacking is how to follow through. Like you said we have done predictions and such but now that I'm working on more complex projects I'm drawing blanks on how you move after that. Most examples I see online are also just predicting one metric.

Where can I learn/see examples of this so I can learn how to do it?

> **u/HiderDK** (score: 2)
>
> create a model where the overall goal is to predict the win-probability of the game after every play. The way you could do this is to simulate future plays until the game is over. For each simulation you generate distribution of probable outcomes along with the probability for whether its a run or a pass. This method allows you assess the value of every single play that occurs in the game in relation to the change in expected win probability.
>
> Further you would also be able to assess whether its better to run or throw the ball. If you wanna build further on top of it, you could rate each QB and RB on this model.

> > **u/electricIbis** (score: 1)
> >
> > This is an interesting take, I think I see what you mean. So basically, you make small predictions and then find a way to put them together to obtain a final conclusion.
> >
> > For example, if I am interested in predicting whether a machine is going to fail. I have seen a classification example where they take the failure and label it as such, then some period before the failure labels as "about to fail" for example, and then records before this as "normal" or something like that. Such that the model could detect when it's in that "about to fail" range, essentially giving you a warning.
> >
> > That being said, that would still be predicting a single metric no? I am trying to follow your analogy, but I'm not sure how to implement more metrics that would help me predict a failure. Maybe like I can tell if I am close to failure, then create other model that could try and predict what the reason could be?

> > > **u/HiderDK** (score: 2)
> > >
> > > > . So basically, you make small predictions and then find a way to put them together to obtain a final conclusion.
> > >
> > > Well me process is the other way around. I create an entirely modelling approach consisting of a coding projects that has many different functions/classes within.
> > >
> > > Then for some of the function I need to predict some smaller sub-parts in which I guess I might use some machine-learning models.
> > >
> > > E.g. in the case of how well a pass is gonna perform for a QB I might look at the strenght of the enemy team, previous performance for the QB, context of the game etc. Basically every historical data-points that increases the accuracy in predicing what will happen in the next play.
> > >
> > > >  I am trying to follow your analogy, but I'm not sure how to implement more metrics that would help me predict a failure.
> > >
> > > So the above approach isn't always ideal. It's only ideal when you can break it down into smaller isolated parts. In your situation it might be entirely plausible that it's not feasible.

> > > > **u/electricIbis** (score: 1)
> > > >
> > > > That's fair on your last point. Thanks for the explanation and sorry for the super late delay btw

> **u/jmortin** (score: 3)
>
> Classification problem naturally has multiple core metrics—at least precision & recall, but also f-score and different area under curves. Moreover, experimenting with changing decision thresholds is also often (in my experience) rewarding for performance, which is another dimension of measuring classification performance. Best thing: good classification problems are very easy to find.

> > **u/electricIbis** (score: 1)
> >
> > These are metrics to confirm your classification is good/precise, right?
> >
> > As I understood the OP, they mean like predict one thing that should let you predict a second thing. ex. predict number of points a player can make, then do that for all players in each round to help make decisions in order to win the league.
> >
> > I am just having a harder time picturing it in regards to things like machine failure as it seems less sistematic in my mind.

---

**u/noahpoah** (score: 1)

Thanks for this post. It's extremely useful.

I'm curious if you (or anyone else in the sub) has any advice on generating questions/projects that will be good indicators that my data science will add value.

I have what I assume is a fairly unusual background for this kind of thread. I have a PhD in Linguistics & Cognitive Science and an MS in Applied Statistics. I've worked as an I/O Psychologist/Applied Statistician (job title: research scientist), as a tenure-track professor running a lab, then as a data scientist at a FAANG company. I'm currently back in an I/O Psych role (research scientist again).

One of the things I learned as a data scientist was that my CS, programming, and related knowledge and skills were weak, especially compared to my knowledge and skills with study design and stats. I've been putting a lot of effort into learning in those areas (e.g., algorithms, software engineering, production data science/ML tech stacks), and I'm feeling way better about all this (and I continue to be excited to study and learn this stuff).

But I'm acutely aware of, on the one hand, the kinds of questions people wanted answers to when I was an industry data scientist and, on the other hand, my lack of access to the data relevant to answering these questions.

I would like to think I'm good at talking to people with questions, figuring out what, exactly, they want to know and why, figuring out how to use data to answer the questions, and then doing so (part of why I left my TT position was that I like working on teams in this kind of role).

I'm getting better at the data engineering side of things (and this post confirms that I was right to think that it's important to be able to get from messy, relatively unstructured data to nice, clean(ish) tables), but I'm feeling a lot less confident thinking of good questions, where by good I mean, again, indicative of added value.

> **u/dfphd** (score: 3)
>
> You lost me - can you try to summarize your question a bit more concisely?
>
> Are you looking for advice on being able to evaluate whether a project will add value to the company?

> > **u/noahpoah** (score: 2)
> >
> > I was wondering if you have advice for generating good DS questions/projects, where good means indicative of my ability to add value.
> >
> > So, yes, I want to be able to evaluate projects for their value, in part so that I can evaluate project ideas of my own as I build out my skill set.

> > > **u/dfphd** (score: 5)
> > >
> > > You can make this really complicated, but generally speaking the things you are looking for are:
> > >
> > > 1. Upside: that is, opportunities where the existing solution either doesn't exist or it's really bad or you already know you can improve them greatly. This allows you to establish that there is a lot of room for improvement.
> > > 2. Scope: the total number of units/dollars/etc to be impacted.
> > > 3. Frequency: how often does this process/decision/event happen?
> > >
> > > These are multiplicative. Find opportunities that rank high across all three and you'll be in a good spot.

> > > > **u/noahpoah** (score: 1)
> > > >
> > > > Thanks.

---

**u/Single_Blueberry** (score: 2)

Awesome insights, thank you! I wish we could get these for other engineering disciplines, too.

---

**u/speedisntfree** (score: 6)

> most people seem to think that the answer is a Jupyter Notebook that takes a pretty standard dataset, does EDA, builds a model, and presents a bunch of plots showing quality of fit.

But then I'd have to think and not copy a tutorial online or kaggle kernal

---

**u/GalacticTurtleBu** (score: 3)

God bless you.

This post has helped me out so much, I greatly appreciate your time and effortto write it out.

---

**u/nf_highlights** (score: 13)

One good thing is if a capstone/personal project is also relevant to the industry that you are in (aka please don't use Titanic).

If you're in Finance, modeling on the lendingclub dataset (https://www.kaggle.com/wendykan/lending-club-loan-data) is always interesting. In retail, the ecommerce data transaction dataset (https://www.kaggle.com/carrie1/ecommerce-data) is good.

---

**u/[deleted]** (score: 31)

A somewhat related question:
As someone new to the field (2 years, w/ a B.S.), how can I show what I've done? I currently work in academia with student data, so I can't just throw things up on my private github.

Also, one thing I keep seeing is that you should build up these extra curricular portfolio, and to me it just seems bonkers - like I'm already overworked, and the last thing I want to do is spend my evening/weekend is fucking around with another data set. I love what I do on a daily basis, but holy shit do recruiters have some high expectations.

Just had to get this off my chest. I'm tired, sick of applying for 300+ jobs in a pool of 2000 each, and coming to the realization that going to college is not paying off.

> **u/schonde** (score: 1)
>
> Just spit balling here and apologies if you already do this. Sounds like you should change the odds in your favor. Two thoughts are:
>
> Narrow your list substantially, network with managers and employees to get a referral, and don't be discouraged in reapplying. We know we are (overly?) strict in the loops and if you make, e.g., one mistake on the technicals you'll not advance.
>
> Get a mentor in a position you want with substantial experience interviewing that can help you prep.

> **u/dfphd** (score: 25)
>
> This is my opinion, and certainly not shared by every hiring manager:
>
> A portfolio is more relevant for people looking to break into the field, i.e., people who don't yet have real world projects to discuss.
>
> If you do have experience, your resume should then show that, and it's reasonable as a candidate to not feel like in addition to having relevant work experience, you now also need to go put together an additional portfolio of extracurricular projects.
>
> Personally, for someone with more than 1 year experience, I don't care about your personal projects at all unless it's something amazing.
>
> Now, some jobs/companies/hiring managers, specifically those looking for heavier R&D experience, might be looking for a portfolio because that's the environment they live in - open source work, more transparency, etc. But I think even they would understand that people in certain industries don't really have the ability to make their work public - often due to the sensitivity of the data, but often because companies want to protect the IP their employees generate.

> > **u/gandalfgreyheme** (score: 3)
> >
> > I'm a hiring manager and I'd concur.
> >
> > With real-world work ex, I'd focus on that and try to glean out the difference between what you claim you did and what you actually did. I'd also try to understand if you are able to connect the dots to actual business value as opposed to geeking out on a tool.
> >
> > PS: (fantastic post OP)

> > > **u/FollowTheGradient** (score: 3)
> > >
> > > I agree with that. Personal projects are not necessary if you have experience. However, anything you can do that shows me that you care will be a big plus. It can be a project, a Kaggle competition, a blog, answering questions on StackOverflow, online classes that you do for fun, whatever.
> > >
> > > What I'm always looking for is evidence of passion and self-directed learning.

---

**u/nafferly** (score: 20)

Totally agree. Being a data scientist is as much about creative problem solving and critical thinking as it is about technical skills. Show the hiring manager that you can pull a question out of the abstract, and then make an interesting explanation for it using your skills. Pick a topic that makes people think, “huh, that’s cool!” The publication “The Pudding” is a good source for ideas like this.

> **u/TheOuts1der** (score: 7)
>
> Link for the lazy! https://pudding.cool/

> > **u/culturedindividual** (score: 1)
> >
> > >https://pudding.cool/
> >
> > Would be cool to make a frontend API like this for an MSc dissertation project.

---

**u/riggsmir** (score: 76)

Awesome write-up, I’m not a hiring manager but I totally agree on this. Don’t just work on a project to build your portfolio, but find a problem that’s actually interesting to you.

Along with the numerous benefits OP posted above in regard to overcoming challenges (particularly the messiness of data), I personally think passion about a project makes it a lot more valuable when explaining it to an interviewer (and also it’s more fun for you to work on!).

> **u/dfphd** (score: 27)
>
> Agreed - I also think it makes it more likely that you can engage in a deeper conversation about the business and data science concepts and how they interact.
>
> For example, my favorite way of explaining over-fitting is to say "if you wanted to predict running back production and you overfit your model, you will find that the best running back performance happens when they play at Oakland in December when the opposing QB's name is Matt and the game is played at 3:05PM EST and less than 50K people attend the game".
>
> Aka, the day that Jamaal Charles went for 215 total yards, 8 receptions and 5 TDs.
>
> I don't doubt that most people here understand overfitting, but applying data science to something you're passionate about helps you tie many data science concepts into more intuitive narratives that are easier to talk about and explain to others.

> > **u/Severe-Focus** (score: 15)
> >
> > Weird, my model suggests that the best RB performance happens when the RB's first name has six letters, their head coach is named "Brad", and the game happens on November 4, 2007. You must have made an error somewhere ;)

---
