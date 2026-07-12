#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name

        # Başlangıç yüksekliği doğrulaması
        if height >= 0:
            self._height = height
        else:
            self._height = 0.0
            print(f"{self.name}: Error, height can't be negative")

        # Başlangıç yaşı doğrulaması
        if age >= 0:
            self._age = age
        else:
            self._age = 0
            print(f"{self.name}: Error, age can't be negative")

    def set_height(self, h: float) -> None:
        if h < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = h
            print(f"Height updated: {int(h) if h.is_integer() else h}cm")

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
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    # 1. Bitki oluşturma (Örnek çıktı test adımları)
    plant = Plant("Rose", 15.0, 10)
    print(
        f"Plant created: {plant.name}: "
        f"{round(plant.get_height(), 1)}cm, {plant.get_age()} days old"
    )

    # 2. Geçerli güncellemeler
    plant.set_height(25.0)
    plant.set_age(30)

    # 3. Geçersiz (Negatif) güncellemeler - Hata fırlatmalı
    plant.set_height(-5.0)
    plant.set_age(-10)

    print(
        f"Current state: {plant.name}: "
        f"{round(plant.get_height(), 1)}cm, {plant.get_age()} days old"
    )


if __name__ == "__main__":
    main()
