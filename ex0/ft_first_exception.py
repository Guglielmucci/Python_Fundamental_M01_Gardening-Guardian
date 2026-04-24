#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """
    Converte una stringa in un intero.
    Solleva ValueError se la conversione fallisce.
    """
    return int(temp_str)


def test_temperature() -> None:
    """
    Esegue i test richiesti dall'esercizio.
    """
    print("=== Garden Temperature ===")
    print()

    data = "25"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()

    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
