# Portfolio Research Notes

Raw research for the portfolio section.

This mirrors the interview-question research style: keep source indexes and fetched artifacts separate from final prose. Use these files as evidence when expanding the public `portfolio/` pages.

## Files

- [local-corpus.md](local-corpus.md) - relevant material from this repo and `telegram-writing-assistant`
- [podcast-sources.md](podcast-sources.md) - relevant DataTalks.Club podcast episodes and transcript line references
- [discussion-threads.md](discussion-threads.md) - Reddit, X/Twitter, and Hacker News leads
- [articles.md](articles.md) - blog/article leads
- [all-links.md](all-links.md) - de-duplicated link inventory

## Fetched Artifacts

- [fetched/reddit-posts/](fetched/reddit-posts/) - Reddit posts and comments fetched with `interview/_internal/fetch_reddit.py`
- [fetched/grok-responses/](fetched/grok-responses/) - raw Grok web/X search response JSON

## Reusable Commands

Fetch a Reddit post:

```bash
uv run python interview/_internal/fetch_reddit.py \
  'https://www.reddit.com/r/.../comments/...' \
  portfolio/_internal/fetched/reddit-posts
```

Run a Grok web/X search:

```bash
uv run python interview/_internal/xai_search.py \
  'I am researching portfolio project advice for AI engineers...' \
  --tools web_search,x_search \
  --system 'Research assistant. Prefer first-person and hiring-manager sources. Include URLs.' \
  --label portfolio-projects-public-perspectives
```
