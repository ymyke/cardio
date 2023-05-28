from datetime import datetime
import json
from pathlib import Path
from typing import Tuple
from platformdirs import user_data_path
import toml
import cardio
from cardio import Card, Deck, HumanPlayer
from cardio.run import Run

BASE_PATH = user_data_path("cardio")
PLAYER_PATH = BASE_PATH / "player.json"
RUN_PATH = BASE_PATH / "run.json"
META_PATH = BASE_PATH / "meta.json"


def encoder(x):
    if isinstance(x, cardio.skills.SkillSet):
        return [t.__name__ for t in x.get_types()]
    d = x.__dict__
    if "_fc" in d:
        del d["_fc"]
    return d


def decoder(d):
    if "skills" in d:
        d["skills"] = [getattr(cardio.skills, t) for t in d["skills"]]
    for class_ in [HumanPlayer, Deck, Card, Run]:
        try:
            return class_(**d)
        except TypeError:
            pass
    return d


def encode(x) -> str:
    return json.dumps(x, default=encoder, indent=4)


def decode(jsonstr: str) -> Card:
    return json.loads(jsonstr, object_hook=decoder)


def save_file(x, filename: Path):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(encode(x))


def load_file(filename: Path):
    with open(filename, "r", encoding="utf-8") as f:
        return decode(f.read())


def save_all(player: HumanPlayer, run: Run):
    if not BASE_PATH.exists():
        BASE_PATH.mkdir(parents=True)

    meta = {
        "version": toml.load("pyproject.toml")["tool"]["poetry"]["version"],
        "timestamp": datetime.utcnow().strftime("%Y%m%d%H%M%S"),
    }
    save_file(meta, META_PATH)
    save_file(player, PLAYER_PATH)
    save_file(run, RUN_PATH)


def load_all() -> Tuple[HumanPlayer, Run]:
    meta = load_file(META_PATH)
    assert isinstance(meta, dict)
    assert meta["version"] == toml.load("pyproject.toml")["tool"]["poetry"]["version"]
    player = load_file(PLAYER_PATH)
    run = load_file(RUN_PATH)
    assert isinstance(player, HumanPlayer)
    assert isinstance(run, Run)
    return player, run


def reset_all() -> None:
    if BASE_PATH.exists():
        for f in BASE_PATH.iterdir():
            f.unlink()
