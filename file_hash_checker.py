import hashlib
import os


def calculate_sha256(file_path: str) -> str:
    """Calculate SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    print("==== File Hash Checker ====\n")

    file_path = input("Enter file path: ").strip()

    if not os.path.isfile(file_path):
        print("\nError: File not found.")
        return

    hash_value = calculate_sha256(file_path)

    print("\nSHA-256 Hash")
    print("-" * 64)
    print(hash_value)


if __name__ == "__main__":
    main()
