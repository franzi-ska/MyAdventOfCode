def fuel_for_mass(mass: int, account_for_own_mass: bool = True):
    fuel_mass = mass // 3 - 2

    if account_for_own_mass and fuel_mass > 0:
        fuel_mass += fuel_for_mass(fuel_mass)

    if fuel_mass < 0:
        fuel_mass = 0

    return fuel_mass


def part_a(input_str: str):
    fuel = 0
    for module_mass in input_str.splitlines():
        fuel += fuel_for_mass(int(module_mass), False)
    return fuel


def part_b(input_str: str):
    fuel = 0
    for module_mass in input_str.splitlines():
        fuel += fuel_for_mass(int(module_mass), True)
    return fuel
