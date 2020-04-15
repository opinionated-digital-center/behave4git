from pathlib import Path

import pytest
from git import Repo


@pytest.fixture()
def tmp_repo(tmp_path):
    repo = Repo.init(tmp_path)

    file = Path(tmp_path / "foo")
    file.touch()

    repo.index.add([str(file)])
    repo.index.commit("initial commit")

    yield repo
