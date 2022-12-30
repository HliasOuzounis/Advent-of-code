
target_area = ((287, 309), (-76, -48))
# target_area = ((20, 30), (-10, -5))

starting_pos = (0, 0)

def update_pos(pos, vel):
    pos[0] += vel[0]
    pos[1] += vel[1]

    if vel[0] > 0: vel[0] -= 1
    if vel[0] < 0: vel[0] += 1
    
    vel[1] -= 1

    return pos, vel

def hit_target(pos, tatget):
    if pos[0] >= tatget[0][0] and pos[0] <= tatget[0][1]:
        if pos[1] >= tatget[1][0] and pos[1] <= tatget[1][1]:
            return True
    else:
        return False

def overshot(pos, target):
    if pos[0] > target[0][1] or pos[1] < target[1][0]:
        return True
    else: 
        return False

ultimate_y = 0
for x_vel in range(target_area[0][1] + 1):
    for y_vel in range(target_area[1][0], 100):
        max_y = 0
        pos = list(starting_pos)
        vel = [x_vel, y_vel]
        while not overshot(pos, target_area):
            pos, vel = update_pos(pos, vel)
            max_y = max(max_y, pos[1])
            if hit_target(pos, target_area): 
                if max_y > ultimate_y:
                    ultimate_y = max_y
                    ultimate_vel = (x_vel, y_vel)
                break

print(ultimate_y, ultimate_vel)


