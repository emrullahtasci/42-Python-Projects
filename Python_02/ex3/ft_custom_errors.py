#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, error: str = "Unknown garden error") -> None:
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error: str = "Unknown plant error") -> None:
        super().__init__(error)


class WaterError(GardenError):
    def __init__(self, error: str = "Unknown water error") -> None:
        super().__init__(error)


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
