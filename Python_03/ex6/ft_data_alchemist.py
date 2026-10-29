
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam",
    ]
    print(f"Initial list of players: {initial_players}")

    all_cap: list[str] = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_cap}")

    only_cap: list[str] = [
        name for name in initial_players if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {only_cap}")

    score_dict: dict[str, int] = {
        name: random.randint(10, 1000) for name in all_cap
    }
    print(f"Score dict: {score_dict}")

    avg_score: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(avg_score, 2)}")

    high_scores: dict[str, int] = {
        name: score
        for name, score in score_dict.items()
        if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
