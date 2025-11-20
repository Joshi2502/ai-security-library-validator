from .patterns import DANGEROUS_OUTPUT_PATTERNS
from .config import SecurityConfig

class OutputGuard:
    def __init__(self, config: SecurityConfig):
        self.config = config

    def is_safe(self, text: str) -> bool:
        if not self.config.enable_output_guard:
            return True

        for pattern in DANGEROUS_OUTPUT_PATTERNS:
            if pattern.search(text):
                return False

        return True
    