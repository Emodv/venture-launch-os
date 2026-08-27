from __future__ import annotations

import argparse
import asyncio
import json
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agent import analyze_venture, merge_analysis
from persistence import load_state, save_state
from state import VentureState

app = FastAPI(title="Venture Launch Agent", version="0.1.0")


class LaunchRequest(BaseModel):
    idea: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "vla", "version": "0.1.0"}


@app.post("/ventures")
async def create_venture(request: LaunchRequest) -> dict:
    state = VentureState(idea=request.idea)
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


async def run_cli(idea: str) -> None:
    state = VentureState(idea=idea)
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    path = save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    print(json.dumps({"venture_id": merged.venture_id, "state_path": path, "state": merged.model_dump()}, indent=2))


def cli() -> None:
    parser = argparse.ArgumentParser(description="Venture Launch Agent v0.1")
    parser.add_argument("idea", help="Plain-English business idea")
    args = parser.parse_args()
    asyncio.run(run_cli(args.idea))


if __name__ == "__main__":
    if os.getenv("PORT"):
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ["PORT"]))
    else:
        cli()
