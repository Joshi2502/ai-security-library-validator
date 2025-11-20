"""
Tests for Redactor.
"""

from ai_security_validator.redaction import Redactor
from ai_security_validator.config import SecurityConfig



def test_redacts_email() -> None:
    config = SecurityConfig()
    redactor = Redactor(config)

    text = "My email is user@example.com"
    redacted = redactor.redact(text)

    assert "user@example.com" not in redacted
    assert config.redact_email_token in redacted


def test_redacts_phone() -> None:
    config = SecurityConfig()
    redactor = Redactor(config)

    text = "Call me at 1234567890"
    redacted = redactor.redact(text)

    assert "1234567890" not in redacted
    assert config.redact_phone_token in redacted


def test_redacts_ssn() -> None:
    config = SecurityConfig()
    redactor = Redactor(config)

    text = "SSN: 123-45-6789"
    redacted = redactor.redact(text)

    assert "123-45-6789" not in redacted
    assert config.redact_ssn_token in redacted
