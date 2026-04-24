#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


def water_plant(plant_name: str) -> None:
    """
    Innaffia la pianta se il nome è scritto con
    la lettera iniziale maiuscola; altrimenti
    genera un errore PlantError.
    """
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
