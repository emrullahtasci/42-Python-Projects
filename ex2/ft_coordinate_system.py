import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts: list[str] = user_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        valid: bool = True
        coords: list[float] = []
        for part in parts:
            clean_part = part.strip()
            try:
                val: float = float(clean_part)
                coords.append(val)
            except ValueError as e:
                print(f"Error on parameter '{clean_part}': {e}")
                valid = False
                break

        if valid and len(coords) == 3:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_to_center: float = math.sqrt(
        pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2
    )
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between: float = math.sqrt(
        (pos2[0] - pos1[0]) ** 2
        + (pos2[1] - pos1[1]) ** 2
        + (pos2[2] - pos1[2]) ** 2
    )
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
