from pathlib import Path

def ans(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        cards = []
        for _ in range(len(lines)):
            cards.append(1)

        for line in range(len(lines)):
            line_split = lines[line].split()
            line_split = line_split[2:]
            string_line = ' '.join(line_split).strip()
            half_split = string_line.split('|')
            winning_nums = half_split[0].strip().split()
            curr_nums = half_split[1].strip().split()

            points = 0
            
            for num in curr_nums:
                if num in winning_nums:
                    points += 1          
            
            for i in range(points):
                if line + 1 + 1 < len(lines):
                    cards[line + i + 1] += cards[line]

    return sum(cards)


if __name__ == '__main__':
    test_path = Path('test.txt')
    input_path = Path('input.txt')

    print(ans(test_path))
    print(ans(input_path))