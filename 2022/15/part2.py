class Line:
    def __init__(self, point0, point1, power):
        self.x0 = point0[0]
        self.y0 = point0[1]
        self.x1 = point1[0]
        self.y1 = point1[1]
        self.slope = (self.x0 - self.x1) / (self.y0 - self.y1)
        self.power = power

    def point_in_line(self, point):
        x, y = point
        if point in ((self.x0, self.y0), (self.x1, self.y1)):
            return True
        if y == self.y0:
            return False
        return abs(x - self.x0) + abs(y - self.y0) + abs(x - self.x1) + abs(y - self.y1
        ) == 2 * self.power and (self.slope == (self.x0 - x) / (self.y0 - y))

    def intersection(self, line):
        import math

        if self.slope == line.slope:
            return None

        line1, line2 = (self, line) if self.slope == 1 else (line, self)
        c1 = line1.y0 - line1.x0
        c2 = line2.y0 + line2.x0

        x = math.ceil((c2 - c1) / 2)
        y = math.ceil((c2 + c1) / 2)
        return (x, y)


def main():
    sensors = []
    scan_power = []
    beacons = []

    for line in open("input.txt"):
        sensor, beacon = (
            line.strip()
            .replace("x=", "")
            .replace("y=", "")
            .replace(",", "")
            .split(": ")
        )
        sensor = sensor.split()[-2:]
        beacon = beacon.split()[-2:]

        sensor = tuple(map(int, sensor))[::-1]
        beacon = tuple(map(int, beacon))[::-1]
        sensors.append(sensor)
        beacons.append(beacon)

        scan_power.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))
    lines = []
    for sensor, power in zip(sensors, scan_power):
        lines.append(
            Line((sensor[0] - power, sensor[1]), (sensor[0], sensor[1] + power), power)
        )
        lines.append(
            Line((sensor[0] + power, sensor[1]), (sensor[0], sensor[1] - power), power)
        )
        lines.append(
            Line((sensor[0] - power, sensor[1]), (sensor[0], sensor[1] - power), power)
        )
        lines.append(
            Line((sensor[0] + power, sensor[1]), (sensor[0], sensor[1] + power), power)
        )

    intersections = set()
    for i, line1 in enumerate(lines):
        for line2 in lines[(i + 1) :]:
            intersection = line1.intersection(line2)
            if (
                intersection
                and line1.point_in_line(intersection)
                and line2.point_in_line(intersection)
            ):
                intersections.add(intersection)

    candidates = []
    for point in intersections:
        x, y = point
        if all(
            any(line.point_in_line(p) for line in lines)
            for p in ((x + 1, y - 1), (x + 2, y), (x + 1, y + 1))
        ):
            candidates.append((x + 1, y))

    for point in candidates:
        x, y = point
        if all(
            power < abs(sensor[0] - x) + abs(sensor[1] - y)
            for power, sensor in zip(scan_power, sensors)
        ):
            print(y * 4000000 + x)


if __name__ == "__main__":
    main()


def draw_example(sensors, beacons, intersections, lines):
    for r in range(-10, 30):
        for c in range(-10, 30):
            p = (r, c)
            if p in sensors:
                print("S", end="")
            elif p in beacons:
                print("B", end="")
            elif p in intersections:
                print("0", end="")
            elif p == (11, 14):
                print("W", end="")
            elif any(line.point_in_line(p) for line in lines):
                print("#", end="")
            else:
                print("-", end="")
        print(": ", r)
