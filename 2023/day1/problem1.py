from pathlib import Path

def ans(path):
    sum = 0
    with open(path, 'r') as file:
        for line in file:
            line_digit = 0
            for i in line:
                if i.isdigit():
                    line_digit += int(i) * 10
                    break
            for i in line[::-1]:
                if i.isdigit():
                    line_digit += int(i)
                    break
            sum += line_digit
    return sum

if __name__ == '__main__':
    input_file = Path('input.txt')
    print(ans(input_file))