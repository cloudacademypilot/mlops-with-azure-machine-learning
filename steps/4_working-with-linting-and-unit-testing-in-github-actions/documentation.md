# Working with linting and unit testing in GitHub Actions

You can verify your code used by Azure Machine Learning to train models automatically with GitHub Actions.

Whenever you create your own machine learning models, you're likely to work with scripts to automate machine learning tasks.

You may want the scripts to adhere to your organization's quality standards. By enforcing programmatic or stylistic guidelines for your code, it's easier for data scientists to read each other's scripts.

Before moving code to production, you'll also want to check the performance of the scripts to ensure they work as expected.

Only when you've verified the code quality do you want to use the code in production. You can use GitHub Actions to automatically check the code whenever a pull request is created.

To verify the code used to train the diabetes classification model, you'll want to run:

- Linting: Checking for programmatic or stylistic errors in Python or R scripts.
- Unit testing: Checking for the performance of the contents of the code.

To help the data science team understand the code quality standards, they'll be able to verify their code when developing locally in Visual Studio Code.

However, you want to automate the code verification to check that all code pushed to production has no issues and works as expected. Together with the data science team, you decide to run linting and unit testing whenever a pull request is created by using GitHub Actions workflow.

Let's explore the workflow:

- The production code is hosted in the **main** branch.
- A data scientist creates a **feature branch** for model development.
- The data scientist creates a **pull request** to propose to push changes to the main branch.
- When a pull request is created, a **GitHub Actions workflow** is triggered to verify the code.
- When the code passes **linting** and **unit testing**, the lead data scientist needs to approve the proposed changes.
- After the lead data scientist approves the changes, the pull request is **merged**, and the main branch is updated accordingly.

You'll need to create a GitHub Actions workflow that verifies the code by running a linter and unit tests whenever a pull request is created.

## Prerequisites

- Azure Subscription
- GitHub Account

## Learning objectives

- Run linters and unit tests with GitHub Actions.
- Integrate code checks with pull requests.


## Exercise 1: Run linters and unit tests with GitHub Actions

There are two common types of checks you'll want to do on your code: linters and unit tests.

You can use linters to check whether your code adheres to quality guidelines your organization has set. For example, to lint your code with Flake8, you'll create a .flake8 configuration file, which contains the rules your code has to adhere to.

To check whether the code works as expected, you can create unit tests. To easily test specific parts of your code, your scripts should contain functions. You can test functions in your scripts by creating test files. A popular tool to test Python code is Pytest.







































[ ⏮️ Previous Module](../3_triggering-github-actions-with-trunk-based-development/documentation.md) - [Next Module ⏭️ ](../5_working-with-environments-in-github-actions/documentation.md)
