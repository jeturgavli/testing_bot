import json
import sys
import os

REQUIRED_FIELDS = ["name", "profession", "quote", "github"]

# template values jo skip karne hain
TEMPLATE_VALUES = {
    "name": "Your Name",
    "profession": "Your Profession",
    "quote": "\"Your favourite quote\"</br> - Said By Me",
    "github": "https://github.com"
}

def is_template_entry(card):
    """Check kare ki entry template hai ya nahi"""
    return all(card.get(k) == v for k, v in TEMPLATE_VALUES.items() if k in card)

def validate_json(file_path):
    errors = []

    if not os.path.exists(file_path):
        errors.append(f"❌ File not found: {file_path}")
        return errors

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"❌ JSON Syntax Error: {str(e)}")
        return errors

    if "cardDetails" not in data:
        errors.append("❌ Missing 'cardDetails' key at root level.")
        return errors

    for idx, card in enumerate(data["cardDetails"], start=1):
        # Template entries ko skip karo
        if is_template_entry(card):
            continue

        for field in REQUIRED_FIELDS:
            if field not in card or not str(card[field]).strip():
                errors.append(f"❌ Entry {idx} missing required field: {field}")

    return errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python validator.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    errors = validate_json(file_path)

    if errors:
        print("\n".join(errors))
        sys.exit(1)
    else:
        print("✅ JSON Validation Passed! All required fields are present.")
        sys.exit(0)
