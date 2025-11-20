import re
from .config import SecurityConfig
from .patterns import PII_PATTERNS

class Redactor:
    def __init__(self, config: SecurityConfig):
        self.config = config

    def redact(self, text: str) -> str:
        if not self.config.enable_redaction:
            return text

        for pattern, replacement in PII_PATTERNS:
            text = pattern.sub(replacement, text)

        return text
