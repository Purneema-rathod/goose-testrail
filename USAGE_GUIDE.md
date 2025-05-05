# Using TestRail Extension in Goose - Quick Start Guide

## Overview
The TestRail extension for Goose allows you to:
- Retrieve test run details
- Get failed and blocked test cases
- Export test results to Google Sheets
- Automate test result reporting

## Installation Steps

1. **Open Goose Desktop Application**
   - Launch the Goose application on your computer

2. **Access Extensions Settings**
   - Click on the menu icon (⋮) in the top right corner
   - Select "Settings"
   - Navigate to the "Extensions" tab

3. **Enable TestRail Extension**
   - Search for "TestRail" in the extensions list
   - Click "Enable" next to the TestRail extension

## Configuration

1. **Get Your TestRail Credentials**
   - Your TestRail instance URL (e.g., https://afterpay.testrail.io)
   - Your email address
   - Your TestRail password or API key

2. **Configure the Extension**
   ```yaml
   testrail:
     base_url: https://afterpay.testrail.io
     username: your-email@example.com
     password: your-api-key
   ```

## Usage Examples

### Example 1: Export Failed and Blocked Tests to Google Sheet
```python
# First, get your test run ID from TestRail URL
# Example: https://afterpay.testrail.io/index.php?/runs/view/15644
# Run ID is 15644

# Initialize client
client = TestRailClient(
    base_url='https://afterpay.testrail.io',
    username='your-email@example.com',
    password='your-api-key'
)

# Get failed and blocked tests
results = get_failed_and_blocked(run_id=15644)

# Export to Google Sheet
export_to_spreadsheet(
    run_id=15644,
    spreadsheet_id="your-google-sheet-id"
)
```

### Example 2: Get Test Run Details
```python
# Get test run information
run = get_run(run_id=15644)
print(f"Test Run: {run['name']}")
print(f"Failed Tests: {run['failed_count']}")
print(f"Blocked Tests: {run['blocked_count']}")
```

### Example 3: Analyze Test Results
```python
# Get all tests from a run
tests = get_tests(run_id=15644)

# Get results for a specific test
test_results = get_results_for_test(test_id=tests[0]['id'])
```

## Common Tasks

### Task 1: Export Test Results to SAT Spreadsheet
1. Get your TestRail run ID from the URL
2. Get your Google Sheet ID from the URL
3. Run the following commands:
```python
# In Goose chat, type:
run_id = 15644  # Replace with your run ID
sheet_id = "your-sheet-id"  # Get from Google Sheet URL

results = get_failed_and_blocked(run_id)
export_to_spreadsheet(run_id, sheet_id)
```

### Task 2: Get Test Run Summary
```python
run = get_run(run_id=15644)
print(f"""
Test Run Summary:
----------------
Name: {run['name']}
Total Tests: {run['passed_count'] + run['failed_count'] + run['blocked_count'] + run['untested_count']}
Passed: {run['passed_count']}
Failed: {run['failed_count']}
Blocked: {run['blocked_count']}
Untested: {run['untested_count']}
""")
```

## Troubleshooting

### Common Issues and Solutions

1. **Authentication Error**
   ```
   Error: Authentication failed
   ```
   Solution:
   - Verify your email and API key are correct
   - Check if your API key has expired
   - Ensure you have access to the TestRail instance

2. **Test Run Not Found**
   ```
   Error: Test run with ID XXX not found
   ```
   Solution:
   - Verify the run ID from the TestRail URL
   - Check if you have access to this test run
   - Ensure the test run hasn't been deleted

3. **Google Sheet Access Error**
   ```
   Error: Unable to access Google Sheet
   ```
   Solution:
   - Verify the sheet ID
   - Check if you have edit access to the sheet
   - Ensure the Google Sheets integration is enabled

## Best Practices

1. **Using API Keys**
   - Generate a new API key in TestRail instead of using your password
   - Regularly rotate your API keys
   - Never share your API keys

2. **Exporting Results**
   - Always verify the test run ID before exporting
   - Double-check the Google Sheet ID
   - Review the exported data for accuracy

3. **Error Handling**
   - Keep track of any error messages
   - Report persistent issues to the extension maintainer
   - Document any workarounds you discover

## Getting Help

If you encounter issues:

1. **Check Documentation**
   - Review this guide
   - Check the TestRail API documentation
   - Look for similar issues in the extension repository

2. **Contact Support**
   - Email: purneemarathod@gmail.com
   - Include:
     - Error messages
     - Steps to reproduce
     - TestRail run ID (if applicable)
     - Screenshots if possible

3. **Report Bugs**
   - Create an issue in the extension repository
   - Provide detailed reproduction steps
   - Include your Goose and extension versions

## Updates and Maintenance

- The extension is regularly updated
- Check for new versions in the Goose extension manager
- Review the changelog for new features and fixes

## Security Notes

- Never share your API keys
- Don't store credentials in scripts
- Use environment variables for sensitive data
- Regularly review access logs in TestRail

## Additional Resources

- [TestRail API Documentation](https://support.testrail.com/hc/en-us/articles/7077792415252-Using-TestRail-s-API)
- [Goose Documentation](https://block.github.io/goose/)
- [Extension Repository](https://github.com/YOUR_USERNAME/goose-testrail)
