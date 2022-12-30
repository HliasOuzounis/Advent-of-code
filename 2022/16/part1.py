def most_pressure(start, valves, minutes, pressure, opened_valves, cache):
    if (start, minutes, pressure) in cache:
        return cache[(start, minutes, pressure)]
        
    if minutes <= 1:
        return pressure

    max_pressure = max(
        most_pressure(neighbour, valves, minutes - 1, pressure, opened_valves, cache)
        for neighbour in valves[start][1]
    )
    if start in opened_valves or valves[start][0] == 0:
        cache[(start, minutes, pressure)] = max_pressure
        return max_pressure

    cache[(start, minutes, pressure)] = max(
        max_pressure,
        max(
            most_pressure(
                neighbour,
                valves,
                minutes - 2,
                pressure + valves[start][0] * (minutes - 1),
                opened_valves + [start],
                cache
            )
            for neighbour in valves[start][1]
        ),
    )
    return cache[(start, minutes, pressure)]


def main():
    valves = {}
    for line in open("input.txt"):
        line = line.replace(",", "").strip().split()
        valve_name = line[1]
        valve_flow = int(line[4].replace("rate=", "").replace(";", ""))
        neighbours = line[9:]
        valves[valve_name] = (valve_flow, neighbours)

    print(most_pressure("AA", valves, 30, 0, [], {}))


if __name__ == "__main__":
    main()
