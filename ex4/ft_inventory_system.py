import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, quantity = arg.split(":")

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            value = int(quantity)
        except ValueError as v:
            print(f"Quantity error for '{item}': {v}")
            continue
        inventory.update({item: value})

    return inventory


def analyze_inventory(inventory: dict[str, int]) -> None:
    items = list(inventory.keys())
    total = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total}")

    for item in items:
        percent = round(inventory[item] * 100 / total, 1)
        print(f"Item {item} represents {percent}%")

    most = items[0]
    least = items[0]

    for item in items:
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])
    if inventory:
        analyze_inventory(inventory)
    else:
        print("Got inventory: {}")
        print("Item list: []")
        print("Total quantity of the 0 items: 0")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
