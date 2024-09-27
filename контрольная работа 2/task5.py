input_numbers = list(map(int, list(input("Введите последовательность (без пробелов): "))))


def find_last_borders(_input: list[int]) -> tuple[int, int]:
    pos_first_border, pos_second_border = 0, -1
    
    i = 0
    while i < len(_input):
        if _input[i] == 0:
            pos_second_border = pos_first_border
            pos_first_border = i

        i += 1
        
    return (pos_first_border, pos_second_border)


positions = find_last_borders(_input=input_numbers)

result = 0
print(sum(input_numbers[positions[1]:positions[0]]))
