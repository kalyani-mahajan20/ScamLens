import re


def preprocess_text(message: str) -> str:
    """
    Normalize a suspicious message while preserving
    important information such as URLs, numbers and keywords.
    """

    text = message.strip()

    # Normalize repeated whitespace
    text = re.sub(r"\s+", " ", text)

    # Convert to lowercase for consistent signal matching
    text = text.lower()

    return text