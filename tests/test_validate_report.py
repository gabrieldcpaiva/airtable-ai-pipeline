import json
from unittest.mock import patch, mock_open
from validate_report import main

def test_main_success_single_object():
    """Test main function when testing_report.json is a valid single object."""
    mock_data = {"title": "Test Report", "confidence": 2}
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        # Should complete without error
        main()

def test_main_success_list_of_objects():
    """Test main function when testing_report.json is a valid list of objects."""
    mock_data = [
        {"title": "Report 1", "confidence": 1},
        {"title": "Report 2", "confidence": 3}
    ]
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
                assert any("invalid JSON" in str(call) for call in mock_print.call_args_list)

def test_main_missing_required_field():
    """Test main function when an item is missing a required field."""
    mock_data = [{"confidence": 2}] # missing 'title'
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("sys.exit") as mock_exit:
            with patch("builtins.print") as mock_print:
                main()
                mock_exit.assert_called_once_with(1)
                assert any("missing required field 'title'" in str(call) for call in mock_print.call_args_list)

def test_main_invalid_field_type():
    """Test main function when a field has an invalid type."""
    mock_data = {"title": "Test Report", "confidence": "high"} # confidence should be int
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("sys.exit") as mock_exit:
            with patch("builtins.print") as mock_print:
                main()
                mock_exit.assert_called_once_with(1)
                assert any("field 'confidence' must be of type int" in str(call) for call in mock_print.call_args_list)

def test_main_confidence_out_of_range():
    """Test main function when confidence is out of range."""
    mock_data = {"title": "Test Report", "confidence": 5}
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("sys.exit") as mock_exit:
            with patch("builtins.print") as mock_print:
                main()
                mock_exit.assert_called_once_with(1)
                assert any("confidence' must be between 1 and 3" in str(call) for call in mock_print.call_args_list)

def test_main_invalid_root_structure():
    """Test main function when root is not object or list."""
    mock_data = "just a string"
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("sys.exit") as mock_exit:
            with patch("builtins.print") as mock_print:
                main()
                mock_exit.assert_called_once_with(1)
                assert any("must contain an object or a list of objects" in str(call) for call in mock_print.call_args_list)
