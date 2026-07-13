#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")


def main() -> None:
    print("=== Plant Factory Output ===")


    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)


    print("Created: ", end="")
    plant1.show()

    print("Created: ", end="")
    plant2.show()

    print("Created: ", end="")
    plant3.show()

    print("Created: ", end="")
    plant4.show()

    print("Created: ", end="")
    plant5.show()


if __name__ == "__main__":
    main()