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

The extension provides comprehensive TestRail integration with the following capabilities:

### Project Management
- List TestRail projects
- Get project details

### Test Case Management
- Get test cases for a project
- Get test cases for a specific suite

### Test Run Management
- Create test runs
- Get test runs with filters
- Get specific test run details
- Get tests within a run
- Close test runs
- Filter test runs by:
  - Creation date range
  - Creator
  - Completion status
  - Pagination (limit/offset)

### Test Results
- Add test results
- Get test results
- Support for:
  - Status updates
  - Comments
  - Version/build information
  - Time tracking
  - Defect linking
  - Test assignments

## Usage Examples

### Working with Projects
```python
# Get all projects
projects = testrail.get_projects()
```

### Working with Test Cases
```python
# Get test cases for a project
cases = testrail.get_test_cases(project_id=1, suite_id=2)
```

### Managing Test Runs
```python
# Create a test run
run = testrail.create_test_run(
    project_id=1,
    name="Automated Test Run",
    suite_id=2,
    description="Created via Goose",
    include_all=True
)

# Get test runs with filters
runs = testrail.get_test_runs(
    project_id=1,
    created_after="2024-01-01",
    created_before="2024-12-31",
    is_completed=False,
    limit=10
)

# Get tests in a run
tests = testrail.get_tests_in_run(
    run_id=100,
    status_ids=[1, 5]  # Get only passed (1) and failed (5) tests
)

# Close a test run
testrail.close_test_run(run_id=100)
```

### Managing Test Results
```python
# Add a test result
result = testrail.add_test_result(
    test_id=100,
    status_id=1,  # 1=Passed
    comment="Test passed successfully",
    version="1.0.0",
    elapsed="2m 30s",
    defects="DEF-123",
    assignedto_id=5
)

# Get test results
results = testrail.get_test_results(
    test_id=100,
    limit=50,
    offset=0
)
```

## Status IDs

When working with test statuses, use these IDs:

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