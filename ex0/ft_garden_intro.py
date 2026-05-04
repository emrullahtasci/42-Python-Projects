class   Herbs:
    def __init__ (self, name: str, height: int, age : int) -> None:
        self.herb_name = name
        self.herb_height = height
        self.herb_age = age


def main() -> None:
    my_herb = Herbs("Nane", 15, 1)
    print(f"Bitki Adı: {my_herb.herb_name}")
    print(f"Bitkinin Boyu: {my_herb.herb_height} cm")
    print(f"Bitkinin Yaşı: {my_herb.herb_age}")


if __name__ == "__main__":
    main()



