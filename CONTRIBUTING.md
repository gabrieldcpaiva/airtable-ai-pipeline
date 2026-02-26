# Contributing to Airtable AI Pipeline

First off, thanks for taking the time to contribute!

The following is a set of guidelines for contributing to Airtable AI Pipeline. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## I Have a Question

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below.

If you have a general question about the project, please start a discussion or reach out to the maintainers directly.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Describe the exact steps which reproduce the problem** in as much detail as possible.
- **Provide specific examples** to demonstrate the steps.
- **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
- **Explain which behavior you expected to see instead and why.**
- **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion and find related suggestions.

- **Use a clear and descriptive title** for the issue to identify the suggestion.
- **Provide a step-by-step description of the suggested enhancement** in as much detail as possible.
- **Provide specific examples** to demonstrate the steps.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why.

### Pull Requests

The process described here has several goals:

- Maintain the quality of the product.
- Fix problems that are important to users.
- Engage the community in working toward the best possible product.

Please follow these steps to have your contribution considered by the maintainers:

1.  Follow all instructions in the [template](.github/PULL_REQUEST_TEMPLATE.md).
2.  Follow the style guides.
3.  After you submit your pull request, verify that all status checks are passing.

## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the first line to 72 characters or less.
- Reference issues and pull requests liberally after the first line.

### Python Styleguide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).

### JavaScript Styleguide

- Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript).

## Setting Up the Development Environment

1.  Clone the repository.
2.  Copy `.env.example` to `.env` and fill in the required environment variables.
3.  Install dependencies:
    - **Python**: `pip install -r src/python/requirements.txt` (if applicable)
    - **Node.js**: `npm install` inside `src/node/` (if applicable)
4.  Run tests before submitting.
