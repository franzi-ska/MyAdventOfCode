def part_a(input_str: str):
    known_orbits = {'COM': 0}
    orbits = [line.split(')') for line in input_str.splitlines()]

    def count_orbits(planet):
        if planet in known_orbits:
            n_orbit = known_orbits[planet]
        else:
            n_orbit = sum([1 + count_orbits(p0) for p0, p1 in orbits if p1 == planet])
            known_orbits[planet] = n_orbit
        return n_orbit
    planets = set([c for line in input_str.splitlines() for c in line.split(')') ])
    n_orbits = sum([count_orbits(planet) for planet in planets])
    return n_orbits


def part_b(input_str: str):
    orbits = [line.split(')') for line in input_str.splitlines()]
    not_visited_planets = set([c for line in input_str.splitlines() for c in line.split(')') ])

    start_planet = "YOU"
    target_planet = "SAN"

    def get_next_possible_nodes(position):
        options = []
        for orbit in orbits:
            if position in orbit:
                next_planet = orbit[0] if orbit[1] == position else orbit[1]
                if next_planet in not_visited_planets:
                    options.append(next_planet)
                    not_visited_planets.remove(next_planet)
        return options

    not_visited_planets.remove(start_planet)
    this_level = [start_planet]
    count = 0
    while True:
        if target_planet in this_level:
            break
        else:
            count += 1
            next_level = []
            for p in this_level:
                next_level += get_next_possible_nodes(p)
            this_level = next_level

    return count - 2

