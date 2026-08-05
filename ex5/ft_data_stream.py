import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Sonsuz döngüde rastgele oyuncu ve aksiyon üreten generator."""
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
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
) -> Generator[tuple[str, str], None, None]:
    """Listeden rastgele eleman seçip silen ve kalan listeyi gösteren generator."""
    while len(event_list) > 0:
        index = random.randint(0, len(event_list) - 1)
        event = event_list.pop(index)
        yield event
        print(f"Remains in list: {event_list}")


def main() -> None:
    print("=== Game Data Stream Processor ===")

    # 1. Sonsuz generator'ı başlatıyoruz
    event_stream = gen_event()

    # 2. 1000 defa next() çağırarak eventleri ekrana basıyoruz
    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    # 3. 10 elemanlı bir liste oluşturuyoruz
    ten_events = []
    for _ in range(10):
        ten_events.append(next(event_stream))

    print(f"Built list of 10 events: {ten_events}")

    # 4. consume_event generator'ını for .. in .. ile çalıştırıyoruz
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")


if __name__ == "__main__":
    main()