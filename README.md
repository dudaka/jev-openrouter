# jev-openrouter

Minimal Python example calling TypeSafe's **Jev** decision model through OpenRouter
(no TypeSafe waitlist needed, only an OpenRouter key).

Repository: <https://github.com/dudaka/jev-openrouter.git>

Jev is not a chat LLM: you send `state` plus typed `questions` and get typed answers with probabilities.

| type     | answer                                             |
|----------|----------------------------------------------------|
| `noul`   | probability the statement is true (0-1)            |
| `choice` | one key from `criteria` + per-option probabilities |
| `score`  | continuous score over ordered `criteria` levels    |

## Run

```bash
git clone https://github.com/dudaka/jev-openrouter.git && cd jev-openrouter
echo "OPENROUTER_API_KEY=sk-or-..." > .env   # git-ignored
uv run jev-openrouter
```

Endpoint: `POST https://openrouter.ai/api/alpha/decisions` (alpha), model `typesafe/jev-1.13`
(or `~typesafe/jev-latest`). Each response reports its price in `usage.cost`.

## Example diagnosis

Ticket (enterprise customer): *"My checkout page shows a blank screen after I click Pay. I have tried two browsers."*

| question  | Jev answer                                            |
|-----------|-------------------------------------------------------|
| `is_bug`  | 0.93 probability it is a software defect              |
| `team`    | `payments` (0.75 vs `frontend` 0.25), confidence 0.63 |
| `urgency` | 1.99 of 0-2: "Blocking revenue right now"             |

Cost: $0.000018564 for 442 input tokens (~0.7 s end to end, model `typesafe/jev-1.13-20260917`).

## Pricing

$0.042 per 1M input tokens, output tokens free (1M requests of this size cost about $19).
