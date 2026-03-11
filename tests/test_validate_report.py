import pytest
import json
import sys
from unittest.mock import patch, mock_open
from validate_report import main

def test_main_success():
    """Test main function when testing_report.json is valid."""
    mock_data = {"status": "success"}
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        # Should complete without error
        main()

def test_main_file_not_found():
    """Test main function when testing_report.json is missing."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch("sys.exit") as mock_exit:
            with patch("builtins.print") as mock_print:
                main()
                mock_exit.assert_called_once_with(1)
                mock_print.assert_called_once_with("Error: testing_report.json not found")

def test_main_invalid_json():
    """Test main function when testing_report.json contains invalid JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("sys.exit") as mock_exit:
            with patch("builtins.print") as mock_print:
                main()
                mock_exit.assert_called_once_with(1)
                assert any("invalid JSON" in call.args[0] for call in mock_print.call_args_list)
