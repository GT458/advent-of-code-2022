
def calculate_calories_carried():
    f = open('input.txt', 'r')
    current = 0
    max_elf = 0
    elf_cals = []
    for num in f:
        conv = num.strip()
        if len(conv) > 0:
            current+= int(conv)
        else:
            if (current > max_elf):
                max_elf = current  
            elf_cals.append(current)
            current = 0
    elf_cals.sort()
    print(f'Most calories held by an elf: {elf_cals[-1]}')
    print(f'Calories held by the top three elves: {sum(elf_cals[::-1][0:3])}')

    f.close()

calculate_calories_carried()