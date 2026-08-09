from urllib.parse import urlparse
import re


def check_url(url):
    """Perform basic checks for potentially suspicious URL patterns."""

    warnings = []

    # Add https:// if the user did not provide a scheme
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    if not hostname:
        return ["Invalid URL"]

    # Check HTTPS
    if parsed_url.scheme != "https":
        warnings.append("URL does not use HTTPS.")

    # Check for an IP address instead of a domain name
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.match(ip_pattern, hostname):
        warnings.append("URL uses an IP address instead of a domain name.")

    # Check for suspicious use of @
    if "@" in parsed_url.netloc:
        warnings.append("URL contains '@', which can hide the real destination.")

    # Check for excessive subdomains
    if hostname.count(".") >= 4:
        warnings.append("URL contains many subdomains.")

    # Check for unusually long URLs
    if len(url) > 100:
        warnings.append("URL is unusually long.")

    return warnings


def main():
    print("=== URL Safety Checker ===")

    url = input("Enter a URL: ").strip()

    warnings = check_url(url)

    if not warnings:
        print("\nNo obvious suspicious patterns detected.")
        print("Note: This does not guarantee that the website is safe.")
    else:
        print("\nPotential warning signs:")
        for warning in warnings:
            print(f"- {warning}")

        print("\nBe careful before opening this URL.")


if __name__ == "__main__":
    main()