import random


def gen_player_achievements() -> set[str]:
    game_pool: list[str] = [
        "Crafting Genius", "Strategist", "World Savior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Hidden Path Finder"
    ]
    picked_count: int = random.randint(4, 9)
    return set(random.sample(game_pool, picked_count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    p_alice: set[str] = gen_player_achievements()
    p_bob: set[str] = gen_player_achievements()
    p_charlie: set[str] = gen_player_achievements()
    p_dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {p_alice}")
    print(f"Player Bob: {p_bob}")
    print(f"Player Charlie: {p_charlie}")
    print(f"Player Dylan: {p_dylan}")
    print()

    all_unions: set[str] = set.union(p_alice, p_bob, p_charlie, p_dylan)
    print(f"All distinct achievements: {all_unions}")
    print()

    all_intersects: set[str] = set.intersection(
        p_alice, p_bob, p_charlie, p_dylan
    )
    print(f"Common achievements: {all_intersects}")
    print()

    only_alice = set.difference(p_alice, p_bob, p_charlie, p_dylan)
    only_bob = set.difference(p_bob, p_alice, p_charlie, p_dylan)
    only_charlie = set.difference(p_charlie, p_alice, p_bob, p_dylan)
    only_dylan = set.difference(p_dylan, p_alice, p_bob, p_charlie)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()

    full_universe: set[str] = {
        "Crafting Genius", "Strategist", "World Savior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Hidden Path Finder"
    }

    alice_missing = set.difference(full_universe, p_alice)
    bob_missing = set.difference(full_universe, p_bob)
    charlie_missing = set.difference(full_universe, p_charlie)
    dylan_missing = set.difference(full_universe, p_dylan)

    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
