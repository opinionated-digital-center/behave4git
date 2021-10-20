Feature: Git steps reused throughout the features

    Scenario: Create a branch
        Given a starting git repo
        And I create the branch "my_branch"
        Then the branch "my_branch" should exist
        And the branch "my_branch" should be at the same level as branch "main"

    Scenario: Switch to a branch
        Given a starting git repo
        And I create the branch "my_branch"
        And I switch to the branch "my_branch"
        Then the head should be at branch "my_branch"

    Scenario: Commit to a branch
        Given a starting git repo
        And I create the branch "my_branch"
        And I switch to the branch "my_branch"
        And a file named "branch_file" with
            """
            foo bar
            """
        And I add the file "branch_file" to the git index
        And I commit the git index with message "chore: branch commit"
        Then there should be 1 commit between head and the branch "main"
        Then there should be 2 commit in "my_branch"
