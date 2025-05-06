"""Tests for the TestRail extension."""
from unittest.mock import MagicMock, patch
import pytest
from goose_testrail import TestRailExtension

def test_initialization():
    """Test extension initialization."""
    extension = TestRailExtension()
    assert extension.client is None
    assert extension.base_url is None
    assert extension.username is None
    assert extension.api_key is None

@patch('goose_testrail.TestRailAPI')
def test_initialization_with_config(mock_api):
    """Test extension initialization with configuration."""
    extension = TestRailExtension()
    config = {
        "base_url": "https://example.testrail.io",
        "username": "test_user",
        "api_key": "test_key"
    }
    extension.initialize(config)
    
    assert extension.base_url == config["base_url"]
    assert extension.username == config["username"]
    assert extension.api_key == config["api_key"]
    mock_api.assert_called_once_with(
        base_url=config["base_url"],
        username=config["username"],
        password=config["api_key"]
    )

def test_initialization_missing_config():
    """Test extension initialization with missing configuration."""
    extension = TestRailExtension()
    config = {}
    
    with pytest.raises(ValueError):
        extension.initialize(config)

def test_get_projects():
    """Test getting projects."""
    extension = TestRailExtension()
    extension.client = MagicMock()
    extension.client.projects.get_projects.return_value = {"projects": []}
    
    result = extension.get_projects()
    assert result == {"projects": []}

def test_get_test_runs():
    """Test getting test runs with filters."""
    extension = TestRailExtension()
    extension.client = MagicMock()
    
    # Setup mock return value
    mock_runs = {
        "runs": [
            {"id": 1, "name": "Test Run 1"},
            {"id": 2, "name": "Test Run 2"}
        ]
    }
    extension.client.runs.get_runs.return_value = mock_runs
    
    # Test with various filters
    filters = {
        "project_id": 1,
        "created_after": "2024-01-01",
        "created_before": "2024-12-31",
        "created_by": [123],
        "is_completed": True,
        "limit": 10,
        "offset": 0
    }
    
    result = extension.get_test_runs(**filters)
    
    assert result == mock_runs
    extension.client.runs.get_runs.assert_called_once_with(
        1,
        created_after="2024-01-01",
        created_before="2024-12-31",
        created_by=[123],
        is_completed=1,
        limit=10,
        offset=0
    )

def test_get_test_run():
    """Test getting a specific test run."""
    extension = TestRailExtension()
    extension.client = MagicMock()
    
    mock_run = {"id": 1, "name": "Test Run 1"}
    extension.client.runs.get_run.return_value = mock_run
    
    result = extension.get_test_run(1)
    
    assert result == mock_run
    extension.client.runs.get_run.assert_called_once_with(1)

def test_get_tests_in_run():
    """Test getting tests in a run with status filter."""
    extension = TestRailExtension()
    extension.client = MagicMock()
    
    mock_tests = {
        "tests": [
            {"id": 1, "title": "Test 1", "status_id": 1},
            {"id": 2, "title": "Test 2", "status_id": 5}
        ]
    }
    extension.client.tests.get_tests.return_value = mock_tests
    
    # Test with status filter
    result = extension.get_tests_in_run(1, status_ids=[1, 5])
    
    assert result == mock_tests
    extension.client.tests.get_tests.assert_called_once_with(1, status_id=[1, 5])

def test_close_test_run():
    """Test closing a test run."""
    extension = TestRailExtension()
    extension.client = MagicMock()
    
    mock_run = {"id": 1, "name": "Test Run 1", "is_completed": True}
    extension.client.runs.close_run.return_value = mock_run
    
    result = extension.close_test_run(1)
    
    assert result == mock_run
    extension.client.runs.close_run.assert_called_once_with(1)

def test_get_test_results():
    """Test getting test results with pagination."""
    extension = TestRailExtension()
    extension.client = MagicMock()
    
    mock_results = {
        "results": [
            {"id": 1, "status_id": 1, "comment": "Test passed"},
            {"id": 2, "status_id": 5, "comment": "Test failed"}
        ]
    }
    extension.client.results.get_results.return_value = mock_results
    
    # Test with pagination
    result = extension.get_test_results(1, limit=10, offset=0)
    
    assert result == mock_results
    extension.client.results.get_results.assert_called_once_with(1, limit=10, offset=0)

def test_add_test_result_with_all_fields():
    """Test adding a test result with all optional fields."""
    extension = TestRailExtension()
    extension.client = MagicMock()
    
    mock_result = {
        "id": 1,
        "status_id": 1,
        "comment": "Test passed",
        "version": "1.0",
        "elapsed": "30s",
        "defects": "DEF-1",
        "assignedto_id": 123
    }
    extension.client.results.add_result.return_value = mock_result
    
    result = extension.add_test_result(
        test_id=1,
        status_id=1,
        comment="Test passed",
        version="1.0",
        elapsed="30s",
        defects="DEF-1",
        assignedto_id=123
    )
    
    assert result == mock_result
    extension.client.results.add_result.assert_called_once_with(1, {
        "status_id": 1,
        "comment": "Test passed",
        "version": "1.0",
        "elapsed": "30s",
        "defects": "DEF-1",
        "assignedto_id": 123
    })