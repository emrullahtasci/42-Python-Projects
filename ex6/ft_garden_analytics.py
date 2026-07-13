#!/usr/bin/env python3
from typing import Any


class Plant:

    class Analytics:
        def __init__(self) -> None:
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_count} grow, {self.age_count} age, "
                f"{self.show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age = age if age >= 0 else 0
        self.stats = self.Analytics()

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")

    def grow(self) -> None:
        self._height += 0.8
        self.stats.grow_count += 1

    def age(self) -> None:
        self._age += 1
        self.stats.age_count += 1

    def set_height(self, h: float) -> None:
        if h < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = h
            print(f"Height updated: {int(h) if h == int(h) else h}cm")

    def set_age(self, a: int) -> None:
        if a < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = a
            print(f"Age updated: {a} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self.stats.show_count += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
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
        self.shade_count: int = 0

    def produce_shade(self) -> None:
        self.shade_count += 1
        h = self.get_height()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{h:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        # HATA DÜZELTİLDİ: Üst sınıf olan Flower'a 'color' parametresi başarıyla gönderildi.
        super().__init__(name, height, age, color)
        self.seeds_count: int = 0

    def grow(self) -> None:
        self._height += 30.0
        self.stats.grow_count += 1

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


# İstatistikleri ekrana basan sınıflardan bağımsız fonksiyon
def display_plant_stats(plant_obj: Any) -> None:
    plant_obj.stats.display()
    if hasattr(plant_obj, "shade_count"):
        print(f"{plant_obj.shade_count} shade")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_a_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_a_year(400)}"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose._height += 8.0
    rose.stats.grow_count += 1
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower._age += 19
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_stats(sunflower)

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    display_plant_stats(anon)


if __name__ == "__main__":
    main()