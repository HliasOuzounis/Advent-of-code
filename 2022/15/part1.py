def main():
    sensors = []
    scan_power = []
    beacons = []

    for line in open("input.txt"):
        sensor, beacon = line.strip().replace("x=", "").replace("y=", "").replace(",", "").split(": ")
        sensor = sensor.split()[-2:]
        beacon = beacon.split()[-2:]
        
        sensor = tuple(map(int, sensor))
        beacon = tuple(map(int, beacon))
        sensors.append(sensor)
        beacons.append(beacon)

        scan_power.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))

    target_line = 2_000_000
    scanned = set()
    ans = 0
    for sensor, scan_size in zip(sensors, scan_power):
        dist_to_line = abs(sensor[1] - target_line)
        if dist_to_line > scan_size:
            continue
        
        scan_power_left = scan_size - dist_to_line
        for i in range(-scan_power_left, scan_power_left + 1):
            scanned.add((target_line, sensor[0] + i))

    ans = len(scanned) - len(set(beacon for beacon in beacons if beacon[1] == target_line))

    print(ans)        


if __name__ == "__main__":
    main()