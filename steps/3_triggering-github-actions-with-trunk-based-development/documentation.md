# Triggering GitHub Actions with trunk-based development

**Automation** is one of the most important practices of machine learning operations (MLOps). By automating tasks, you can deploy new models to production more quickly.

Next to automation, another key aspect of MLOps is **source control** to manage code and track any changes. 

Together, you can use automation and source control to trigger tasks in the machine learning workflow based on changes to the code. However, you want the automated task to be triggered only when the code changes have been verified and approved.

For example, after retraining a model using new hyperparameter values, you want to update the hyperparameter in the source code. After verifying and approving the change to the code that is used to train the model, you want to trigger the new model to be trained.

GitHub is a platform that offers GitHub Actions for automation and repositories using Git for source control. You can configure your GitHub Actions workflows to be triggered by a change in your repo.

## What is Trunk-based development ?

Trunk-based development is a version control management practice where developers merge small, frequent updates to a core “trunk” or main branch. Since it streamlines merging and integration phases, it helps achieve CI/CD and increases software delivery and organizational performance.

Developers can create short-lived branches with a few small commits compared to other long-lived feature branching strategies. As codebase complexity and team size grow, trunk-based development helps keep production releases flowing.

To set up trunk-based development, you'll want to:

- Block any direct pushes to the main branch.
- Work with pull requests whenever an update to the code is needed.
- Trigger code quality checks whenever a pull request is created to automatically verify the code.
- Merge a pull request only when changes are approved manually.

## Prerequisites

- Azure Subscription
- Azure Machine Learning workspace and Compute Cluster
- GitHub Account 

## Learning Objectives

- Create a branch protection rule to block direct pushes to main.
- Create a branch to update the code.
- Trigger a GitHub Actions workflow when opening a pull request.









[ ⏮️ Previous Module](../2_triggering-azure-machine-learning-jobs-with-github-actions/documentation.md) - [Next Module ⏭️ ](../4_working-with-linting-and-unit-testing-in-github-actions/documentation.md)
