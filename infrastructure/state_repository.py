from pathlib import Path


class StateRepository:
    def __init__(self, path="state.txt"):
        self._path = Path(path)

    def get(self) -> int:
        if not self._path.exists():
            return 0
        content = self._path.read_text().strip()
        return int(content) if content else 0

    def set(self, value: int):
        self._path.write_text(str(value))
