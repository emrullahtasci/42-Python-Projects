class Plant:
    def __init__(self, name :str ,height : float = 0.0, age : int = 0 )->None:
        self._name = name
        self._height = height
        self._age = age
        
    def grow(self)->None:
        self._height += 1.5

    def get_height(self)->float:
        return self._height

    def get_age(self)-> int:
        return self._age
    
    def set_height(self,value : float)->None:
        if value < 0:
            print(f"{self._name}: Error height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height update : {value} cm")

    
    def set_age(self,value)->None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age update {value} days")


    def show(self)->None:
        print(f"{self._name}: {round(self._height, 1):>4}cm, {self._age} days old")
if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    # 1. Geçerli başlangıç değerleriyle bir bitki oluşturuyoruz
    plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plant._name}: {plant.get_height()}cm, {plant.get_age()} days old")
    
    # 2. Geçerli (pozitif) güncellemeler yapıyoruz (Setter kapılarını test ediyoruz)
    plant.set_height(25.0)
    plant.set_age(30)
    
    # 3. GEÇERSİZ (Negatif) değerler göndererek güvenlik sistemini test ediyoruz
    # Sistem bunları reddetmeli ve ekrana hata basmalı
    plant.set_height(-5.0)
    plant.set_age(-10)
    
    # 4. En son durumu ekrana basarak verinin bozulmadığını kanıtlıyoruz
    print("Current state:", end=" ")
    plant.show()
