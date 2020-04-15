from git import Repo
from hamcrest import assert_that, equal_to

from behave4git.utils import files_committed_in_commit


def test_files_committed_in_commit(tmp_repo: Repo):
    # Given
    # When
    # Then
    files = files_committed_in_commit(tmp_repo.head.commit)
    assert_that(len(files), equal_to(1))
    assert_that(files, equal_to(["foo"]))
