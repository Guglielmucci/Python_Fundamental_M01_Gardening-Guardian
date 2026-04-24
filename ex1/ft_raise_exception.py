#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """
    Converte una stringa in intero e verifica che la temperatura
    sia compresa tra 0 e 40°C (inclusi).
    Solleva ValueError con messaggi specifici in caso di errore.
    """
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(
             "invalid literal for int() with base 10: "
             f"'{temp_str}'"
            )
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature() -> None:
    """
    Esegue i test richiesti dall'esercizio.
    """
    print("=== Garden Temperature Checker ===")
    print()
    data = "25"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    data = "100"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    data = "-50"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
