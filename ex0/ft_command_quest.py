import sys

def main() -> None:
    print("===Command Quest==")
    program_name = sys.argv[0]
    print(f"Program name : {program_name}")

    total_arguman = len(sys.argv)
    if total_arguman <= 1:
        print("No arguments provided!")
    else:
        new_argv = total_arguman - 1
        print(f"Arguments received: {new_argv}")

        i = 1
        while i < total_arguman:
            print(f"Argument {i}: {sys.argv[i]}")
            i = i + 1

    print(f"Total arguments: {total_arguman}")

if __name__ == "__main__":
    main()