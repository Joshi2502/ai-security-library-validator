# AI Security Library Validator

A small, focused Python library for securing AI / LLM workflows.

## Features

- **Prompt validation**
  - Detects **prompt injection / jailbreak** attempts
  - Detects **dangerous intent** (e.g., malware, hacking, exploits)
  - Detects potential **PII** (email, phone, SSN patterns)

- **Output guarding**
  - Flags shell / PowerShell / Python commands that look unsafe
  - Configurable blocking severities

- **PII redaction**
  - Redacts email, phone, SSN from both prompts and outputs

- **Configurable**
  - Central `SecurityConfig` with severity levels
  - Easy to extend the regex rules in `patterns.py`

## Quick Start

```bash
pip install -e .
pytest
