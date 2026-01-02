from pathlib import Path


class StateRepository:
    def __init__(self, path="state.txt"):
        self.path = Path(path)

    def get(self) -> int:
        if not self.path.exists():
            return 0
        content = self.path.read_text().strip()
        return int(content) if content else 0

    def set(self, value: int):
        self.path.write_text(str(value))
