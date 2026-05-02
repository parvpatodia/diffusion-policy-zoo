---
name: research
description: Deep technical research — arXiv papers, GitHub repos, benchmarks, SOTA. Returns structured findings, not prose essays.
user_invocable: true
args: source query
---

# research — Technical Research Protocol

## Args
- `arxiv [topic]` → search arXiv, return top 5 with abstracts + key contributions
- `github [keywords]` → find reference implementations
- `sota [benchmark]` → current SOTA on benchmark (Papers With Code)
- `compare [method_a] vs [method_b]` → structured comparison
- `reproduce [paper_id]` → find reproduction notes, gotchas

## Execution

### arXiv search
```
1. Search: arxiv.org/search/?searchtype=all&query=[topic]
2. Filter: last 2 years unless foundational
3. Return per paper: title, arXiv ID, 2-sentence summary, key method, relevance
4. Cite as: // REF: arXiv:XXXX.XXXXX in implementing code
```

### GitHub search
```
1. Filter: >100 stars, active last 6 months
2. Return: name, stars, last commit, what it implements, key files, known issues
```

## Output Format

```
## Research: [query] — [date]

### Papers (arXiv)
1. [arXiv:ID] Title | Authors | Date
   Method: [1-sentence technical insight]
   Relevance: [why it matters for current task]

### Repos
1. owner/repo (⭐N, last commit: Xd ago)
   Implements: [1 sentence]
   Entry: [file] | Core: [file]

### SOTA
Benchmark: [name]
  1. Method: [score]
  2. Method: [score]

### Recommendation
[1 sentence: what to use given current project context]
```

## Anti-patterns
- Don't summarize papers without citing arXiv IDs
- Don't recommend methods without checking working code exists
- Don't spend more than 5K tokens — stop at 5 papers, pick best
