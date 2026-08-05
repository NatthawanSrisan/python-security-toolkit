import re


def check_password_strength(password: str) -> tuple[str, list[str]]:
    """
    Check password strength based on common security rules.

    Returns:
        A strength label and a list of suggestions.
    """
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


def main() -> None:
    password = input("Enter a password to check: ")

    strength, suggestions = check_password_strength(password)

    print(f"\nPassword strength: {strength}")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Your password meets all security requirements.")


if __name__ == "__main__":
    main()