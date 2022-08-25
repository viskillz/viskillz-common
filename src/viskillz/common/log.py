from datetime import datetime


class StageLogger:
    """
    A logger specially designed for GLB encoding and decoding processes.
    """

    def __init__(self, expression, indent: int = 0) -> None:
        self._data = dict()
        self._start_time = None
        self._last_id = None
        self._indent = indent
        self._expression = expression

    def start(self, file_name: str) -> None:
        """
        Logs the start of processing the given file.
        :param file_name: the name of the file
        :return: nothing
        """
        actual_id = self._expression(file_name)
        if actual_id == self._last_id:
            return
        if self._last_id is not None:
            delta = (datetime.now() - self._start_time).total_seconds()
            self._data[self._last_id] = delta
            print(f"{delta:8.2f}")
        self._start_time = datetime.now()
        self._last_id = self._expression(file_name)
        print(*(" " * self._indent), "-", self._last_id, end=" ")

    def finish(self) -> dict:
        """
        Logs the end of processing the actual file.
        :return: self
        """
        delta = (datetime.now() - self._start_time).total_seconds()
        self._data[self._last_id] = delta
        print(f"{delta:8.2f}")
        return self._data
