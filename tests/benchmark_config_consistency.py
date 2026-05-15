import re
import timeit
import os

def benchmark():
    env_example_path = ".env.example"
    readme_path = "README.md"

    if not os.path.exists(env_example_path) or not os.path.exists(readme_path):
        print("Required files not found.")
        return

    with open(env_example_path, "r") as f:
        env_content = f.read()
    with open(readme_path, "r") as f:
        readme_content = f.read()

    def current_logic():
        # Extract keys from .env.example
        env_keys = set(re.findall(r'^([A-Z_]+)=', env_content, re.MULTILINE))

        # Find the configuration section in README.md
        config_match = re.search(r'#+ .*?Configuration.*?\n.*?```.*?\.env\n(.*?)\n\s*```', readme_content, re.DOTALL | re.IGNORECASE)
        if config_match:
            readme_config_content = config_match.group(1)
            readme_keys = set(re.findall(r'([A-Z_]+)=', readme_config_content))
        return env_keys, readme_keys

    # Pre-compiled version (what we will implement)
    ENV_REGEX = re.compile(r'^([A-Z_]+)=', re.MULTILINE)
    CONFIG_SECTION_REGEX = re.compile(r'#+ .*?Configuration.*?\n.*?```.*?\.env\n(.*?)\n\s*```', re.DOTALL | re.IGNORECASE)
    README_KEYS_REGEX = re.compile(r'([A-Z_]+)=')

    def optimized_logic():
        env_keys = set(ENV_REGEX.findall(env_content))
        config_match = CONFIG_SECTION_REGEX.search(readme_content)
        if config_match:
            readme_config_content = config_match.group(1)
            readme_keys = set(README_KEYS_REGEX.findall(readme_config_content))
        return env_keys, readme_keys

    iterations = 100000

    print(f"Running benchmark with {iterations} iterations...")
    current_time = timeit.timeit(current_logic, number=iterations)
    print(f"Current logic time: {current_time:.4f} seconds")

    optimized_time = timeit.timeit(optimized_logic, number=iterations)
    print(f"Optimized logic time: {optimized_time:.4f} seconds")

    improvement = (current_time - optimized_time) / current_time * 100
    print(f"Improvement: {improvement:.2f}%")

if __name__ == "__main__":
    benchmark()
