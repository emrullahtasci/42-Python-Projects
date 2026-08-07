import sys


def main() -> None:
    print("=== Command Quest ===")
    program_name: str = sys.argv[0]
    print(f"Program name: {program_name}")

    total_arguments: int = len(sys.argv)
    if total_arguments <= 1:
        print("No arguments provided!")
    else:
        new_argv: int = total_arguments - 1
        print(f"Arguments received: {new_argv}")

        i: int = 1
        while i < total_arguments:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {total_arguments}")


if __name__ == "__main__":
    main()
