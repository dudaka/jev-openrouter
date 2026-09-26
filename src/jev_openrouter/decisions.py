"""Minimal client for OpenRouter's Decisions API (Jev by TypeSafe)."""

import os

import httpx
from dotenv import load_dotenv

load_dotenv()

DECISIONS_URL = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"


def decide(state: dict | str, questions: dict, model: str = MODEL) -> dict:
    """Ask Jev typed questions about `state` and return the full JSON response."""
    response = httpx.post(
        DECISIONS_URL,
        headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"},
        json={"model": model, "state": state, "questions": questions},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()
