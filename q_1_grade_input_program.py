grades_list = []

while True:
    garde = input("Enter a grade")

    try:
        num = int(garde)
        if num == -999:
            if len(grades_list) < 10:
                print("please enter at least 10 grades")
            else:
                break
        elif num < 0 or num > 100:
            print("not in range, skip")
        else:
            grades_list.append(num)

    except ValueError:
        print("invalid input, skip")

print("number of vaild grade:",len(grades_list))
print("class average:", sum(grades_list)/len(grades_list))
print("highest grade:", max(grades_list))
