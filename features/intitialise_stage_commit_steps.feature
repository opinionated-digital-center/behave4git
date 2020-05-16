Feature: Git steps reused throughout the features

    Scenario: Initialise a repo
        Given an empty git repo
        Then a git repo should exist

    Scenario: Stage files - wording using the "stage" term
        Given a starting git repo
        And a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        Then the file "foo_file" should be staged

    Scenario: Stage files - wording using the "git index" terms
        Given a starting git repo
        And a file named "foo_file" with
            """
            foo bar
            """
        And I add the file "foo_file" to the git index
        Then the file "foo_file" should be in the git index

    Scenario: Commit files - wording using the "stage" term
        Given an empty git repo
        And a file named "foo_file" with
            """
            foo bar
            """
        And I stage the file "foo_file"
        And I commit the staged files with message "foo bar commit message"
        Then the head commit message should be
            """
            foo bar commit message
            """
        And 1 files should be committed in the last commit
        And the file "foo_file" should be committed in the last commit

    Scenario: Commit files - wording using the "git index" terms
        Given an empty git repo
        And a file named "foo_file" with
            """
            foo bar
            """
        And I add the file "foo_file" to the git index
        And I commit the git index with message "foo bar commit message"
        Then the head commit message should be
            """
            foo bar commit message
            """
        And 1 files should be committed in the last commit
        And the file "foo_file" should be committed in the last commit

    Scenario: Create a starting repo step
        Given a starting git repo
        Then a git repo should exist
        And the file named "initial_commit_file" should exist
        And the file "initial_commit_file" should contain
            """
            foo bar
            """
        And the head commit message should be
            """
            chore: initial commit
            """
        And 1 files should be committed in the last commit
        And the file "initial_commit_file" should be committed in the last commit
