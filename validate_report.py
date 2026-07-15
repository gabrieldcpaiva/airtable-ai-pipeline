import json
import sys

def main():
    try:
        with open("testing_report.json", "r") as f:
            json.load(f)
    except FileNotFoundError:
        print("Error: testing_report.json not found")
        sys.exit(1)
        return
    except json.JSONDecodeError:
        print("Error: testing_report.json contains invalid JSON")
        sys.exit(1)
        return

    if isinstance(data, dict):
        items = [data]
    elif isinstance(data, list):
        items = data
    else:
        print("Error: testing_report.json must contain an object or a list of objects")
        sys.exit(1)
        return

    required_fields = {
        "title": str,
        "confidence": int
    }

    for index, item in enumerate(items):
        if not isinstance(item, dict):
            print(f"Error: item at index {index} is not an object")
            sys.exit(1)
            return

        for field, field_type in required_fields.items():
            if field not in item:
                print(f"Error: item at index {index} is missing required field '{field}'")
                sys.exit(1)
                return

            if not isinstance(item[field], field_type):
                print(f"Error: item at index {index} field '{field}' must be of type {field_type.__name__}")
                sys.exit(1)
                return

        if not (1 <= item["confidence"] <= 3):
            print(f"Error: item at index {index} field 'confidence' must be between 1 and 3")
            sys.exit(1)
            return

if __name__ == "__main__":
    main()
