from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    fire_result, heal_result = combined("Dragon", 20)
    print(f"Combined spell result: "
          f"{fire_result.split(' for')[0]}, "
          f"{heal_result.split(' restores')[0]} Dragon")
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {10 * 3}")
    print()

    print("Testing conditional caster...")
    can_cast = lambda target, power: power >= 15  # noqa: E731
    safe_cast = conditional_caster(can_cast, fireball)
    print(safe_cast("Goblin", 20))
    print(safe_cast("Goblin", 5))
    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for result in sequence("Knight", 15):
        print(result)
    print()

    print("Is fireball callable?", callable(fireball))
    