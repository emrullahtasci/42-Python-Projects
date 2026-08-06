import random


def create_player() -> set[str]:
    game_pool = [
        "Crafting Genius", "Strategist", "World Savior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Hidden Path Finder"
    ]
    picked_count = random.randint(4, 9)
    return set(random.sample(game_pool, picked_count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    p_alice = create_player()
    p_bob = create_player()
    p_charlie = create_player()
    p_dylan = create_player()

    print(f"Player Alice: {p_alice}")
    print(f"Player Bob: {p_bob}")
    print(f"Player Charlie: {p_charlie}")
    print(f"Player Dylan: {p_dylan}")
    print()

    all_unions = set.union(p_alice, p_bob, p_charlie, p_dylan)
    print(f"All distinct achievements: {all_unions}")
    print()

    all_intersects = set.intersection(p_alice, p_bob, p_charlie, p_dylan)
    print(f"Common achievements: {all_intersects}")
    print()

    print(
        "Only Alice has: "
        f"{set.difference(p_alice, p_bob, p_charlie, p_dylan)}"
    )
    print(
        "Only Bob has: "
        f"{set.difference(p_bob, p_alice, p_charlie, p_dylan)}"
    )
    print(
        "Only Charlie has: "
        f"{set.difference(p_charlie, p_alice, p_bob, p_dylan)}"
    )
    print(
        "Only Dylan has: "
        f"{set.difference(p_dylan, p_alice, p_bob, p_charlie)}"
    )
    print()

    full_universe = {
        "Crafting Genius", "Strategist", "World Savior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Hidden Path Finder"
    }

    print(f"Alice is missing: {set.difference(full_universe, p_alice)}")
    print(f"Bob is missing: {set.difference(full_universe, p_bob)}")
    print(f"Charlie is missing: {set.difference(full_universe, p_charlie)}")
    print(f"Dylan is missing: {set.difference(full_universe, p_dylan)}")


if __name__ == "__main__":
    main()
