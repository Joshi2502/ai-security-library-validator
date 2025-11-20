class SecurityConfig:
    """
    Holds configuration for guards and redaction.
    """
    def __init__(
        self,
        enable_output_guard: bool = True,
        enable_redaction: bool = True,
    ):
        self.enable_output_guard = enable_output_guard
        self.enable_redaction = enable_redaction
