Feature: Git initialisation steps

    Scenario: Initialise repo with initial branch named "main"
        Given a starting git repo with "main" as initial branch
        Then the branch "main" should exist

    Scenario: Initialise repo with initial branch named "master"
        Given a starting git repo with "master" as initial branch
        Then the branch "master" should exist
