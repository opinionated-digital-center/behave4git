Feature: Git steps reused throughout the features

    Scenario: Initialise a repo
        Given an empty git repo
        Then a git repo should exist

    Scenario: Stage files
        Given a starting git repo
        And a file named "foo_file" with
            """
            foo bar
            """
        And I add the file "foo_file" to the git index
        Then the file "foo_file" should be staged

    Scenario: Commit files
        Given an empty git repo
        And a file named "initial_commit_file" with
            """
            foo bar
            """
        And I add the file "initial_commit_file" to the git index
        And I commit the git index with message "chore: initial commit"
        Then the head commit message should be
            """
            chore: initial commit
            """
        And 1 files should be committed in the last commit
        And the file "initial_commit_file" should be committed in the last commit

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
