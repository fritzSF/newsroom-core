import sys
from pathlib import Path

from flask import Config
from pytest import fixture

from newsroom.web.factory import get_app
from tests.conftest import update_config, client, setup  # noqa


root = (Path(__file__).parent / '..').resolve()
sys.path.insert(0, str(root))


@fixture
def app():
    cfg = Config(root)
    # cfg.from_object('newsroom.default_settings')
    update_config(cfg)
    return get_app(config=cfg, testing=True)
