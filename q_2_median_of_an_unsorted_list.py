def find_median(numbers: list) -> float:
    numbers.sort()
    len_num = len(numbers)
    mid_num = len_num // 2
    if len_num % 2 == 0:
        num_1 =  numbers[mid_num - 1]
        num_2 = numbers[mid_num]
        madian = (num_1 + num_2) / 2
    else:
        return numbers[mid_num]
    return float(madian)

print(find_median([2, 7, 10 ,9]))