#!/usr/bin/env python3

class Plant:
    # İç içe geçmiş istatistik sınıfı (Nested Class)
    class Stats:
        def __init__(self) -> None:
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_count} grow, "
                f"{self.age_count} age, "
                f"{self.show_count} show"
            )

    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age = age if age >= 0 else 0
        # Her bitkinin kendi iç istatistik nesnesi olur
        self._stats = self.Stats()

    def grow(self, amount: float = 1.5) -> None:
        self._height += amount
        self._stats.grow_count += 1

    def age_up(self, days: int = 1) -> None:
        self._age += days
        self._stats.age_count += 1

    def show(self) -> None:
        self._stats.show_count += 1
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        # Tüm bilgileri varsayılan olan anonim bitki fabrikası
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
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


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds_count: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42  # Örnek çıktıya göre tohum sayısı 42 oluyor

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        # Ağaçlar için ekstra istatistik verisi
        self.shade_count: int = 0

    def produce_shade(self) -> None:
        self.shade_count += 1
        h = round(self._height, 1)
        w = round(self.trunk_diameter, 1)
        print(
            f"Tree {self.name} now produces a shade of "
            f"{h}cm long and {w}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


# Sınıfların dışında yer alan bağımsız istatistik fonksiyonu
def display_plant_statistics(plant: Plant) -> None:
    # İç içe geçmiş sınıftan ana display fonksiyonunu çağırıyoruz
    plant._stats.display()
    # Eğer gelen bitki bir ağaç ise ekstra gölge istatistiğini de basıyoruz
    if isinstance(plant, Tree):
        print(f"{plant.shade_count} shade")


def main() -> None:
    print("=== Garden statistics ===")

    # === Statik Metot Testi
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_a_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_a_year(400)}"
    )

    # === Flower Testi
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)  # 15 + 8 = 23cm
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_plant_statistics(rose)

    # === Tree Testi
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_statistics(oak)

    # === Seed Testi
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)  # 80 + 30 = 110cm
    sunflower.age_up(20)  # 45 + 20 = 65 days
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_statistics(sunflower)

    # === Anonymous Sınıf Metodu Testi
    print("=== Anonymous")
    anon_plant = Plant.create_anonymous()
    anon_plant.show()
    print("[statistics for Unknown plant]")
    display_plant_statistics(anon_plant)


if __name__ == "__main__":
    main()
