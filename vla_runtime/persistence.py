from __future__ import annotations

import json
from pathlib import Path
from state import VentureState


def save_state(state: VentureState, root: str = "./data/ventures") -> str:
    folder = Path(root)
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / (state.venture_id + ".json")
    state.mark_updated()
    with target.open("w", encoding="utf-8") as handle:
        json.dump(state.model_dump(), handle, indent=2)
    return str(target)


def load_state(venture_id: str, root: str = "./data/ventures") -> VentureState:
    target = Path(root) / (venture_id + ".json")
    with target.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return VentureState.model_validate(data)
