from pathlib import Path

def ans(path):
    sum = 0
    with open(path, 'r') as file:
        for line in file:
            line_split = line.split(' ')
            line_split = line_split[2:]
            string_line = ' '.join(line_split).strip()
            half_split = string_line.split('|')
            winning_nums = half_split[0].strip().split()
            curr_nums = half_split[1].strip().split()

            points = 0
            
            for num in curr_nums:
                if num in winning_nums:
                    if points == 0:
                        points += 1
                    else:
                        points *= 2
            sum += points
    return sum


if __name__ == '__main__':
    test_path = Path('test.txt')
    input_path = Path('input.txt')

    #print(ans(test_path))
    print(ans(input_path)) 