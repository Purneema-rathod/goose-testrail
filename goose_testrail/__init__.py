"""TestRail extension for Goose."""
from typing import Any, Dict, List, Optional
from goose_mcp import Extension, Tool

class TestRailExtension(Extension):
    """TestRail extension for Goose."""

    def __init__(self) -> None:
        """Initialize the TestRail extension."""
        super().__init__()
        self.client = None
        self.base_url = None
        self.username = None
        self.api_key = None

    def initialize(self, config: Dict[str, Any]) -> None:
        """Initialize the TestRail client with configuration."""
        from testrail_api import TestRailAPI
        
        self.base_url = config.get("base_url")
        self.username = config.get("username")
        self.api_key = config.get("api_key")
        
        if not all([self.base_url, self.username, self.api_key]):
            raise ValueError("TestRail configuration missing required values")
            
        self.client = TestRailAPI(
            base_url=self.base_url,
            username=self.username,
            password=self.api_key
        )

    @Tool()
    def get_projects(self) -> Dict[str, Any]:
        """Get all TestRail projects.
        
        Returns:
            Dict containing list of projects
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
        return self.client.projects.get_projects()

    @Tool()
    def get_test_cases(self, project_id: int, suite_id: Optional[int] = None) -> Dict[str, Any]:
        """Get test cases for a project and optional suite.
        
        Args:
            project_id: ID of the project
            suite_id: Optional ID of the test suite
            
        Returns:
            Dict containing list of test cases
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        if suite_id:
            return self.client.cases.get_cases(project_id, suite_id=suite_id)
        return self.client.cases.get_cases(project_id)

    @Tool()
    def create_test_run(
        self,
        project_id: int,
        name: str,
        suite_id: Optional[int] = None,
        description: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new test run.
        
        Args:
            project_id: ID of the project
            name: Name of the test run
            suite_id: Optional ID of the test suite
            description: Optional description of the test run
            
        Returns:
            Dict containing created test run details
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        data = {
            "name": name,
            "description": description
        }
        if suite_id:
            data["suite_id"] = suite_id
            
        return self.client.runs.add_run(project_id, data)

    @Tool()
    def add_test_result(
        self,
        test_id: int,
        status_id: int,
        comment: Optional[str] = None
    ) -> Dict[str, Any]:
        """Add a result for a test.
        
        Args:
            test_id: ID of the test
            status_id: ID of the test status (1=Passed, 2=Blocked, 3=Untested, 4=Retest, 5=Failed)
            comment: Optional comment about the test result
            
        Returns:
            Dict containing added result details
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        data = {
            "status_id": status_id
        }
        if comment:
            data["comment"] = comment
            
        return self.client.results.add_result(test_id, data)