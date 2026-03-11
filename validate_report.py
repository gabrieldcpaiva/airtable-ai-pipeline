import json
import sys

def main():
    try:
        with open("testing_report.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: testing_report.json not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: testing_report.json contains invalid JSON")
        sys.exit(1)

if __name__ == "__main__":
    main()
