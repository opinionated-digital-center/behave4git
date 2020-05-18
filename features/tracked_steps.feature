Feature: Git tracked steps

    Background:
        Given a starting git repo

    Scenario: Tracking - new file tracked
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        Then the file "foo_file" should not be tracked by git

    Scenario: Tracking - staged file tracked
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        Then the file "foo_file" should be tracked by git

    Scenario: Tracking - committed file tracked
        Given a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        And I commit the staged files with message "foo bar"
        Then the file "foo_file" should be tracked by git
