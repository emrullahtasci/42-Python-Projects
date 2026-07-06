class Plant:
    def __init__(self,name : str, height :float = 0.0, age : int = 0 )->None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) ->None:
        self.height += 1.5
    def age_up(self) -> None:
        self.age += 1
    def show(self) -> None:
        print(f"{self.name:12}:{round(self.height ,1):>5}cm {self.age:>3} days old")

    
    


if __name__ == "__main__":
        print("=== Plant Factory Output ===")
        plant1 = Plant("Rose", 15.0, 2)
        plant2 = Plant("Cactus", 5.2, 10)
        plant3 = Plant("Orchid", 22.5, 5)
        plant4 = Plant("Sunflower", 35.0, 1)
        plant5 = Plant("Bonsai", 12.0, 45)

        plant1.grow()
        plant1.age_up()
        plant3.grow()
        plant2.grow()
        plant2.grow()
        plant2.age_up()
        
        
        plant1.show()
        plant2.show()
        plant3.show()
        plant4.show()
        plant5.show()
       
    

    
