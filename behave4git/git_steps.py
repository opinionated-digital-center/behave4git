from behave import given, then
from behave4cli import command_util
from behave4cli.command_steps import (
    step_a_file_named_filename_with,
    step_a_new_working_directory,
)
from git import InvalidGitRepositoryError, Repo
from hamcrest import assert_that, calling, equal_to, has_item, has_items, not_, raises

from behave4git.utils import files_committed_in_commit


# -----------------------------------------------------------------------------
# STEPS: Git repositories
# -----------------------------------------------------------------------------
@given("an empty git repo")
def step_an_empty_git_repo(context):
    step_a_new_working_directory(context)
    repo = Repo.init(context.workdir)
    command_util.ensure_context_attribute_exists(context, "repo", repo)


@given('an empty git repo with "{initial_branch}" as initial branch')
def step_an_empty_git_repo_with_initial_branch(context, initial_branch):
    step_a_new_working_directory(context)
    repo = Repo.init(context.workdir, initial_branch=initial_branch)
    command_util.ensure_context_attribute_exists(context, "repo", repo)


@given("a starting git repo")
def step_a_starting_git_repo(context):
    step_an_empty_git_repo_with_initial_branch(context, "main")
    context.surrogate_text = "foo bar"
    step_a_file_named_filename_with(context, "initial_commit_file")
    step_add_file_to_index(context, "initial_commit_file")
    step_commit_index_with_message(context, "chore: initial commit")


@given('a starting git repo with "{initial_branch}" as initial branch')
def step_a_starting_git_repo_with_initial_branch(context, initial_branch):
    step_an_empty_git_repo_with_initial_branch(context, initial_branch)
    context.surrogate_text = "foo bar"
    step_a_file_named_filename_with(context, "initial_commit_file")
    step_add_file_to_index(context, "initial_commit_file")
    step_commit_index_with_message(context, "chore: initial commit")


@then("a git repo should exist")
def step_a_git_repo_should_exist(context):
    assert_that(
        calling(Repo).with_args(context.workdir),
        not_(raises(InvalidGitRepositoryError)),
    )


# -----------------------------------------------------------------------------
# STEPS: Commits
# -----------------------------------------------------------------------------
@then("the head commit should contain the files")
def step_current_commit_should_contain_files(context):
    assert context.table is not None and context.table.has_column(
        "path"
    ), "ENSURE: a table with a 'path' column is provided."

    expected = [row["path"] for row in context.table]

    files = files_committed_in_commit(context.repo.head.commit)
    assert_that([item.path for item in files], has_items(*expected))


@then("the head commit message should be")
def step_current_commit_message_should_be(context):
    assert context.text is not None, "ENSURE: multiline text is provided."

    assert_that(context.repo.head.commit.message, equal_to(context.text))


@then("{count:d} files should be committed in the last commit")
def step_x_files_should_be_committed_in_last_commit(context, count):
    assert_that(
        len(files_committed_in_commit(context.repo.head.commit)), equal_to(count)
    )


@then('the file "{filepath}" should be committed in the last commit')
def step_file_should_be_committed_in_last_commit(context, filepath):
    assert_that(files_committed_in_commit(context.repo.head.commit), has_item(filepath))


# -----------------------------------------------------------------------------
# STEPS: Index
# -----------------------------------------------------------------------------
@given('I add the file "{filepath}" to the git index')
@given('I stage the file "{filepath}"')
def step_add_file_to_index(context, filepath):
    context.repo.index.add(filepath)


@given('I commit the git index with message "{message}"')
@given('I commit the staged files with message "{message}"')
def step_commit_index_with_message(context, message):
    context.repo.index.commit(message)


@then('the file "{filepath}" should be in the git index')
@then('the file "{filepath}" should be staged')
def step_file_should_be_staged(context, filepath):
    assert_that(
        [d.a_path for d in context.repo.index.diff("HEAD")],
        has_item(filepath),
    )


