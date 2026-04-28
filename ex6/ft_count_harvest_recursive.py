def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def counter(i,days):
        if days < i:
            print("Harvest time!")
            return
        print("Day:",i)
        counter(i + 1,days)
    counter(1,days)
