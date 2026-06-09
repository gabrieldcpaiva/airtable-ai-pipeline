import os
import re
import pytest
import unittest.mock

# Pre-compile regular expressions at the module level for performance
ENV_KEYS_REGEX = re.compile(r"^([A-Z_]+)=", re.MULTILINE)
CONFIG_SECTION_REGEX = re.compile(
    r"#+ .*?Configuration.*?\n.*?```.*?\.env\n(.*?)\n\s*```", re.DOTALL | re.IGNORECASE
)
README_KEYS_REGEX = re.compile(r"([A-Z_]+)=")


def test_config_consistency():
    # Read .env.example
    env_example_path = ".env.example"
    assert os.path.exists(env_example_path), ".env.example not found"

    with open(env_example_path, "r") as f:
        env_content = f.read()

    # Extract keys from .env.example (assuming KEY=VALUE format)
    env_keys = set(ENV_KEYS_REGEX.findall(env_content))
    assert len(env_keys) > 0, "No environment variables found in .env.example"

    # Read README.md
    readme_path = "README.md"
    assert os.path.exists(readme_path), "README.md not found"

    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Find the configuration section in README.md
    # Look for a code block containing .env variables after a Configuration header
    config_match = CONFIG_SECTION_REGEX.search(readme_content)
    assert config_match, "Configuration template block not found in README.md"

    readme_config_content = config_match.group(1)
    readme_keys = set(README_KEYS_REGEX.findall(readme_config_content))

    # Check if all keys from .env.example are in README.md
    missing_in_readme = env_keys - readme_keys
    assert not missing_in_readme, (
        f"Environment variables missing in README.md configuration section: {missing_in_readme}"
    )

    # Check if README.md has extra keys not in .env.example
    extra_in_readme = readme_keys - env_keys
    assert not extra_in_readme, (
        f"Extra environment variables in README.md configuration section not found in .env.example: {extra_in_readme}"
    )


def test_env_extraction_variations(tmp_path, monkeypatch):
    """Test extracting environment variables from various .env.example formats."""
    # Change working directory to a temporary path
    monkeypatch.chdir(tmp_path)

    # Create a dummy README.md to satisfy the test
    readme_content = """
    ## Configuration
    ```.env
    VALID_KEY=value
    KEY_WITH_COMMENT=value
    KEY_NO_VALUE=
    ```
    """
    (tmp_path / "README.md").write_text(readme_content)

    # Create .env.example with variations
    env_content = """VALID_KEY=value
# COMMENTED_KEY=value
KEY_WITH_COMMENT=value # inline comment
KEY_NO_VALUE=
invalid_key=value
"""
    (tmp_path / ".env.example").write_text(env_content)

    # Run the consistency test, which will extract and validate keys
    test_config_consistency()

    # Verify the extracted keys (should match the dummy README.md)
    # The actual extraction test is implicit in test_config_consistency passing,
    # but we can also explicitly test the regex here to be sure.
    extracted_keys = set(ENV_KEYS_REGEX.findall(env_content))
    assert extracted_keys == {"VALID_KEY", "KEY_WITH_COMMENT", "KEY_NO_VALUE"}


def test_empty_env_example(tmp_path, monkeypatch):
    """Test that an empty .env.example raises an assertion error."""
    monkeypatch.chdir(tmp_path)

    (tmp_path / "README.md").write_text("dummy")
    (tmp_path / ".env.example").write_text("\n\n")

    with pytest.raises(
        AssertionError, match="No environment variables found in .env.example"
    ):
        test_config_consistency()


def test_missing_env_example():
    """Test when .env.example file is missing."""

    def mock_exists(path):
        return path != ".env.example"

    with unittest.mock.patch("os.path.exists", side_effect=mock_exists):
        with pytest.raises(AssertionError, match=r"\.env\.example not found"):
            test_config_consistency()


def test_missing_readme():
    """Test when README.md file is missing."""

    def mock_exists(path):
        return path != "README.md"

    with unittest.mock.patch("os.path.exists", side_effect=mock_exists):
        with unittest.mock.patch(
            "builtins.open", unittest.mock.mock_open(read_data="KEY=value\n")
        ):
            with pytest.raises(AssertionError, match=r"README\.md not found"):
                test_config_consistency()


def test_missing_in_readme(tmp_path, monkeypatch):
    """Test when a key is in .env.example but missing in README.md."""
    monkeypatch.chdir(tmp_path)

    env_content = "KEY_A=value1\nKEY_B=value2\n"
    (tmp_path / ".env.example").write_text(env_content)

    readme_content = "## Configuration\n```.env\nKEY_A=value1\n```\n"
    (tmp_path / "README.md").write_text(readme_content)

    with pytest.raises(
        AssertionError,
        match=r"Environment variables missing in README\.md configuration section: \{'KEY_B'\}",
    ):
        test_config_consistency()


def test_extra_in_readme(tmp_path, monkeypatch):
    """Test when a key is in README.md but missing in .env.example."""
    monkeypatch.chdir(tmp_path)

    env_content = "KEY_A=value1\n"
    (tmp_path / ".env.example").write_text(env_content)

    readme_content = "## Configuration\n```.env\nKEY_A=value1\nKEY_C=value3\n```\n"
    (tmp_path / "README.md").write_text(readme_content)

    with pytest.raises(
        AssertionError,
        match=r"Extra environment variables in README\.md configuration section not found in \.env\.example: \{'KEY_C'\}",
    ):
        test_config_consistency()
