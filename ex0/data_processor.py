from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    name: str = "Data Processor"

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)

    def _store(self, values: list[str]) -> None:
        for value in values:
            self._storage.append((self._total, value))
            self._total += 1

    @property
    def total_processed(self) -> int:
        return self._total

    @property
    def remaining(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data:
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self._store([str(item) for item in data])
        else:
            self._store([str(data)])


class TextProcessor(DataProcessor):
    name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self._store(list(data))
        else:
            self._store([data])


class LogProcessor(DataProcessor):
    name = "Log Processor"

    @staticmethod
    def _is_log_entry(data: Any) -> bool:
        return (
            isinstance(data, dict)
            and bool(data)
            and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        )

    def validate(self, data: Any) -> bool:
        if self._is_log_entry(data):
            return True
        if isinstance(data, list) and data:
            return all(self._is_log_entry(item) for item in data)
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        entries = data if isinstance(data, list) else [data]
        formatted = [
            f"{entry['log_level']}: {entry['log_message']}"
            for entry in entries
        ]
        self._store(formatted)


def _test_numeric_processor() -> None:
    print("Testing Numeric Processor...")
    processor = NumericProcessor()

    print(f"Trying to validate input '42': {processor.validate(42)}")
    print(f"Trying to validate input 'Hello': "
          f"{processor.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without "
          "prior validation:")
    try:
        processor.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")

    data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    processor.ingest(data)
    print("Extracting 3 values...")
    for i in range(3):
        _, value = processor.output()
        print(f"Numeric value {i}: {value}")


def _test_text_processor() -> None:
    print("Testing Text Processor...")
    processor = TextProcessor()

    print(f"Trying to validate input '42': {processor.validate(42)}")

    data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {data}")
    processor.ingest(data)
    print("Extracting 1 value...")
    _, value = processor.output()
    print(f"Text value 0: {value}")


def _test_log_processor() -> None:
    print("Testing Log Processor...")
    processor = LogProcessor()

    print(f"Trying to validate input 'Hello': "
          f"{processor.validate('Hello')}")

    data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {data}")
    processor.ingest(data)
    print("Extracting 2 values...")
    for i in range(2):
        _, value = processor.output()
        print(f"Log entry {i}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    _test_numeric_processor()
    print()
    _test_text_processor()
    print()
    _test_log_processor()


if __name__ == "__main__":
    main()
