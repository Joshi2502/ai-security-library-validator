from typing import Dict, List
from .patterns import JAILBREAK_PATTERNS, DANGEROUS_PATTERNS, PII_PATTERNS

class PromptValidator:
    """
    Validates LLM prompts for jailbreak attempts, dangerous intent, and PII exposure.
    """

    def validate(self, text: str) -> Dict[str, List[str]]:
        issues = {"jailbreak": [], "dangerous_intent": [], "pii": []}

        for pattern in JAILBREAK_PATTERNS:
            if pattern.search(text):
                issues["jailbreak"].append(pattern.pattern)

        for pattern in DANGEROUS_PATTERNS:
            if pattern.search(text):
                issues["dangerous_intent"].append(pattern.pattern)

        for pattern in PII_PATTERNS:
            if pattern.search(text):
                issues["pii"].append(pattern.pattern)

        return {k: v for k, v in issues.items() if v}
