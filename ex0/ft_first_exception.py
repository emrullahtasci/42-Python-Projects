#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    try:
        val1 = "25"
        print(f"Input data is '{val1}'")
        temp1 = input_temperature(val1)
        print(f"Temperature is now {temp1}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    try:
        val2 = "abc"
        print(f"Input data is '{val2}'")
        temp2 = input_temperature(val2)
        print(f"Temperature is now {temp2}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
