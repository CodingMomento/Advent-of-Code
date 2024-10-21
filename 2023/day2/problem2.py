from pathlib import Path

def ans(path):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    with open(path, 'r') as file:
        sum = 0
        for line in file:
            line_split = line.split()
            m_sets = ' '.join(line_split[2:]).split(';')
            red = 0
            green = 0
            blue = 0
            
            for s in m_sets:
                for c in s.split(','):
                    c_split = c.strip().split(' ')
                    m_color = c_split[1]
                    if m_color == 'red':
                        m_red = int(c_split[0])
                        if m_red > red:
                            red = m_red

                    elif m_color == 'green':
                        m_green = int(c_split[0])
                        if m_green > green:
                            green = m_green

                    elif m_color == 'blue':
                        m_blue = int(c_split[0])
                        if m_blue > blue:
                            blue = m_blue
            sum += red * green * blue
        return sum

if __name__ == '__main__':
    input = Path('input.txt')
    print(ans(input))