#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age = age if age >= 0 else 0

    def grow(self) -> None:
        self._height += 1.5

    def age_up(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        # Ortak özellikleri üst sınıfa paslıyoruz
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        h = round(self.get_height(), 1)
        w = round(self.trunk_diameter, 1)
        print(
            f"Tree {self.name} now produces a shade of "
            f"{h}cm long and {w}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow_and_age_simulation(self, days: int) -> None:
        # Örnek çıktıdaki 20 gün büyüme simülasyonunu yapıyor
        for _ in range(days):

            self._height += 2.1
            self.age_up()
            self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    # === Flower Test Bölümü
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    # === Tree Test Bölümü
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    # === Vegetable Test Bölümü
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow_and_age_simulation(20)
    tomato.show()


if __name__ == "__main__":
    main()
