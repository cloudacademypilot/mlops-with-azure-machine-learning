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

### Lint your code
The quality of your code depends on the standards you and your team agree on. To ensure that the agreed upon quality is met, you can run linters that will check whether the code conforms to the standards of the team.

Depending on the code language you use, there are several options to lint your code. For example, if you work with Python, you can use either Flake8 or Pylint.

Use Flake8 to lint your code
To use Flake8 locally with Visual Studio Code:

Install Flake8 with pip install flake8.
Create a configuration file .flake8 and store the file in your repo.
Configure Visual Studio Code to use Flake8 as the linter by going to your settings (Ctrl+,).
Search for flake8.
Enable Python > Linting > Flake8 Enabled.
Set the Flake8 path to the location in your repo where you stored your .flake8 file.

To specify what your team's standards are for code quality, you can configure the Flake8 linter. A common method to define the standards is by creating a .flake8 file that is stored with your code.

The .flake8 file should start with [flake8], followed by any of the configurations you want to use.

For example, if you want to specify that the maximum length of any line can't be more than 80 characters, you'll add the following line to your .flake8 file:

Flake8 has a predefined list of errors it can return. Additionally, you can make use of error codes that are based on the PEP 8 style guide. For example, you can include error codes that refer to proper use of indentation or white spaces.

You can choose to either select (select) a set of error codes that will be part of the linter or select which error codes to ignore (ignore) from the default list of options.

As a result, your .flake8 configuration file may look like the following example:

```
[flake8]
ignore = 
    W504,
    C901,
    E41
max-line-length = 79
exclude = 
    .git,
    .cache,
per-file-ignores =
    code/__init__.py:D104
max-complexity = 10
import-order-style = pep8
```

Lint with GitHub Actions
You can also run the linter automatically with Azure Pipelines or GitHub Actions. The agent provided by either platform will run the linter when you:

Create a configuration file .flake8 and store the file in your repo.
Define the continuous integration pipeline or workflow in YAML.
As a task or step, install Flake8 with python -m pip install flake8.
As a task or step, run the flake8 command to lint your code.

### Unit tests
Where linting verifies how you wrote the code, unit tests check how your code works. Units refer to the code you create. Unit testing is therefore also known as code testing.

As a best practice, your code should exist mostly out of functions. Whether you've created functions to prepare data, or to train a model. You can apply unit testing to, for example:

Check that column names are right.
Check the prediction level of model on new datasets.
Check the distribution of prediction levels.
When you work with Python, you can use Pytest and Numpy (which uses the Pytest framework) to test your code. To learn more about working with Pytest, learn how to write tests with Pytest.

Imagine you created a training script train.py, which contains the following function:

```
# Train the model, return the model
def train_model(data, ridge_args):
    reg_model = Ridge(**ridge_args)
    reg_model.fit(data["train"]["X"], data["train"]["y"])
    return reg_model
```

Assume you stored the training script in the directory src/model/train.py within your repo. To test the train_model function, you must import the function from code.model.train.

You create the test_train.py file in the tests folder. One way to test Python code is to use numpy. Numpy offers several assert functions to compare arrays, strings, objects, or items.

For example, to test the train_model function, you can use a small training dataset and use assert to verify whether the predictions are almost equal to your predefined performance metrics.

To run the test in GitHub Action:

Ensure all necessary libraries are installed to run the training script. Ideally, use a requirements.txt listing all libraries with pip install -r requirements.txt
Install pytest with pip install pytest
Run the tests with pytest tests/
The results of the tests will show in the output of the pipeline or workflow you run.





































[ ⏮️ Previous Module](../3_triggering-github-actions-with-trunk-based-development/documentation.md) - [Next Module ⏭️ ](../5_working-with-environments-in-github-actions/documentation.md)
