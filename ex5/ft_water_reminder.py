def ft_water_reminder():
    gun = int(input("Days since last watering: "))
    if gun > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
