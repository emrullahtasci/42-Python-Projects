class Plant:
    def __init__(self,name = str, height = float, age = int )->None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) ->None:
        self.height += 1.5
    def age(self) -> None:
        self.age += 1
    def show(self) -> None:
        print(f"{self.name:12}:{round(self.height ,1):>5}cm {self.age:>3} days old")
def main():
    prinf("=== Plant Factory Output ===")
    print()
