"""Optional private Claude drafting service. Never put ANTHROPIC_API_KEY in GitHub Pages."""
import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import httpx

app = FastAPI(title="Tribit Westminster drafting API")
allowed = os.getenv("ALLOWED_ORIGIN", "https://ritwikntrehan.github.io")
app.add_middleware(CORSMiddleware, allow_origins=[allowed], allow_methods=["POST"], allow_headers=["Content-Type"])

class DraftRequest(BaseModel):
    fields: dict = Field(default_factory=dict)
    jurisdiction: str = "Westminster, CA"

@app.post("/api/draft")
async def draft(request: DraftRequest):
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise HTTPException(503, "Claude API key not configured on server")
    if request.jurisdiction != "Westminster, CA":
        raise HTTPException(400, "Unsupported jurisdiction")
    if len(json.dumps(request.fields)) > 40000:
        raise HTTPException(413, "Intake exceeds draft size limit")
    facts = {str(k): str(v.get("value") or "")[:1000] for k, v in request.fields.items() if isinstance(v, dict)}
    prompt = ("Prepare a concise Westminster Development Review PROJECT NARRATIVE draft using ONLY the supplied intake facts. "
              "Do not invent zoning compliance, approvals, studies, legal conclusions, names or site conditions. "
              "Use [MISSING] for facts not supplied. Clearly mark DRAFT / HUMAN REVIEW REQUIRED. "
              "Do not claim to fill or sign official forms. Input JSON:\n" + json.dumps(facts))
    async with httpx.AsyncClient(timeout=60) as client:
        try:
            response = await client.post("https://api.anthropic.com/v1/messages",
                headers={"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                json={"model": os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5"), "max_tokens": 1400,
                      "messages": [{"role": "user", "content": prompt}]})
            response.raise_for_status()
        except httpx.HTTPError:
            raise HTTPException(502, "Claude request failed")
    body = response.json()
    text = "\n".join(part.get("text", "") for part in body.get("content", []) if part.get("type") == "text")
    return {"narrative": text, "human_review_required": True, "approval_prediction": None}
