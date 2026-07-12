#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name
        self.height = height
        self.plant_age = age
        self.water_level: int = 0

    def water(self) -> None:
        self.water_level += 5
        print(f"{self.name} was watered.")

    def needs_water(self) -> bool:
        if self.water_level <= 2:
            return True
        else:
            return False

    def grow(self) -> None:
        if self.water_level == 0:
            print(f"{self.name} needs water to grow!")
        else:
            self.height += 1.5
            self.water_level -= 1

    def age_up(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        rounded_height = round(self.height, 1)
        print(
            f"{self.name:12}:{rounded_height:>5}cm "
            f"{self.plant_age:>3} days old"
        )


def main() -> None:
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 15.0, 2)
    plant2 = Plant("Cactus", 5.2, 10)
    plant3 = Plant("Orchid", 22.5, 5)
    plant4 = Plant("Sunflower", 35.0, 1)
    plant5 = Plant("Bonsai", 12.0, 45)

    plant1.grow()
    plant1.water()
    plant1.grow()
    plant1.age_up()

    plant3.water()
    plant3.grow()

    plant2.water()
    plant2.grow()
    plant2.grow()
    plant2.age_up()

    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()


if __name__ == "__main__":
    main()
