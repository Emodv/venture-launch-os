from __future__ import annotations

import argparse
import asyncio
import json
import os
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agent import analyze_venture, looks_like_url, merge_analysis, normalized_url
from persistence import load_state, save_state
from state import VentureState

app = FastAPI(title="Venture Launch Agent", version="0.2.0")


class LaunchRequest(BaseModel):
    input: str = Field(min_length=2, description="Plain-English venture idea or an existing business URL")
    mode: Literal["auto", "greenfield", "existing_business"] = "auto"


class ExistingBusinessRequest(BaseModel):
    url: str = Field(min_length=4)


def state_from_request(request: LaunchRequest) -> VentureState:
    mode = request.mode
    if mode == "auto":
        mode = "existing_business" if looks_like_url(request.input) else "greenfield"

    if mode == "existing_business":
        url = normalized_url(request.input)
        return VentureState(
            idea=f"Transform existing business website: {url}",
            entry_mode="existing_business",
            website_url=url,
            status="audit_pending",
        )

    return VentureState(idea=request.input, entry_mode="greenfield", status="discovery")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "vla", "version": "0.2.0"}


@app.post("/ventures")
async def create_venture(request: LaunchRequest) -> dict:
    state = state_from_request(request)
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    return merged.model_dump()


@app.post("/transform")
async def transform_existing_business(request: ExistingBusinessRequest) -> dict:
    url = normalized_url(request.url)
    state = VentureState(
        idea=f"Transform existing business website: {url}",
        entry_mode="existing_business",
        website_url=url,
        status="audit_pending",
    )
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    return merged.model_dump()


@app.get("/ventures/{venture_id}")
def get_venture(venture_id: str) -> dict:
    try:
        state = load_state(venture_id, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="venture not found") from exc
    return state.model_dump()


@app.post("/ventures/{venture_id}/resume")
async def resume_venture(venture_id: str) -> dict:
    try:
        state = load_state(venture_id, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="venture not found") from exc
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    return merged.model_dump()


async def run_cli(value: str, mode: str = "auto") -> None:
    request = LaunchRequest(input=value, mode=mode)
    state = state_from_request(request)
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    path = save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    print(json.dumps({"venture_id": merged.venture_id, "state_path": path, "state": merged.model_dump()}, indent=2))


def cli() -> None:
    parser = argparse.ArgumentParser(description="Venture Launch Agent v0.2")
    parser.add_argument("input", help="Plain-English business idea OR existing business URL")
    parser.add_argument(
        "--mode",
        choices=["auto", "greenfield", "existing_business"],
        default="auto",
        help="Entry mode. Auto treats URL-like inputs as existing businesses.",
    )
    args = parser.parse_args()
    asyncio.run(run_cli(args.input, args.mode))


if __name__ == "__main__":
    if os.getenv("PORT"):
        import uvicorn

        uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ["PORT"]))
    else:
        cli()
