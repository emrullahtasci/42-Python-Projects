def ft_plant_age():
    senaryo1 =int(input("Enter plant age in days: "))

    if senaryo1 > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")