"""
TestRail MCP Extension

This extension provides integration with TestRail, allowing you to:
1. Retrieve test runs and their details
2. Get test results
3. Export results to Google Sheets
"""

import base64
from typing import Dict, Any, List, Optional
import urllib.request
import urllib.error
import json
from datetime import datetime

class TestRailClient:
    """Client for interacting with TestRail API."""
    
    def __init__(self, base_url: str, username: str, password: str):
        """Initialize TestRail client.
        
        Args:
            base_url: TestRail instance URL (e.g., https://your-instance.testrail.io)
            username: TestRail username or email
            password: TestRail password or API key
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password

    def _make_request(self, endpoint: str) -> Dict[str, Any]:
        """Make an authenticated request to TestRail API.
        
        Args:
            endpoint: API endpoint path
            
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/index.php?/api/v2/{endpoint}"
        
        # Create auth string
        auth_string = f"{self.username}:{self.password}"
        auth_b64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        
        headers = {
            'Authorization': f'Basic {auth_b64}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        request = urllib.request.Request(url, headers=headers)
        
        try:
            with urllib.request.urlopen(request) as response:
                return json.loads(response.read().decode('utf-8'))
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            try:
                error_json = json.loads(error_body)
                raise Exception(f"TestRail API error: {error_json.get('error', error_body)}")
            except json.JSONDecodeError:
                raise Exception(f"TestRail API error: {error_body}")
            
        except Exception as e:
            raise Exception(f"Error accessing TestRail API: {str(e)}")

def get_run(run_id: int, config: Dict[str, Any]) -> Dict[str, Any]:
    """Get details of a test run.
    
    Args:
        run_id: ID of the test run to retrieve
        config: Configuration dictionary containing TestRail credentials
        
    Returns:
        Test run details
    """
    client = TestRailClient(
        base_url=config['base_url'],
        username=config['username'],
        password=config['password']
    )
    return client._make_request(f'get_run/{run_id}')

def get_tests(run_id: int, config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Get all tests in a test run.
    
    Args:
        run_id: ID of the test run
        config: Configuration dictionary containing TestRail credentials
        
    Returns:
        List of tests
    """
    client = TestRailClient(
        base_url=config['base_url'],
        username=config['username'],
        password=config['password']
    )
    response = client._make_request(f'get_tests/{run_id}')
    return response.get('tests', [])

def get_results_for_test(test_id: int, config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Get test results for a specific test.
    
    Args:
        test_id: ID of the test
        config: Configuration dictionary containing TestRail credentials
        
    Returns:
        List of test results
    """
    client = TestRailClient(
        base_url=config['base_url'],
        username=config['username'],
        password=config['password']
    )
    response = client._make_request(f'get_results/{test_id}')
    return response.get('results', [])

def get_failed_and_blocked(run_id: int, config: Dict[str, Any]) -> Dict[str, Any]:
    """Get all failed and blocked tests from a test run.
    
    Args:
        run_id: ID of the test run
        config: Configuration dictionary containing TestRail credentials
        
    Returns:
        Dictionary containing lists of failed and blocked tests with their results
    """
    client = TestRailClient(
        base_url=config['base_url'],
        username=config['username'],
        password=config['password']
    )
    
    # Get all tests in the run
    tests = get_tests(run_id, config)
    
    # Filter failed (status_id = 5) and blocked (status_id = 2) tests
    failed_tests = []
    blocked_tests = []
    
    for test in tests:
        if test['status_id'] == 5:  # Failed
            results = get_results_for_test(test['id'], config)
            if results:
                test['latest_result'] = results[0]  # Most recent result
            failed_tests.append(test)
        elif test['status_id'] == 2:  # Blocked
            results = get_results_for_test(test['id'], config)
            if results:
                test['latest_result'] = results[0]  # Most recent result
            blocked_tests.append(test)
    
    return {
        'failed': failed_tests,
        'blocked': blocked_tests
    }

def export_to_spreadsheet(run_id: int, spreadsheet_id: str, config: Dict[str, Any]) -> Dict[str, Any]:
    """Export test results to a Google Sheet.
    
    Args:
        run_id: ID of the test run to export
        spreadsheet_id: ID of the Google Sheet to update
        config: Configuration dictionary containing TestRail credentials
        
    Returns:
        Status of the export operation
    """
    # Get run details
    run = get_run(run_id, config)
    
    # Get failed and blocked tests
    results = get_failed_and_blocked(run_id, config)
    
    # This function would need to be implemented to actually update the Google Sheet
    # For now, return the data that would be exported
    return {
        'run': run,
        'results': results,
        'spreadsheet_id': spreadsheet_id,
        'status': 'Would export these results to the specified Google Sheet'
    }