@then('the file "{filepath}" should not be in the git index')
@then('the file "{filepath}" should not be staged')
def step_file_should_not_be_staged(context, filepath):
    assert_that(
        [d.a_path for d in context.repo.index.diff("HEAD")],
        not_(has_item(filepath)),
    )


@then('the file "{filepath}" should be in the git index as added')
@then('the file "{filepath}" should be staged as added')
def step_file_should_be_staged_as_added(context, filepath):
    file_should_be_staged_with_change_type(context, filepath, "D")


@then('the file "{filepath}" should be in the git index as deleted')
@then('the file "{filepath}" should be staged as deleted')
def step_file_should_be_staged_as_deleted(context, filepath):
    file_should_be_staged_with_change_type(context, filepath, "A")


@then('the file "{filepath}" should be in the git index as renamed')
@then('the file "{filepath}" should be staged as renamed')
@then('the file "{filepath}" should be in the git index as moved')
@then('the file "{filepath}" should be staged as moved')
def step_file_should_be_staged_as_renamed(context, filepath):
    file_should_be_staged_with_change_type(context, filepath, "R")


@then('the file "{filepath}" should be in the git index as modified')
@then('the file "{filepath}" should be staged as modified')
def step_file_should_be_staged_as_modified(context, filepath):
    file_should_be_staged_with_change_type(context, filepath, "M")


def file_should_be_staged_with_change_type(context, filepath, change_type):
    assert_that(
        [
            d.a_path
            for d in list(context.repo.index.diff("HEAD").iter_change_type(change_type))
        ],
        has_item(filepath),
    )


# -----------------------------------------------------------------------------
# STEPS: Tracked/untracked files
# -----------------------------------------------------------------------------
@then('the file "{filepath}" should be tracked by git')
def step_file_should_be_tracked(context, filepath):
    assert_that(context.repo.untracked_files, not_(has_item(filepath)))


@then('the file "{filepath}" should not be tracked by git')
def step_file_should_not_be_tracked(context, filepath):
    assert_that(context.repo.untracked_files, not_(has_item(filepath)))


# -----------------------------------------------------------------------------
# STEPS: Branches
# -----------------------------------------------------------------------------
@given('I create the branch "{branch}"')
def step_create_branch(context, branch):
    context.repo.create_head(branch)
    assert_that(
        calling((lambda x: context.repo.heads[branch])).with_args(1),
        not_(raises(IndexError)),
    )


@given('I switch to the branch "{branch}"')
def step_switch_to_branch(context, branch):
    context.repo.heads[branch].checkout()


@then('the branch "{branch}" should exist')
def step_branch_should_exist(context, branch):
    refs = [ref.name for ref in context.repo.heads]
    assert_that(refs, has_item(branch), "Branch does not exist")


@then('the head should be at branch "{branch}"')
def step_head_should_be_at_branch(context, branch):
    assert_that(context.repo.head.ref.name, equal_to(branch))


@then('the branch "{branch}" should be at the same level as branch "{base_branch}"')
def step_branch_should_be_at_same_level_as_base_branch(context, branch, base_branch):
    assert_that(
        context.repo.heads[base_branch].commit,
        equal_to(context.repo.heads[branch].commit),
        f"'{branch}' not at same commit as '{base_branch}'",
    )


@then('there should be {count:d} commit between head and the branch "{branch}"')
def step_there_should_be_x_commit_between_head_and_branch(context, count, branch):
    step_branch_should_exist(context, branch)
    assert_that(
        len(list(context.repo.iter_commits(f"HEAD...{branch}"))), equal_to(count)
    )


@then('there should be {count:d} commit in "{branch}"')
def step_there_should_be_x_commit_in_branch(context, count, branch):
    step_branch_should_exist(context, branch)
    assert_that(len(list(context.repo.iter_commits(branch))), equal_to(count))


# @then('there should be {count:d} commit between git head and the branch "{branch}"')
# def step_there_should_be_x_commit_between_head_and_branch(context, count, branch):
#     assert_that(context.repo.head.ref, equal_to(context.repo.heads[branch]))
