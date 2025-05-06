"""TestRail extension for Goose."""
from typing import Any, Dict, List, Optional, Union
from mcp import Extension, Tool

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
        description: Optional[str] = None,
        include_all: bool = True,
        case_ids: Optional[List[int]] = None,
    ) -> Dict[str, Any]:
        """Create a new test run.
        
        Args:
            project_id: ID of the project
            name: Name of the test run
            suite_id: Optional ID of the test suite
            description: Optional description of the test run
            include_all: Include all test cases (default: True)
            case_ids: Optional list of specific test case IDs to include
            
        Returns:
            Dict containing created test run details
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        data = {
            "name": name,
            "include_all": include_all
        }
        if description:
            data["description"] = description
        if suite_id:
            data["suite_id"] = suite_id
        if case_ids:
            data["case_ids"] = case_ids
            data["include_all"] = False
            
        return self.client.runs.add_run(project_id, data)

    @Tool()
    def get_test_runs(
        self,
        project_id: int,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        created_by: Optional[List[int]] = None,
        is_completed: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get test runs for a project with optional filters.
        
        Args:
            project_id: ID of the project
            created_after: Only return test runs created after this date (format: YYYY-MM-DD)
            created_before: Only return test runs created before this date (format: YYYY-MM-DD)
            created_by: Only return test runs created by these user IDs
            is_completed: If True, only return completed test runs; if False, only return active test runs
            limit: Limit the number of returned test runs
            offset: Skip this many test runs before returning
            
        Returns:
            Dict containing list of test runs
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        filters = {}
        if created_after:
            filters["created_after"] = created_after
        if created_before:
            filters["created_before"] = created_before
        if created_by:
            filters["created_by"] = created_by
        if is_completed is not None:
            filters["is_completed"] = 1 if is_completed else 0
        if limit:
            filters["limit"] = limit
        if offset:
            filters["offset"] = offset
            
        return self.client.runs.get_runs(project_id, **filters)

    @Tool()
    def get_test_run(self, run_id: int) -> Dict[str, Any]:
        """Get a specific test run by ID.
        
        Args:
            run_id: ID of the test run
            
        Returns:
            Dict containing test run details
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        return self.client.runs.get_run(run_id)

    @Tool()
    def get_tests_in_run(
        self,
        run_id: int,
        status_ids: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """Get all tests in a test run.
        
        Args:
            run_id: ID of the test run
            status_ids: Optional list of status IDs to filter by
                       (1=Passed, 2=Blocked, 3=Untested, 4=Retest, 5=Failed)
            
        Returns:
            Dict containing list of tests
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        filters = {}
        if status_ids:
            filters["status_id"] = status_ids
            
        return self.client.tests.get_tests(run_id, **filters)

    @Tool()
    def close_test_run(self, run_id: int) -> Dict[str, Any]:
        """Close a test run.
        
        Args:
            run_id: ID of the test run to close
            
        Returns:
            Dict containing the closed test run details
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        return self.client.runs.close_run(run_id)

    @Tool()
    def add_test_result(
        self,
        test_id: int,
        status_id: int,
        comment: Optional[str] = None,
        version: Optional[str] = None,
        elapsed: Optional[str] = None,
        defects: Optional[str] = None,
        assignedto_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Add a result for a test.
        
        Args:
            test_id: ID of the test
            status_id: ID of the test status (1=Passed, 2=Blocked, 3=Untested, 4=Retest, 5=Failed)
            comment: Optional comment about the test result
            version: Optional version or build tested against
            elapsed: Optional time spent testing (e.g., "30s" or "1m 45s")
            defects: Optional comma-separated list of defects to link to
            assignedto_id: Optional ID of the user to assign this test to
            
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
        if version:
            data["version"] = version
        if elapsed:
            data["elapsed"] = elapsed
        if defects:
            data["defects"] = defects
        if assignedto_id:
            data["assignedto_id"] = assignedto_id
            
        return self.client.results.add_result(test_id, data)

    @Tool()
    def get_test_results(
        self,
        test_id: int,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Dict[str, Any]:
        """Get all results for a test.
        
        Args:
            test_id: ID of the test
            limit: Optional limit on number of results to return
            offset: Optional number of results to skip
            
        Returns:
            Dict containing list of test results
        """
        if not self.client:
            raise RuntimeError("TestRail client not initialized")
            
        filters = {}
        if limit:
            filters["limit"] = limit
        if offset:
            filters["offset"] = offset
            
        return self.client.results.get_results(test_id, **filters)