import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "use",
        "release",
    ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index: int = random.randint(0, len(event_list) - 1)
        event: tuple[str, str] = event_list.pop(index)
        yield event
        print(f"Remains in list: {event_list}")


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream: typing.Generator[
        tuple[str, str], None, None
    ] = gen_event()

    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_stream))

    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")


if __name__ == "__main__":
    main()
