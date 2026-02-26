import os
import re

def test_config_consistency():
    # Read .env.example
    env_example_path = ".env.example"
    assert os.path.exists(env_example_path), ".env.example not found"

    with open(env_example_path, "r") as f:
        env_content = f.read()

    # Extract keys from .env.example (assuming KEY=VALUE format)
    env_keys = set(re.findall(r'^([A-Z_]+)=', env_content, re.MULTILINE))
    assert len(env_keys) > 0, "No environment variables found in .env.example"

    # Read README.md
    readme_path = "README.md"
    assert os.path.exists(readme_path), "README.md not found"

    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Find the configuration section in README.md
    # Look for a code block following the "Configuration" header
    config_match = re.search(r'## Configuration.*?\n```.*?\.env\n(.*?)\n```', readme_content, re.DOTALL | re.IGNORECASE)
    assert config_match, "Configuration template block not found in README.md"

    readme_config_content = config_match.group(1)
    readme_keys = set(re.findall(r'([A-Z_]+)=', readme_config_content))

    # Check if all keys from .env.example are in README.md
    missing_in_readme = env_keys - readme_keys
    assert not missing_in_readme, f"Environment variables missing in README.md configuration section: {missing_in_readme}"

    # Check if README.md has extra keys not in .env.example
    extra_in_readme = readme_keys - env_keys
    assert not extra_in_readme, f"Extra environment variables in README.md configuration section not found in .env.example: {extra_in_readme}"
