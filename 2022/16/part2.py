INF = 9999999

important_valves = {}
valves_dist = {}
my_cache = {}


def distance_between_nodes(node1, node2, graph):
    queue = [(node1, 0)]
    visited = []

    while queue:
        node, dist = queue.pop(0)
        if node in visited:
            continue
        visited.append(node)
        if node == node2:
            return dist
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, dist + 1))

    return INF


from functools import cache


@cache
def max_pressure(start_valve, minutes, pressure, closed_valves, finish=False):
    if (minutes, closed_valves) in my_cache:
        if pressure < my_cache[(minutes, closed_valves)]:
            return 0, ""
    my_cache[(minutes, closed_valves)] = pressure

    if minutes <= 1:
        return (
            (pressure, closed_valves)
            if finish
            else max_pressure("AA", 26, pressure, closed_valves, True)
        )

    return max(
        (
            max_pressure(
                next_valve,
                minutes - distance - 1,
                pressure
                + max(0, (minutes - distance - 1) * important_valves[next_valve]),
                closed_valves.replace("-" + next_valve, ""),
                finish,
            )
            if next_valve in closed_valves
            else (pressure, "")
            for next_valve, distance in valves_dist[start_valve].items()
        ),
        key=lambda x: x[0],
    )


def main():
    valves = {}
    for line in open("input.txt"):
        line = line.replace(",", "").strip().split()
        valve_name = line[1]
        valve_flow = int(line[4].replace("rate=", "").replace(";", ""))
        neighbours = line[9:]
        valves[valve_name] = neighbours
        if valve_flow:
            important_valves[valve_name] = valve_flow

    global valves_dist
    valves_dist = {
        valve: {
            target_valve: distance_between_nodes(valve, target_valve, valves)
            for target_valve in important_valves
            if not target_valve == valve
        }
        for valve in important_valves
    }
    start = "AA"

    valves_dist[start] = {
        target_valve: distance_between_nodes(start, target_valve, valves)
        for target_valve in important_valves
    }

    print(
        max_pressure(
            start, 26, 0, "-" + "-".join(valve for valve in important_valves.keys())
        )
    )


if __name__ == "__main__":
    main()
