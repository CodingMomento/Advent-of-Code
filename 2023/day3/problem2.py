from pathlib import Path

def ans(path):
    def surroundings(l, w):
        pos = [[0, -1], [0, 1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]]
        gears = []
        has_seen = []
        for i in range(8):
            n_l = l + pos[i][0]
            n_w = w + pos[i][1]

            if len(gears) > 2:
                return 0

            if in_bounds(n_l, n_w) and lines[n_l][n_w].isnumeric() and (n_l, n_w) not in has_seen:
                has_seen.append(n_l)
                gear = lines[n_l][n_w]
                left = n_w - 1
                right = n_w + 1

                while lines[n_l][left].isnumeric():
                    if in_bounds(n_l, left):
                        gear = lines[n_l][left] + gear
                        has_seen.append((n_l, left))
                    left -= 1

                while lines[n_l][right].isnumeric():
                    if in_bounds(n_l, right):
                        gear += lines[n_l][right]
                        has_seen.append((n_l, right))
                    right += 1

                gears.append(gear)
        
        if len(gears) == 2:
            return int(gears[0]) * int(gears[1])
        return 0

    
    def in_bounds(l, w):
        return l >= 0 and w >= 0 and l < len(lines) and w < len(lines[l])
    
    lines = []
    with open(path) as file:
        for l in file:
            lines.append([*l])

    sum = 0
    for l in range(len(lines)):
        for w in range(len(lines[l])):
            if lines[l][w] == '*':
                sum += surroundings(l, w)
    return sum

if __name__ == '__main__':

    path = Path('test.txt')
    path2 = Path('input.txt')
    print(ans(path))
    print(ans(path2))