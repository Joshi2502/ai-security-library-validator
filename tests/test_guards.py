"""
Tests for OutputGuard.
"""

from ai_security_validator.guards import OutputGuard
from ai_security_validator.config import SecurityConfig



def test_blocks_rm_rf_command() -> None:
    config = SecurityConfig()
    guard = OutputGuard(config)

    output = "To reset the system, run: rm -rf /"
    assert guard.is_safe(output) is False


def test_blocks_additional_blocked_commands() -> None:
    config = SecurityConfig(
        blocked_commands=["format c:", "shutdown -s"]
    )
    guard = OutputGuard(config)

    output = "You could try to format C: using 'format c:'"
    assert guard.is_safe(output) is False


def test_allows_harmless_output() -> None:
    config = SecurityConfig()
    guard = OutputGuard(config)

    output = "You can safely restart the application from the UI."
    assert guard.is_safe(output) is True
