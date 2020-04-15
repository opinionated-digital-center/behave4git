from behave import given
from behave4cli.command_steps import step_a_file_named_filename_with


@given('a file named "{filename}" created from within a step with content "{content}"')
def step_a_file_created_from_within_a_step_with_content(context, filename, content):
    context.surrogate_text = content
    step_a_file_named_filename_with(context, filename)
