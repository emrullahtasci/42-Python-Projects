class Plant:
    def __init__(self, name :str ,height : float = 0.0, age : int = 0 )->None:
        self._name = name
        self._height = height
        self._age = age
        
    def grow(self)->None:
        self._height += 1.5


    def age_up(self)->None:
        self._age += 1


    def get_height(self)->float:
        return self._height

 
    
    def show(self)->None:
        print(f"{self._name}: {round(self._height, 1):>4}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, color: str, age: int = 0) -> None:
        super().__init__(name, height, age) # Bu sıra Plant sınıfının sırasıyla aynı kalmalı
        self._color = color
        self._is_bloomed = False

    def bloom(self)->None:
        self._is_bloomed = True
        print(f"{self._name} is blooming beautifully!")

    def show(self)->None:
        super().show()
        print(f"Color : {self._color}")
        if self._is_bloomed:
            print(f"{self._name} is blooming beautifully!")      
        else:
            print(f"{self._name} has not bloomed yet")
    
class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0  # Besin değeri 0'dan başlıyor

    # grow metodunu eziyoruz (Override)
    def grow(self) -> None:
        super().grow()  # Eski grow çalıştı, boyu 1.5 cm arttı.
        self._nutritional_value += 10  # Üzerine ekstra besin değeri ekledik!

    # age_up metodunu eziyoruz
    def age_up(self) -> None:
        super().age_up()  # Yaşı 1 gün arttı.
        self._nutritional_value += 5   # Üzerine besin değeri ekledik!

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")   

if __name__ == "__main__":
    print("=== Flower Test ===")
    gül = Flower("Rose", 15.0, 10, "red")
    gül.show()
    print("[asking the rose to bloom]")
    gül.bloom()
    gül.show()

    print("\n=== Vegetable Test ===")
    domates = Vegetable("Tomato", 5.0, 10, "April")
    domates.show()  # Besin değeri 0 göreceğiz
    print("[make tomato grow and age]")
    domates.grow()
    domates.age_up()
    domates.show()  # Besin değeri artmış olacak!