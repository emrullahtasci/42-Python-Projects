#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age  # _age kullanarak çakışmayı önledik ve kapsülleme yaptık

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        # :.1f formatı sayesinde her zaman virgülden sonra tek basamak basılır
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30)
    plant1.show()

    start_height = plant1.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.grow()
        plant1.age()
        plant1.show()

    total_increase = plant1.height - start_height
    print(f"Growth this week: {total_increase:.1f}cm")


if __name__ == "__main__":
    main()