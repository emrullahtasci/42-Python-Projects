#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        # Negatif değer kontrolü ile varsayılan atamalar
        self._height = height if height >= 0 else 0.0
        self._age = age if age >= 0 else 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")

    # Önceki egzersizlerden gelen metotlar korunmalı
    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1

    # Güvenli Değiştiriciler (Setters)
    def set_height(self, h: float) -> None:
        if h < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = h
            # is_integer() yerine == int(h) kullanarak çökme riskini önledik
            print(f"Height updated: {int(h) if h == int(h) else h}cm")

    def set_age(self, a: int) -> None:
        if a < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = a
            print(f"Age updated: {a} days")

    # Güvenli Erişimciler (Getters)
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)

    print("Plant created: ", end="")
    plant.show()

    plant.set_height(25.0)
    plant.set_age(30)

    plant.set_height(-5.0)
    plant.set_age(-10)

    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
