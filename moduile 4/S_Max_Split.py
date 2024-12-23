def split_balanced_string(S):
    count_L = 0
    count_R = 0
    balanced_strings = []
    current_string = ""
    for char in S:
        current_string += char
        if char == 'L':
            count_L += 1
        else:  
            count_R += 1
        if count_L == count_R:
            balanced_strings.append(current_string)
            current_string = ""  
            count_L = 0
            count_R = 0
    print(len(balanced_strings))
    for b_string in balanced_strings:
        print(b_string)
input_string = input().strip()
split_balanced_string(input_string)