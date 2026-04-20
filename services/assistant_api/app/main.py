from datetime import UTC, datetime
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="offline-assistant-api", version="0.1.0")


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1)
    system: str | None = None


class ReminderRequest(BaseModel):
    title: str = Field(min_length=1)
    due_iso: str = Field(description="ISO8601 datetime string")
    context: dict[str, Any] = Field(default_factory=dict)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "time": datetime.now(UTC).isoformat()}


@app.post("/chat")
async def chat(payload: ChatRequest) -> dict[str, Any]:
    ollama_url = "http://ollama:11434/api/generate"
    body = {
        "model": "qwen2.5:7b-instruct",
        "prompt": payload.prompt,
        "system": payload.system or "You are a concise offline planning assistant.",
        "stream": False,
    }

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(ollama_url, json=body)

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Ollama request failed")

    data = response.json()
    return {
        "answer": data.get("response", ""),
        "model": data.get("model", body["model"]),
        "created_at": data.get("created_at"),
    }


@app.post("/reminders/create")
def create_reminder(payload: ReminderRequest) -> dict[str, Any]:
    return {
        "status": "queued",
        "title": payload.title,
        "due_iso": payload.due_iso,
        "context": payload.context,
    }


@app.get("/briefing/daily")
def daily_briefing() -> dict[str, Any]:
    return {
        "summary": "No persisted reminders yet. Connect DB persistence next.",
        "generated_at": datetime.now(UTC).isoformat(),
    }
