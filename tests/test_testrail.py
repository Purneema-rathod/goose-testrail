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