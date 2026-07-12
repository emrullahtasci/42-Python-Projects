class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.plant_age} days old"
        )


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
    print(f"Growth this week: {round(total_increase, 1)}cm")


if __name__ == "__main__":
    main()
