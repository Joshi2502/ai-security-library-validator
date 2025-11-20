import re

DANGEROUS_OUTPUT_PATTERNS = [
    re.compile(r"rm -rf", re.IGNORECASE),
    re.compile(r"sudo", re.IGNORECASE),
    re.compile(r"ddos", re.IGNORECASE),
    re.compile(r"system\\(.*?\\)", re.IGNORECASE),
    re.compile(r"os\\.system", re.IGNORECASE),
]

PII_PATTERNS = [
    (re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+"), "[REDACTED-EMAIL]"),
    (re.compile(r"\\b\\d{10}\\b"), "[REDACTED-PHONE]"),
    (re.compile(r"\\b\\d{3}-\\d{2}-\\d{4}\\b"), "[REDACTED-SSN]"),
]
