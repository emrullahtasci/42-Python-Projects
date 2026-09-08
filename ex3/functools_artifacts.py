import operator
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any
from collections.abc import Callable

_OPERATIONS = {
    'add': operator.add,
    'multiply': operator.mul,
    'max': max,
    'min': min,
}


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    op = _OPERATIONS.get(operation)
    if op is None:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(op, spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} enchantment of power {power} on " \
           f"{target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire': partial(base_enchantment, 50, 'fire'),
        'ice': partial(base_enchantment, 50, 'ice'),
        'lightning': partial(base_enchantment, 50, 'lightning'),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print()

    print("Testing partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters['fire']("Dragon"))
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")
    print()

    print("Testing spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast([1, 2, 3]))
    print(cast(3.14))
    