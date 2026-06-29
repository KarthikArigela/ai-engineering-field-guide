# Data science projects that helped land a job/internship

- **Subreddit**: r/datascience
- **Author**: u/AccomplishedCraft897
- **Date**: 2023-09-04 06:09 UTC
- **Score**: 86
- **Comments**: 25
- **URL**: https://www.reddit.com/r/datascience/comments/169jwcn/data_science_projects_that_helped_land_a/
- **Post ID**: 169jwcn

## Post Body

 Hi everyone,

I'm looking for a job or internship in the data science/analytics field. I'm quite comfortable with scikit-learn and PyTorch.

I'm wondering what projects helped you land your first job or internship in the data science field. I'm interested in projects that are both challenging and relevant to the real world.

If you have any suggestions, please let me know in the comments. Thanks!

## Comments

**u/bin-c** (score: 2)

anything you can talk about that shows some technical skill and problem solving ability. doesn't really matter what it is

&#x200B;

i have done quite a lot of interviewing. i could give a shit that you classified titanic survivors, or mnist, or anything else that is a common tutorial problem (even if its more complex)


i want to hear what you came up with, *why* you were motivated to do it, what problem it solved, and how you came up with that solution. even a simple little thing that makes your life better is much more interesting for me to hear about than some off the shelf kaggle problem

---

**u/takuonline** (score: 6)

