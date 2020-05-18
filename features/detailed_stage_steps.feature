Feature: Git staged steps

    Background:
        Given a starting git repo

    Scenario: Staging - add new file
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        Then the file "foo_file" should be staged
        And the file "foo_file" should be staged as added

    Scenario: Staging - delete committed file
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        And I commit the staged files with message "foo bar"
        When I run "git rm foo_file"
        Then the file "foo_file" should be staged
        And the file "foo_file" should be staged as deleted

    Scenario: Staging - move/rename committed file
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        And I commit the staged files with message "foo bar"
        When I run "git mv foo_file moved_foo_file"
        Then the file "moved_foo_file" should be staged
        And the file "moved_foo_file" should be staged as renamed
        And the file "moved_foo_file" should be staged as moved

    Scenario: Staging - modify committed file
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        And I commit the staged files with message "foo bar"
        And a file named "foo_file" with
            """
            foo bar foo bar
            """
        And I stage the file "foo_file"
        Then the file "foo_file" should be staged
        And the file "foo_file" should be staged as modified

    Scenario: Staging - Committed files are not staged
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        And I commit the staged files with message "foo bar"
        Then the file "foo_file" should not be staged

    Scenario: Staging - new files that have not been added are not staged
        Given a file named "foo_file" with
            """
            foo bar
            """
        Then the file "foo_file" should not be staged
