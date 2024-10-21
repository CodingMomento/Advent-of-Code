from pathlib import Path

def ans(path):
    symbols = ['!', '@', '#', '$', '%', '/', '&', '*', '+', '-', '=']
    lines = []

    def surroundings(l, w):
        pos = [[0, -1], [0, 1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]]
        for i in range(8):
            n_l = l + pos[i][0]
            n_w = w + pos[i][1]

            if in_bounds(n_l, n_w) and lines[n_l][n_w] in symbols:
                return 1
        return 0
    
    def in_bounds(l, w):
        return l >= 0 and w >= 0 and l < len(lines) and w < len(lines[l])
    
    with open(path) as file:
        for l in file:
            lines.append([*l])

    sum = 0
    for l in range(len(lines)):
        w = 0
        while (w < len(lines[1]) - 1):
            symbol_count = 0
            if lines[l][w].isnumeric():
                string_num = ""
                num_count = w
                while lines[l][num_count].isnumeric():
                    string_num += lines[l][num_count]
                    symbol_count += surroundings(l, num_count)
                    num_count += 1
                w = num_count
            if symbol_count > 0:
                sum += int(string_num)
            else:
                w += 1

    return sum

if __name__ == '__main__':
    path = Path('input.txt')
    print(ans(path))