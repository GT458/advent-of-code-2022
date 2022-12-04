
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def calculate_sum_priority():
    f = open('input.txt', 'r')
    sum = 0
    
    for line in f.readlines():
        left = line[0:int(len(line)/2)]
        right = line[int(len(line)/2):]

        in_both = traverse_half(left, right)
        for char in in_both:
            sum += char_to_int(char)

    f.close()
    print(sum)
    return sum

def calculate_groups_of_three():
    f = open('input.txt', 'r')
    lines = f.readlines()
    sum = 0

    for i in range(0,len(lines), 3):
        letter = find_common_letter(lines[i], lines[i+1], lines[i+2])
        sum += char_to_int(letter)
    f.close()
    print(sum)
    return sum

def traverse_half(left, right):
    ans = ''
    for i in range(min(len(left), len(right))):
        if left[i] in right:
            return left[i]

    return ans

def char_to_int(char):
    if char in lower_case:
        return lower_case.index(char) + 1
    return upper_case.index(char) + 27


def find_common_letter(a, b, c):
    for i in a:
        if i in b and i in c:
            return i 


calculate_sum_priority()
calculate_groups_of_three()