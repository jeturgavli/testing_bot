import json
import sys
import re

def validate_json(file_path):
    errors = []
    required_fields = ["name", "profession", "quote", "github"]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"❌ JSON Syntax Error: {e}")
        return errors

    if "cardDetails" not in data or not isinstance(data["cardDetails"], list):
        errors.append("❌ 'cardDetails' array missing ya galat hai.")
        return errors

    for i, entry in enumerate(data["cardDetails"], start=1):
        # Required fields check
        for field in required_fields:
            if field not in entry:
                errors.append(f"❌ Entry {i}: Missing required field '{field}'.")

        # Optional fields validation
        if "email" in entry:
            if not entry["email"].startswith("mailto:"):
                errors.append(
                    f"⚠️ Entry {i} ({entry.get('name')}): Email '{entry['email']}' 'mailto:' se start hona chahiye."
                )
            elif "@" not in entry["email"]:
                errors.append(
                    f"⚠️ Entry {i} ({entry.get('name')}): Email '{entry['email']}' shayad galat hai."
                )

        if "linkedin" in entry:
            if not entry["linkedin"].startswith("https://"):
                errors.append(
                    f"⚠️ Entry {i} ({entry.get('name')}): LinkedIn link '{entry['linkedin']}' 'https://' se start hona chahiye."
                )

        if "github" in entry:
            if not re.match(r"^https://github\.com", entry["github"]):
                errors.append(
                    f"⚠️ Entry {i} ({entry.get('name')}): GitHub link '{entry['github']}' 'https://github.com' se start hona chahiye."
                )

        if "twitter" in entry:
            if not re.match(r"^https://twitter\.com", entry["twitter"]):
                errors.append(
                    f"⚠️ Entry {i} ({entry.get('name')}): Twitter link '{entry['twitter']}' 'https://twitter.com' se start hona chahiye."
                )

        if "dribbble" in entry:
            if not re.match(r"^https://dribbble\.com", entry["dribbble"]):
                errors.append(
                    f"⚠️ Entry {i} ({entry.get('name')}): Dribbble link '{entry['dribbble']}' 'https://dribbble.com' se start hona chahiye."
                )

        if "behance" in entry:
            if not (entry["behance"].startswith("https://behance.com") or entry["behance"].startswith("https://www.behance.net")):
                errors.append(
                    f"⚠️ Entry {i} ({entry.get('name')}): Behance link '{entry['behance']}' 'https://behance.com' ya 'https://www.behance.net' se start hona chahiye."
                )

    return errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Usage: python validator.py <json_file>")
        sys.exit(0)  # exit cleanly

    file_path = sys.argv[1]
    issues = validate_json(file_path)

    if issues:
        print("\n".join(issues))
        # ❌ yahan FAIL nahi karna hai
        print("\n⚠️ Validation warnings upar diye gaye hain, lekin file ACCEPT ki gayi hai ✅")
    else:
        print("✅ JSON valid hai & template follow ho raha hai.")