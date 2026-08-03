import secrets
import string


def generate_password(length: int) -> str:
    """Generate a secure random password."""

    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def main() -> None:
    print("=== Secure Password Generator ===")

    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)

        print("\nGenerated password:")
        print(password)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
    