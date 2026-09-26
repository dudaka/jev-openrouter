"""Route a support ticket with Jev: one noul, one choice and one score question."""

import json

from jev_openrouter.decisions import decide

TICKET = {
    "customer_tier": "enterprise",
    "ticket": "My checkout page shows a blank screen after I click Pay. I have tried two browsers.",
}

QUESTIONS = {
    "is_bug": {
        "type": "noul",
        "instructions": "Is the customer reporting a software defect?",
    },
    "team": {
        "type": "choice",
        "instructions": "Which team should own `ticket`?",
        "criteria": {
            "payments": "Checkout, billing, or payment processing issues.",
            "frontend": "Rendering, layout, or browser compatibility issues.",
            "account": "Login, permissions, or profile issues.",
        },
    },
    "urgency": {
        "type": "score",
        "instructions": "How urgent is `ticket`?",
        "criteria": [
            "Can wait for the next release",
            "Should be fixed this week",
            "Blocking revenue right now",
        ],
    },
}


def main() -> None:
    """Send the example ticket to Jev and print answers and cost."""
    result = decide(TICKET, QUESTIONS)
    answers = result["answers"]
    print(f"model:   {result['model']}")
    print(f"is_bug:  p={answers['is_bug']['noul']:.2f}")
    print(f"team:    {answers['team']['choice']} (confidence {answers['team']['confidence']:.2f})")
    print(f"urgency: {answers['urgency']['score']:.2f} of 0-2")
    print(f"cost:    ${result['usage']['cost']:.9f} for {result['usage']['input_tokens']} input tokens")
    print(json.dumps(answers, indent=2))
