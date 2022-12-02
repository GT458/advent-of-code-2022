
def calculate_assumed_strategy_score():
    f = open('input.txt', 'r')
    score = 0
    scoring_guide = {
        'A': ('Y','X',2),
        'B': ('Z','Y',3),
        'C': ('X','Z',1),
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    for line in f:
        if scoring_guide[line[0]][0] == line[2]:
            score+=6
        elif scoring_guide[line[0]][1] == line[2]:
            score+=3
        score+= scoring_guide[line[2]]
    f.close()
    print(score)
    return score

def calculate_strategy_score():
    f = open('input.txt', 'r')
    score = 0
    scoring_guide = {
        'A': [3,4,8],
        'B': [1,5,9],
        'C': [2,6,7],
    }

    for line in f:
        opp = line[0]
        plr = line[2]

        if plr == 'X':
            score+= scoring_guide[opp][0]
        elif plr == 'Y':
            score+= scoring_guide[opp][1]
        else:
            score+= scoring_guide[opp][2]

    f.close()
    print(score)
    return score

calculate_assumed_strategy_score()
calculate_strategy_score()