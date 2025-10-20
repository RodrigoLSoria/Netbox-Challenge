import pytest
from unittest.mock import patch, MagicMock
import scripts.query_sites_api as qs
import requests

mock_sites = {
    "results": [
        {"id": 1, "name": "Site 1", "status": {"value": "active"}},
        {"id": 2, "name": "Site 2", "status": {"value": "active"}},
    ]
}

@patch("scripts.query_sites_api.requests.get")
def test_get_sites_by_status_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_sites
    mock_get.return_value = mock_response

    result = qs.get_sites_by_status("active")
    assert isinstance(result, list)
    assert result[0]["name"] == "Site 1"
    assert result[1]["status"]["value"] == "active"

@patch("scripts.query_sites_api.requests.get")
def test_get_sites_by_status_failure(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Connection error")

    with pytest.raises(SystemExit) as exc_info:
        qs.get_sites_by_status("active")

    assert exc_info.value.code == 1

