import os

MIN_CHARS: int = 100
MAX_CHARS: int = 1500


class Script:
    script: str

    def __init__(self) -> None:
        # Minimum 100 characters
        script_file = open(
            f"{os.path.dirname(__file__)}/script.txt", "r", encoding="utf-8"
        )
        self.script = script_file.read()

        if MIN_CHARS > len(self.script) < MAX_CHARS:
            raise ValueError(
                f"Invalid script. Script length must be between {MIN_CHARS} and {MAX_CHARS} characters."
            )

        script_file.close()

    def getScript(self) -> str:
        return self.script
