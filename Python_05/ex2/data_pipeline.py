from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = [
            f'"item_{rank}": "{value}"' for rank, value in data
        ]
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process element in "
                    f"stream: {element}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            items = [
                processor.output()
                for _ in range(min(nb, processor.remaining))
            ]
            plugin.process_output(items)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            print(
                f"{processor.name}: total {processor.total_processed} "
                f"items processed, remaining {processor.remaining} "
                "on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    batch_one = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch_one}")
    stream.process_stream(batch_one)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    batch_two = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {batch_two}")
    stream.process_stream(batch_two)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