Here is [mine](https://www.takuonline.com/#my-work).l named it savvy shopper and It helped me get my first stable job. Basically it comprised of a web scraping server, a database to store price data, a backend for both etl ( read, transform) and also serve data to a mobile app frontend. Not strictly data science but it was a lot of fun

> **u/Thinkmovement** (score: 2)
>
> Thanks for the link Taku, I'm working on a portfolio site as well and have recieved a few bits of feedback that I think might help you as well. Love the look overall:
>
> 1. **Tagline:** *"I a*I More metrics in your "My Experience" section. What has your research and modeling done in terms of user retention, market capitalization, and funding prioritization?your contact me. Links to the relevant projects or description of your mastery of specific technical/application-based skills or successful implementations.ills that you might have. Everyone wants to use AI, innovate and make an impact, but what tech are you proficient with that a company can leverage? Displaying a clear skillset in your tagline goes a long way, as it's one of the first things they'll see to gauge if you meet the minimum requirements.
> 2. **My Services:** It would be great if these were a drop-down that gives an overview of what you can offer for each of those services/skill sets rather than all directly linking to your contact me. Links to the relevant projects or description of your mastery of specific technical/application based skills or successful implementations.
> 3. **My Experience:** More metrics in your "My Experience" section. What has your research and modeling done in terms of user retention, market capitalization, funding prioritization?
> 4. **My Work:** *"I possess a unique blend of expertise in utilizing data to drive business decisions and creating innovative technology solutions",* again a bit generic for the "My Work" section. What makes you have this unique blend? Everyone says they are unique, but what core technologies and experience do you have to back this up? I saw you link your Git at the bottom, which is fantastic, but linking within each project would be nice.

---

**u/samjenkins377** (score: -1)

This sub should be just renamed r/DSCareers at this point… mods in the mud

---

**u/aGuyAndHisWood** (score: 1)

The first internship generally comes by applying to a lot of places and then interviewing well.

My resume only said that I knew data science when I landed my first internship in the field and I landed it because I was great at interviewing.

> **u/Unkilninja** (score: 1)
>
> where did you applied bro , what type of company it was  and was it paid ?

---

**u/FunLovingAmadeus** (score: 3)

Basically linear regression on some real data: https://github.com/Tareq62/solar_panel_model

---

**u/Prestigious_Sort4979** (score: 3)

For my FIRST job, I used exploratory data analysis projects including one with a nice deck (going over the problem and findings) and a public Tableau dashboard. They were all neatly in Github or linked when appropriate. Keep in mind what you will actually be doing as an entry-level person. I had some basic ML projects but my hiring manager was much more interested in projects that more closely resembled the work I would do in the near future.

---

**u/The_Mootz_Pallucci** (score: 2)

Found what sector i wanted to be in, got industry dataset off old kaggle competition, did a small project and spoke to it during interviews

---

**u/Cosmic_Dong** (score: 17)

From the perspective of someone who hires juniors/interns, I can say that I really don't care _what_ your projects on your CV are about (unless they are highly specific which is very unlikely).

As long as there is a decent level complexity to them what matters most to me is that you have a good grasp of the work itself and when I ask questions about it we can have an interesting discussion about it. Heck, the last intern we hired (who's now my junior colleague) corrected a faulty assumption of mine that I made about his work, and then we went on to have a nice detailed discussion about it. Which I thought was fantastic!

So, I'd say find a project you know you will enjoy working on and do it thoroughly.

> **u/ANIMA121** (score: 0)
>
> My project is the forecasting of the stock market, i used the LSTM model and built a dashboard using power bi, what are some interview questions you might ask on this ??

> > **u/Cosmic_Dong** (score: 3)
> >
> > I guess I'd question why you're using a neural network to do the modelling in the first place and talk about that.
> >
> > An answer along the lines of you wanting to learn about them would be perfectly fine, then I'd inquire about what you've learned and go down that rabbithole (biggest obstacle, if you tried other methods, etc.)
> >
> > If you answer along the lines of it being the best approach, I'd ask about why.
> > Particularly because stocks have long been modelled using Brownian motion (this is what the first quants were doing) where there are no long-term dependancies.
> > Does your model beat such a simple model? No? Why not then? Yes? How come? Can you explain which features lead to the better performance? Would other types of models offer better explainability? Then, given the fact that I work with transformers I'd ask if you could imagine a transformer-based model doing the same thing.

> > > **u/ANIMA121** (score: 1)
> > >
> > > Thanks for answering, there was an online test schedule for me that why I wasn't able to reply  earlier.
> > >
> > > First, i wanted to build a stock market dashboard where i can access all the information about a company (news, volume, fundamental, technical)and its prediction in one place that's why I built this project
> > >
> > >
> > > 2- i used LSTM because of the memory storage and yes i wanted to learn the neural network and I got to know the time series analysis LSTM is great and as the data has minimas used Adam optimization
> > > Yes I looked at other methods like decision trees (but processing power of my computer was not that good and LSTM store data in short memory block and GPU compilation is little less in comparison i used this ) but there was not much effect on prediction as 45% was from my LSTM model which is pretty decent for stock market ig
> > >
> > > 3- I know basics of machine learning and brownian motion idk 😶 I willl look into it thank you
> > >
> > >
> > > 4- The transformer might perform better in this way as they allow for better parallelization during training. This is because transformers use the self-attention mechanism, which does not rely on sequential computations like LSTMs but as I was not using parallel computing and my CPU power is not great I used LSTM with little tweek to work on my computer GPU compilation
> > >
> > > Please if you can look into my resume that would be a great help

---

**u/Dapper-Economy** (score: 6)

Anything time series and predictive

> **u/CaterpillarOk7556** (score: 1)
>
> >Anything time series and predictive
>
> can you please elaborate? why those two in specific?

> > **u/Dapper-Economy** (score: 1)
> >
> > From my experience interviewing, I’m usually always tested on a time series data science question/project. I also think simple predictive models are a good place to start to add to your resume. Some other ideas could be automation or NLP projects as well.

> > > **u/CaterpillarOk7556** (score: 1)
> > >
> > > appreciate the reply. i'm currently applying for masters degree or internships. and been having trouble finding project ideas that balance personal interest, novelty, and being appropriate to put in a resume

---

**u/AM_DS** (score: 19)

I would recommend you to start by creating a website where you can share your projects. With GitHub Pages is straightforward to do so, and it's also free.

Then I recommend you to do projects that look interesting for you. I don't recommend you doing the typical projects that can be found everywhere (Titanic, forecast stock market, etc.). For example, a project I've been thinking about is to download all you WhatsApp/Telegram messages, and then train a model that predicts the next word. This way you can build a model that speaks like you (I find interesting to chat with yourself). But this is only one example, I recommend you to think which problem you would like to see solved and then do it yourself.

Also, I recommend you to not only focus on the machine learning part. I would try to build a project that seems like a real project (data pipelines, data storage, data cleaning, CI/CD, automatize everything, VCS, etc.)

> **u/mountainriver56** (score: 1)
>
> How would you go about creating a website on GitHub pages? Basic html/JavaScript/css files? I read there is also a markdown type language on GitHub that you can use as well.

> > **u/AM_DS** (score: 1)
> >
> > GitHub Pages has native support for Jekyll, which allows you to write your pages directly in markdown.

---

**u/Creepy_Angle_5079** (score: 88)

Avoid very common projects
Ex) Titanic survival classification, MNIST CNN classification,

Class projects are normally great opportunities. I did a ML project in a Bioinformatics class and I have it on my resume

Kaggle is a good resource for clean datasets

The most important aspect about having projects on your resume is as a talking point in an interview.

The data scientist interviewing you wants to know that you’ve learned more than the .train(), .predict() pattern.

Being able to explain things like

“I noticed that there was a lot of missing data in my dataset, so I used _____ imputation BECAUSE ________”

“I used ______ feature selection process BECAUSE I wanted to ______”

In the end, I evaluated the model with _____ metric BECAUSE _____”


is the most important thing, and will set you apart from 99% of applicants.

> **u/GreenFractal** (score: 1)
>
> When you say you have a ML project on your resume, does that mean a link to the github repository or something else? I have one project in mind, but I'm not sure if that's the common way to present it on a resume.

> > **u/Creepy_Angle_5079** (score: 1)
> >
> > Should have a projects section to list projects and a few bullet points of descriptions. Templates are everywhere

> > > **u/GreenFractal** (score: 1)
> > >
> > > Gotcha, thanks!

> **u/AerysSk** (score: 22)
>
> Join a real Kaggle competition, and real here does not mean Titanic nor MNIST. I suggest looking at the dataset size, since a big dataset requires a complete different approach than can-be-fit-on-a-single-GPU datasets.

---
