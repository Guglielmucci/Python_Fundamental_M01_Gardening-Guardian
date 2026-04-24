#!/usr/bin/env python3

class GardenError(Exception):
    """
    Eccezione di base per gli errori relativi al giardino.
    """
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    """
    Eccezione per i problemi con le piante.
    """
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    """
    Eccezione per problemi di irrigazione.
    """
    def __init__(self, message: str = "Unknown water error") -> None:
        GardenError.__init__(self, message)


def check_plant(plant_name: str, water_amount: int) -> None:
    """
    Genera un'eccezione PlantError se la quantità d'acqua è
    al di fuori dell'intervallo accettabile.
    """
    if water_amount < 20:
        raise PlantError(f"The {plant_name} plant is wilting!")
    if water_amount > 50:
        raise PlantError(f"Cannot water {plant_name}: it would drown!")


def check_water(tank_level: int, water_amount: int) -> None:
    """
    Genera un'eccezione WaterError se non c'è abbastanza
    acqua nel serbatoio.
    """
    if water_amount > tank_level:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        water_amount = int("10")
        check_plant("tomato", water_amount)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        tank_level = int("100")
        water_amount = int("150")
        check_water(tank_level, water_amount)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        water_amount = int("60")
        check_plant("tomato", water_amount)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        tank_level = int("50")
        water_amount = int("60")
        check_water(tank_level, water_amount)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
