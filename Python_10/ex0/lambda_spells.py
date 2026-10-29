def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    avg_power = round(
        sum(map(lambda mage: mage['power'], mages)) / len(mages), 2
    )

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power,
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    test_artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
    ]
    sorted_artifacts = artifact_sorter(test_artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} "
        f"power) comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )
    print()

    print("Testing power filter...")
    test_mages = [
        {'name': 'Alex', 'power': 90, 'element': 'fire'},
        {'name': 'Sage', 'power': 40, 'element': 'ice'},
        {'name': 'Nova', 'power': 75, 'element': 'wind'},
    ]
    strong_mages = power_filter(test_mages, 70)
    print(f"Mages with power >= 70: "
          f"{[mage['name'] for mage in strong_mages]}")
    print()

    print("Testing spell transformer...")
    test_spells = ['fireball', 'heal', 'shield']
    print(' '.join(spell_transformer(test_spells)))
    print()

    print("Testing mage stats...")
    print(mage_stats(test_mages))
    