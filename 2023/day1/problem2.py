from pathlib import Path

def ans(path):
    sum = 0
    letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    with open(path, 'r') as file:
        for line in file:
            first_index = float('inf')
            first = 0
            last_index = -1
            last = 0

            for l in range(9):
                try:
                    found_first = line.index(letters[l])
                    found_last = line.rindex(letters[l])

                    if found_first < first_index:
                        first_index = found_first
                        first = 10 * (l + 1)
                    if found_last > last_index:
                        last_index = found_last
                        last = l + 1
                except ValueError:
                    pass

            for l in range(9):
                try:
                    found_first = line.index(nums[l])
                    found_last = line.rindex(nums[l])

                    if found_first < first_index:
                        first_index = found_first
                        first = 10 * (l + 1)
                    if found_last > last_index:
                        last_index = found_last
                        last = l + 1
                except ValueError:
                    pass
        
            sum += (first + last)

    return sum

if __name__ == '__main__':
    input_file = Path('input.txt')
    print(ans(input_file))