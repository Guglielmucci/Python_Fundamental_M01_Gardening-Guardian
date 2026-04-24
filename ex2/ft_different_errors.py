#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    """
    Solleva eccezioni specifiche in base a all'errore
    """
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        _ = "string" + 123
    else:
        return


def test_error_types() -> None:
    """
    Esegue i test richiesti dall'esercizio.
    """
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully")
    except Exception:
        print("Unexpected error!")
    print()
    print("=== Catching multiple error types with one try ===")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
