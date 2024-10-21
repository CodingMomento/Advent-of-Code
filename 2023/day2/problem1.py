from pathlib import Path

def ans(path):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    with open(path, 'r') as file:
        sum = 0
        for line in file:
            line_split = line.split()
            m_game = int(line_split[1].split(':')[0])
            m_sets = ' '.join(line_split[2:]).split(';')
            possible = True
            for s in m_sets:
                for c in s.split(','):
                    c_split = c.strip().split(' ')
                    if c_split[1] == 'red' and int(c_split[0]) > MAX_RED:
                        possible = False
                        break
                    elif c_split[1] == 'green' and int(c_split[0]) > MAX_GREEN:
                        possible = False
                        break
                    elif c_split[1] == 'blue' and int(c_split[0]) > MAX_BLUE:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                sum += m_game
        return sum

if __name__ == '__main__':
    input = Path('input.txt')
    print(ans(input))


