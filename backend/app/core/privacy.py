import re

FORBIDDEN_PATTERNS = [
    re.compile(r"\bpatient\b", re.I),
    re.compile(r"\baadhaar\b", re.I),
    re.compile(r"\bward\s*\d+", re.I),
    re.compile(r"\bhouse\s*no\.?\s*\d+", re.I),
]


def assert_privacy_safe(payload: str) -> None:
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(payload):
            raise ValueError(f"Payload violates privacy guardrails: {pattern.pattern}")