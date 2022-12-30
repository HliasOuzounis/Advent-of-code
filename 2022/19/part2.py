from math import ceil

def mine(
    minutes,
    ore_cost,
    clay_cost,
    obs_cost,
    geode_cost,
    ore_robots,
    clay_robots,
    obs_robots,
    geode_robots,
    ore,
    clay,
    obs,
    geodes,
):
    if minutes == 0:
        return geodes

    if ore_robots > max(ore_cost, clay_cost, obs_cost[0], geode_cost[0]):
        return 0
    if clay_robots > obs_cost[1]:
        return 0
    if obs_robots > geode_cost[1]:
        return 0

    max_geodes = 0

    if ore_robots:
        mins = max(0, ceil((ore_cost - ore) / ore_robots)) + 1

        if not mins > minutes:
            max_geodes = max(
                max_geodes,
                mine(
                    int(minutes - mins),
                    ore_cost,
                    clay_cost,
                    obs_cost,
                    geode_cost,
                    ore_robots + 1,
                    clay_robots,
                    obs_robots,
                    geode_robots,
                    ore - ore_cost + ore_robots * mins,
                    clay + clay_robots * mins,
                    obs + obs_robots * mins,
                    geodes + geode_robots * mins,
                ),
            )

        mins = max(0, ceil((clay_cost - ore) / ore_robots)) + 1
        if not mins > minutes:
            max_geodes = max(
                max_geodes,
                mine(
                    int(minutes - mins),
                    ore_cost,
                    clay_cost,
                    obs_cost,
                    geode_cost,
                    ore_robots,
                    clay_robots + 1,
                    obs_robots,
                    geode_robots,
                    ore + ore_robots * mins - clay_cost,
                    clay + clay_robots * mins,
                    obs + obs_robots * mins,
                    geodes + geode_robots * mins,
                ),
            )
    if ore_robots and clay_robots:
        mins = (
            max(
                0,
                max(
                    ceil((obs_cost[0] - ore) / ore_robots),
                    ceil((obs_cost[1] - clay) / clay_robots),
                ),
            )
            + 1
        )
        if not mins > minutes:
            max_geodes = max(
                max_geodes,
                mine(
                    int(minutes - mins),
                    ore_cost,
                    clay_cost,
                    obs_cost,
                    geode_cost,
                    ore_robots,
                    clay_robots,
                    obs_robots + 1,
                    geode_robots,
                    ore + ore_robots * mins - obs_cost[0],
                    clay + clay_robots * mins - obs_cost[1],
                    obs + obs_robots * mins,
                    geodes + geode_robots * mins,
                ),
            )
    if ore_robots and obs_robots:
        mins = (
            max(
                0,
                max(
                    ceil((geode_cost[0] - ore) / ore_robots),
                    ceil((geode_cost[1] - obs) / obs_robots),
                ),
            )
            + 1
        )
        if not mins > minutes:

            max_geodes = max(
                max_geodes,
                mine(
                    int(minutes - mins),
                    ore_cost,
                    clay_cost,
                    obs_cost,
                    geode_cost,
                    ore_robots,
                    clay_robots,
                    obs_robots,
                    geode_robots + 1,
                    ore + ore_robots * mins - geode_cost[0],
                    clay + clay_robots * mins,
                    obs + obs_robots * mins - geode_cost[1],
                    geodes + geode_robots * mins,
                ),
            )

    max_geodes = max(max_geodes, geodes + minutes * geode_robots)

    return max_geodes


def main():
    minutes = 32
    p = 1
    for i, line in enumerate(open("input.txt")):
        if i == 3:
            break
        line = line.split()
        n = int(line[1].replace(":", ""))
        ore_cost = int(line[6])
        clay_cost = int(line[12])
        obs_cost = (int(line[18]), int(line[21]))
        geode_cost = (int(line[27]), int(line[30]))

        geodes = mine(
            minutes, ore_cost, clay_cost, obs_cost, geode_cost, 1, 0, 0, 0, 0, 0, 0, 0
        )

        print("Blueprint", n, geodes, "geodes")

        p *= geodes

    print(p)


if __name__ == "__main__":
    main()
