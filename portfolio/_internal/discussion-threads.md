# Portfolio Project Discussion Threads

Reddit, Hacker News, and X/Twitter leads. Raw fetched Reddit artifacts live in [fetched/reddit-posts/](fetched/reddit-posts/). Grok raw responses live in [fetched/grok-responses/20260629_151010_portfolio-projects-public-perspectives.json](fetched/grok-responses/20260629_151010_portfolio-projects-public-perspectives.json) and [fetched/grok-responses/20260629_152641_ai-engineer-portfolio-reddit-x.json](fetched/grok-responses/20260629_152641_ai-engineer-portfolio-reddit-x.json).

## Reddit

1. [Data science projects that helped land a job](https://www.reddit.com/r/datascience/comments/169jwcn/data_science_projects_that_helped_land_a/) (r/datascience, fetched) -- hiring/commenter advice: avoid common Titanic/MNIST-style projects; projects matter as interview talking points; explain decisions, data issues, and trade-offs. Local: `fetched/reddit-posts/datascience_169jwcn_data_science_projects_that_helped_land_a_20260629_151023.md`.
2. [What makes a good personal project from the perspective of someone who reviews resumes?](https://www.reddit.com/r/datascience/comments/gf9hrs/what_makes_a_good_personal_project_from_the/) (r/datascience, fetched) -- resume-reviewer perspective on personal project strength. Local: `fetched/reddit-posts/datascience_gf9hrs_what_makes_a_good_personal_project_from_the_20260629_151024.md`.
3. [People who make hiring decisions, what do you want to see in a portfolio?](https://www.reddit.com/r/datascience/comments/ujmhtt/people_who_make_hiring_decisions_what_do_you_want/) (r/datascience, fetched) -- hiring-manager checklist: dirty data, API/database work, model choice, interpretation, and plain-English explanation. Local: `fetched/reddit-posts/datascience_ujmhtt_people_who_make_hiring_decisions_what_do_you_want_20260629_151055.md`.
4. [People who hire, what are some of the must-have projects on a CV?](https://www.reddit.com/r/datascience/comments/19cyhaq/people_who_hire_what_are_some_of_the_must/) (r/datascience, fetched) -- best projects start from a standalone business-like problem, not "show neural networks." Local: `fetched/reddit-posts/datascience_19cyhaq_people_who_hire_what_are_some_of_the_must_20260629_151055.md`.
5. [How important is it to have a data science portfolio?](https://www.reddit.com/r/datascience/comments/186w5ak/how_important_is_to_have_a_data_science_portfolio/) (r/datascience, fetched) -- portfolio helps more when you lack relevant experience; copied tutorials/common datasets do not impress. Local: `fetched/reddit-posts/datascience_186w5ak_how_important_is_to_have_a_data_science_portfolio_20260629_151055.md`.
6. [Software projects that get recruiters' attention](https://www.reddit.com/r/cscareerquestions/comments/1m5ek9x/software_projects_that_get_recruiters_attention/) (r/cscareerquestions, fetched) -- real users/impact or OSS contributions beat calculator-style apps. Local: `fetched/reddit-posts/cscareerquestions_1m5ek9x_software_projects_that_get_recruiters_attention_20260629_151055.md`.
7. [What hiring managers actually care about after screening 1000+ portfolios](https://www.reddit.com/r/datascience/comments/1s9m26c/what_hiring_managers_actually_care_about_after/) (r/datascience, lead) -- recent lead; prioritizes clarity, impact, communication, problem framing, decisions, outcome, and next steps.
8. [Do employers still care about personal projects?](https://www.reddit.com/r/cscareerquestions/comments/1nvytmp/do_employers_still_care_about_personal_projects/) (r/cscareerquestions, lead) -- mixed views: high-quality projects help; sloppy/tutorial projects can hurt; some companies ignore them.
9. [Are recruiters even looking at my GitHub or portfolio website?](https://www.reddit.com/r/cscareerquestions/comments/1btmeqx/are_recruiters_even_looking_at_my_github_or/) (r/cscareerquestions, lead) -- candidate anxiety: portfolio fields exist, but recruiter attention is inconsistent.
10. [What kind of projects are employers looking for?](https://www.reddit.com/r/cscareerquestions/comments/1prpt1m/what_kind_of_projects_are_employers_looking_for/) (r/cscareerquestions, lead) -- high-profile or niche OSS contributions matter when relevance is clear.
11. [What projects are good these days?](https://www.reddit.com/r/cscareerquestions/comments/1mz5eou/what_projects_are_good_these_days/) (r/cscareerquestions, lead) -- match projects to target domain: ecommerce, banking, medical, project management, content platforms.
12. [Unique machine learning projects](https://www.reddit.com/r/learnmachinelearning/comments/1gvk23l/unique_machine_learning_projects/) (r/learnmachinelearning, lead) -- everyday/local data and domain experts can make projects less generic.
13. [Should I do a senior capstone project?](https://www.reddit.com/r/cscareerquestions/comments/1rxsd8/should_i_do_a_senior_capstone_project/) (r/cscareerquestions, lead) -- older but useful: team programming projects are valued when experience is thin.
14. [I attended a bootcamp career day through work and saw capstone projects](https://www.reddit.com/r/datascience/comments/d6wgmp/i_attended_a_bootcamp_career_day_through_work_and/) (r/datascience, lead) -- strongest capstones showed model choice, data understanding, model-output understanding, and clear presentation.

## Reddit - AI Engineer Focus

1. [Everyone here posts the same AI engineer roadmap](https://www.reddit.com/r/learnmachinelearning/comments/1t7kc8k/everyone_here_posts_the_same_ai_engineer_roadmap/) (r/learnmachinelearning, lead) -- based on 425 AI engineer job descriptions; says generic chatbot projects are overdone and evals are missing: RAGAS, golden datasets, trace logging.
2. [Roadmap/resources to become a GenAI/LLM engineer](https://www.reddit.com/r/learnmachinelearning/comments/1uehd6h/roadmap_resources_to_become_a_genai_llm_engineer/) (r/learnmachinelearning, lead) -- advice to ship something with real evals and an observable production setup; interviews ask about chunking, embedding choice, latency, cost, and scaling.
3. [Graduating soon: can a RAG project help me land a job?](https://www.reddit.com/r/learnmachinelearning/comments/1s2el6h/graduating_soon_can_a_rag_project_help_me_land_a/) (r/learnmachinelearning, lead) -- RAG project advice: clear README, small demo, and explanation of why the approach beats naive search.
4. [Building an AI portfolio as a web dev: how to keep costs low?](https://www.reddit.com/r/learnmachinelearning/comments/1sqpy2n/building_an_ai_portfolio_as_a_web_dev_how_to_keep/) (r/learnmachinelearning, lead) -- use local sentence-transformers, Postgres/pgvector, free deploy tiers, and a README that explains architecture and production concepts.
5. [Basic skills to be an AI engineer](https://www.reddit.com/r/learnmachinelearning/comments/1puojnb/basic_skills_to_be_an_ai_engineer/) (r/learnmachinelearning, lead) -- emphasizes FastAPI, Docker, logging, monitoring, error handling, CI; two end-to-end projects beat ten notebooks.
6. [From software developer to AI engineer](https://www.reddit.com/r/learnmachinelearning/comments/1pzcw2y/from_software_developer_to_ai_engineer_the_exact/) (r/learnmachinelearning, lead) -- first-person transition story; clean GitHub repos, detailed READMEs, demos, deployed apps, monitoring, and token latency helped with recruiters.
7. [Best agentic AI course](https://www.reddit.com/r/learnmachinelearning/comments/1t6xjix/best_agentic_ai_course/) (r/learnmachinelearning, lead) -- build and deploy real agents; include tool use, memory, evals, observability, demos, GitHub, and LinkedIn proof.
8. [Is this a good roadmap to become an AI engineer?](https://www.reddit.com/r/learnmachinelearning/comments/1rpc5gc/is_this_a_good_roadmap_to_become_an_ai_engineer/) (r/learnmachinelearning, lead) -- AI engineer projects should include eval sets, baselines, retrieval/tool success metrics, and security tests.
9. [Project: full-stack agentic research agent](https://www.reddit.com/r/learnmachinelearning/comments/1t8clzw/project_built_a_fullstack_agentic_research_agent/) (r/learnmachinelearning, lead) -- example of a public agentic portfolio project: live demo, GitHub, LangGraph, FastAPI, Streamlit, planning, citations, memory, and layered architecture.
10. [Recent experience as interviewer for a DS role](https://www.reddit.com/r/datascience/comments/1klmgnj/my_recent_experience_as_interviewer_for_a_ds_role/) (r/datascience, lead) -- GitHub helps fresh candidates only if projects are non-cookie-cutter and show originality and thought.
11. [GenAI portfolio project ideas that actually matter](https://www.reddit.com/r/learnmachinelearning/comments/1qaexwt/any_genai_portfolio_project_ideas_that_actually/) (r/learnmachinelearning, Grok lead) -- lead from focused Grok search.
12. [Stop building chatbots: GenAI project alternatives](https://www.reddit.com/r/generativeAI/comments/1mprg4d/stop_building_chatbots_these_3_gen_ai_projects/) (r/generativeAI, Grok lead) -- lead from focused Grok search.
13. [Industry-ready data science projects for 2025](https://www.reddit.com/r/Rag/comments/1n2399r/5_industry_ready_data_science_projects_for_2025/) (r/Rag, Grok lead) -- lead from focused Grok search.

## X / Twitter

1. [Lee Robinson on reviewing resumes](https://x.com/leerob/status/2053287286226166254) (May 10, 2026) -- link GitHub, show code/interesting ideas, reflect AI/agents, quality over quantity.
2. [Kanika AI engineer roadmap](https://x.com/KanikaBK/status/2066084670031507726) (Jun 14, 2026) -- portfolio phase: pick 5 ideas, build end-to-end, add memory/agents, push to GitHub.
3. [Akhilesh Mishra DevOps roadmap](https://x.com/livingdevops/status/2063929302585082313) (Jun 8, 2026) -- GitHub README checklist: problem, solution, architecture, run instructions; diagrams help.
4. [Tech With Tim profile-building post](https://x.com/TechWithTimm/status/2069077177682087959) (Jun 22, 2026) -- projects help only when aligned with target role; a few strong relevant projects beat many random ones.
5. [Santiago / svpino on ML interview project](https://x.com/svpino/status/1735647333486821436) (Dec 15, 2023) -- project as "conversational piece": pipeline, evaluation, cloud deploy, simple web app, monitoring/retraining write-up.
6. [Narendran on AI-built portfolios](https://x.com/narenpoy/status/2070111010539888844) (Jun 25, 2026) -- real projects document messy data, failed approaches, business questions, specific numbers, and what did not work.
7. [TechiesVerse ML portfolio project list](https://x.com/TechiesVerse/status/2071400115773100436) (Jun 2026) -- end-to-end, business-relevant projects over generic volume.
8. [Ben Tossell on agent-built shipped projects](https://x.com/bentossell/status/2006352820140749073) (Dec 31, 2025) -- examples of agent-built shipped artifacts: site, social tracker, CLIs, bots, video demo system.
9. [Alvin Sng on agentic coding](https://x.com/alvinsng/status/2006536632586174822) (Jan 1, 2026) -- AI-era work rewards agency; portfolio implication is to show adaptability and shipped work.
10. [Andrew Jiang tiny.cv](https://x.com/andrewjiang/status/2057576042118926810) (May 21, 2026) -- adjacent lead on resume/portfolio packaging and linkable artifacts.

## X / Twitter - AI Engineer Focus

1. [Andrew Ng on AI Engineers](https://x.com/AndrewYNg/status/2061477558693384395) (4 weeks ago) -- AI engineers build apps using LLM prompting, agentic frameworks, evals, and related production practices.
2. [Andrew Ng on evals](https://x.com/AndrewYNg/status/1892258190546653392) (2025) -- evals drive AI system improvements; useful support for making evaluation a core portfolio component.
3. [DataCamp on AI engineer interviews](https://x.com/DataCamp/status/2068635277954859144) (Jun 2026) -- interviews test systems thinking: RAG pipelines, latency tradeoffs, and production debugging.
4. [self.dll on portfolio READMEs](https://x.com/seelffff/status/2054991798519656789) (May 2026) -- README should include architecture diagrams and live demo links.
5. [Rohit Ghumare on evals](https://x.com/ghumare64/status/2062430351021015331) (Jun 2026) -- concrete eval artifacts: golden sets, regression tests, adversarial tests, and LLM-as-judge.
6. [DeRonin on shipping one AI system](https://x.com/DeRonin_/status/2068739716480962849) (Jun 2026) -- ship one useful AI system, learn APIs/RAG/evals, deploy it, and open-source one project.
7. [Jay Krishna on AI engineer projects](https://x.com/jaykrishAGI/status/2069872075976909234) (Grok lead) -- lead from focused Grok search.
8. [Jaydeep Karale on AI project portfolio](https://x.com/_jaydeepkarale/status/2027949447653794215) (Grok lead) -- lead from focused Grok search.
9. [Suraj Sharma on AI portfolio projects](https://x.com/suraj_sharma14/status/2070477175984209980) (Grok lead) -- lead from focused Grok search.
10. [Shalini Goyal on AI projects](https://x.com/goyalshaliniuk/status/1946095090130416007) (Grok lead) -- lead from focused Grok search.
11. [Andrew Bolis on AI engineer portfolio](https://x.com/AndrewBolis/status/1967925221412970935) (Grok lead) -- lead from focused Grok search.
12. [Wen on data/AI portfolio](https://x.com/ds_wen_/status/2071027800727826943) (Grok lead) -- lead from focused Grok search.

## Hacker News

1. [HN thread on data engineering/backend portfolio projects](https://news.ycombinator.com/item?id=11812634) -- end-to-end crawler/ETL/dashboard/query projects as practical evidence.
