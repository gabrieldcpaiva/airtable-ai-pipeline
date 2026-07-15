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
    else:
        if isinstance(data, list):
            for item in data:
                if "confidence" in item and item["confidence"] not in [1, 2, 3]:
                    print(f"Error: confidence must be an integer between 1 and 3")
                    sys.exit(1)
        elif isinstance(data, dict):
            if "confidence" in data and data["confidence"] not in [1, 2, 3]:
                print(f"Error: confidence must be an integer between 1 and 3")
                sys.exit(1)

if __name__ == "__main__":
    main()
