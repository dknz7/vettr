# Hivemind

AI-powered product research platform that replaces biased review sources with objective, source-cited comparative dashboards. Works for **any product category** — software, appliances, vehicles, consumer goods, services — anything you can spend money on.

## Core Value Proposition

Dozens of sources. One collective intelligence. Hivemind pulls data from across the web — reviews, specs, forums, expert teardowns, pricing databases — and synthesizes it into a single curated, severity-weighted opinion. No single reviewer, influencer, or affiliate gets to control the narrative. The swarm does the research. You make the decision.

## Project Status

**Phase:** Deep planning — no code yet. Validate before building.

## How to Work on This Project

- Prioritize strategy, architecture, and validation over implementation.
- Do not write production code until planning is complete.
- Be direct and honest. Flag bad ideas early.
- Use tables for comparisons. Use concrete numbers over vague estimates.
- When discussing costs, always show per-unit economics (cost per product, cost per report, margin per tier).
- Default to the simplest solution. No over-engineering, no premature abstraction.
- When multiple approaches exist, present max 3 options as a ranked table with tradeoffs.
- Do not suggest NotebookLM as a production component — no API, violates ToS at scale.
- When estimating costs, use pessimistic numbers (higher token counts, no caching) as baseline.

## Founder Context

- Solo technical DevOps engineer learning AI/LLM economics.
- Strong on infra, learning token cost optimization.

## Concept

Users input product names + URLs → system performs deep AI-powered research (40-80 sources per product) → outputs structured, source-cited comparative dashboards.

**Product scope is universal.** Example categories:
- Software & SaaS (project management tools, CRMs, design tools)
- Consumer electronics (laptops, phones, cameras)
- Home appliances (ovens, dishwashers, vacuums)
- Vehicles (cars, motorcycles, e-bikes)
- Everyday goods (cat food, knife sets, mattresses)
- Services (insurance providers, internet plans, gyms)

The research pipeline adapts per category but the artifact structure is consistent.

### 6-Artifact Pipeline Per Product

1. Product evaluation
2. Market ecosystem report
3. Competitive landscape
4. Risk assessment (5-category matrix)
5. Weighted pros & cons (CRITICAL/HIGH/MEDIUM/LOW severity)
6. Pricing breakdown with TCO (1yr + 3yr projections)

### Proven Prototype

- 7 calendar/planning products researched via NotebookLM deep research
- 419 sources, 42 artifacts → glassmorphic HTML comparison dashboard
- Prototype: `C:\Users\dicke\Desktop\Dump Zone\STACK\01-BRAIN\shared\product-research\index.html`
- Prompt template: `C:\Users\dicke\Desktop\Dump Zone\STACK\01-BRAIN\claude-code\prompt-templates\product-research-dashboard-prompt.md`

## Architecture (Proposed)

- **Frontend:** Next.js/React — product input, progress tracker, dashboard renderer, PDF export
- **Backend:** Research orchestrator — Claude API + web search (Tavily/Serper) + scraper (Firecrawl/Jina Reader)
- **Queue:** Bull for async research jobs (2-5 min per report)
- **Storage:** Postgres + S3
- **Auth:** Clerk/Auth0
- **Billing:** Stripe

## Token Economics

### Cost per product researched:

| Component | Cost |
|---|---|
| Web search (Tavily, ~50 searches) | $0.20 |
| Page scraping (Firecrawl, ~50 pages) | $0.15 |
| Source summarization (Haiku) | $0.12 |
| 6 artifact queries (Sonnet, 30K context) | $0.72 |
| **Total per product** | **~$1.20** |

### Cost per report:

- 3-product free tier: ~$3.70 (unoptimized) → ~$0.80-1.20 (optimized)
- 7-product Starter: ~$8.50
- Break-even: ~10-11 Starter ($29/mo) users

### Free tier cost controls:

1. Haiku-only — 60% cost reduction
2. 15 sources/product (not 50) — 50% reduction
3. 3 artifacts only (not 6) — 40% reduction
4. Aggressive caching (30-day TTL) — 80% reduction for repeat products
5. Hard rate limit: 1 report/month
6. Circuit breaker: pause free signups if monthly spend exceeds budget

## Pricing Tiers (Draft)

| | Free | Starter $29/mo | Pro $79/mo | Team $199/mo |
|---|---|---|---|---|
| Products/report | 3 | 7 | 15 | Unlimited |
| Reports/month | 1 | 10 | 30 | Unlimited |
| Sources/product | 15 | 50 | 80 | 80 |
| AI model | Haiku | Sonnet | Sonnet | Sonnet |
| Artifacts | 3 basic | All 6 | All 6 | All 6 |

## Premium Add-ons (High Margin)

| Output | Cost | Charge | Margin |
|---|---|---|---|
| Audio Overview (ElevenLabs TTS) | ~$0.50 | $3-5 | 85-90% |
| Slide Deck (Claude + template) | ~$0.20 | $2-3 | 90% |
| Flashcards (Haiku) | ~$0.05 | $1-2 | 95% |
| Infographic (Claude + image gen) | ~$0.30-0.80 | $3-5 | 75-85% |

## Competitive Positioning

Replaces: G2 (pay-to-play), Capterra/TrustRadius, affiliate blogs, sponsored YouTube, paid influencer reviews.
Differentiator: No pay-to-play rankings, no affiliate bias, source-cited, severity-weighted. Works across ALL product categories, not just software.

## Brand

**Name:** Hivemind
**Domain:** askthehivemind.com (registered via Cloudflare, 1-year validation period)
**Tagline:** The swarm does the research.
**CTA pattern:** "Ask the Hivemind" (buttons, landing page, marketing copy)
**Logo concept:** Abstract hexagonal cell / neural cluster mark. Fits glassmorphic aesthetic — frosted hex shapes with purple/blue gradient glow. Single logomark that works at favicon scale.
**Brand voice:** Collective intelligence. Confident, precise, anti-BS. Not one opinion — every opinion, distilled.
**Design language:** Glassmorphic "Antigravity OS" — dark #08080c background, purple/blue gradients, Inter font, frosted glass panels.
**Naming metaphor:** The hivemind = many sources working as one intelligence. Maps directly to the product mechanic of aggregating 40-80 sources into a single synthesized report.
**Future consideration:** If revenue justifies it, acquire askthehivemind.ai (~$70/yr) as a redirect for brand polish.

**Previous working names:** Vettr (too obscure), ZeroDoubt (too generic). Both retired.

## Open Questions

- Model selection strategy (Haiku vs Sonnet vs Opus per task)
- Source quality filtering (avoiding SEO spam)
- Caching strategy (TTL, invalidation, freshness indicators)
- Legal: scraping + summarizing copyrighted content at scale
- Competitive landscape for the platform itself
- MVP scope definition
- Handling products with very little online presence
- Audio quality vs NotebookLM's conversational podcast style
- Team features scope (shared reports, comments, export permissions)
- White-label / API access for agencies
- Trademark search in class 42 (SaaS) and class 35 (market research) for "Hivemind"

## Next Steps

1. Deep planning session — identify and fill knowledge gaps
2. Competitive landscape research for the platform itself
3. MVP scope definition
4. Landing page for demand validation at askthehivemind.com
5. Trademark search for "Hivemind" in relevant classes
