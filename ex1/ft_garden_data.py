class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    nane = Plant("Nane", 15, 1)
    papatya = Plant("Papatya", 14, 1)
    gül = Plant("Gül", 14, 1)

    print("=== Garden Plant Registry ===")
    nane.show()
    papatya.show()
    gül.show()


if __name__ == "__main__":
    main()
