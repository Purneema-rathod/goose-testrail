# TestRail Extension for Goose

This extension provides integration with TestRail, allowing you to retrieve and analyze test results, and export them to Google Sheets.

## Installation

There are several ways to install this extension:

### 1. From GitHub (Recommended)
```bash
pip install git+https://github.com/YOUR_USERNAME/goose-testrail.git
```

### 2. From Local Directory
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/goose-testrail.git

# Install in development mode
cd goose-testrail
pip install -e .
```

### 3. Manual Installation
1. Download the extension files
2. Copy them to your Goose extensions directory (typically `~/.goose/extensions/testrail`)
3. Enable the extension in Goose settings

## Configuration

The extension requires the following configuration:

```yaml
testrail:
  base_url: https://your-instance.testrail.io
  username: your-email@example.com
  password: your-api-key  # Use an API key instead of password for better security
```

## Available Tools

### get_run

Get details of a test run by ID.

```python
result = get_run(run_id=12345)
```

### get_tests

Get all tests in a test run.

```python
tests = get_tests(run_id=12345)
```

### get_results_for_test

Get test results for a specific test.

```python
results = get_results_for_test(test_id=67890)
```

### get_failed_and_blocked

Get all failed and blocked tests from a test run.

```python
results = get_failed_and_blocked(run_id=12345)
print(f"Failed tests: {len(results['failed'])}")
print(f"Blocked tests: {len(results['blocked'])}")
```

### export_to_spreadsheet

Export test results to a Google Sheet.

```python
result = export_to_spreadsheet(
    run_id=12345,
    spreadsheet_id="your-google-sheet-id"
)
```

## Example Usage

Here's an example of how to use the extension to analyze test results and export them to a spreadsheet:

```python
# Get failed and blocked tests
results = get_failed_and_blocked(run_id=12345)

# Export to Google Sheet
export_to_spreadsheet(
    run_id=12345,
    spreadsheet_id="your-google-sheet-id"
)
```

## Development

To contribute to this extension:

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/goose-testrail.git
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies
```bash
pip install -e .
```

4. Make your changes and test them

5. Submit a pull request

## Troubleshooting

If you encounter any issues:

1. Ensure your TestRail credentials are correct
2. Check that you have the required permissions in TestRail
3. Verify your network connection and TestRail instance accessibility
4. Check the Goose logs for detailed error messages

## Support

For support:
1. Open an issue on GitHub
2. Contact the maintainer at purneemarathod@gmail.com
3. Check the Goose documentation

## License

This extension is part of the Goose project and is licensed under the same terms.