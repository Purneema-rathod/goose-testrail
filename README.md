# Goose TestRail Extension

This extension provides integration with TestRail for the Goose AI assistant. It allows you to interact with TestRail projects, test cases, test runs, and results directly through Goose.

## Installation

1. Install the extension:
```bash
pip install goose-testrail
```

2. Configure the extension in your Goose configuration:
```yaml
extensions:
  testrail:
    base_url: "https://your-instance.testrail.io"
    username: "your-username"
    api_key: "your-api-key"
```

## Features

The extension provides the following capabilities:

- List TestRail projects
- Get test cases for a project/suite
- Create test runs
- Add test results

## Usage

Once installed and configured, you can use the extension through Goose with commands like:

```python
# Get all projects
projects = testrail.get_projects()

# Get test cases for a project
cases = testrail.get_test_cases(project_id=1, suite_id=2)

# Create a test run
run = testrail.create_test_run(
    project_id=1,
    name="Automated Test Run",
    suite_id=2,
    description="Created via Goose"
)

# Add a test result
result = testrail.add_test_result(
    test_id=100,
    status_id=1,  # 1=Passed
    comment="Test passed successfully"
)
```

## Status IDs

When adding test results, use these status IDs:

- 1 = Passed
- 2 = Blocked
- 3 = Untested
- 4 = Retest
- 5 = Failed

## Development

To contribute to this extension:

1. Clone the repository
2. Install development dependencies:
```bash
pip install -e ".[dev]"
```
3. Run tests:
```bash
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.