# Implement a function called parse that expects a str of HTML as input,
# extracts any YouTube URL that’s the value of a src attribute of an iframe
# element therein, and returns its shorter, shareable youtu.be equivalent as a
# str. Expect that any such URL will be in one of the formats below.

# Assume that the value of src will be surrounded by double quotes. And assume
# that the input will contain no more than one such URL. If the input does not
# contain any such URL at all, return None.


import re
from typing import Final


def parse(html_code : str) -> str | None:
    TARGET_URL : Final[str] = r"(?:<iframe)(?:\s+)(?:src=\")(?:https?://)(?:www\.)?(?:youtube\.com/embed/)([^\"/]+)"

    matched_url : re.Match | None = re.search(TARGET_URL, html_code, re.IGNORECASE)

    if matched_url:
        return f"https://youtu.be/{matched_url.group(1)}"

    return None


def main() -> None:
    html_code : str = input("HTML: ").strip()

    print(parse(html_code))


if __name__ == "__main__":
    main()
