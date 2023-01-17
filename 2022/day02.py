import pandas as pd
file1 = open('day2.txt', 'r')
lines = file1.readlines()
#score values
VALUES = {'R' : 1, 'P' : 2, 'S' : 3}
#what beats the play
LOSER = {'R' : 'P', 'P' : 'S', 'S': 'R'}
#what does the play beat
WINNER = {'R' : 'S', 'P' : 'R', 'S' : 'P'}


def elf_translator(code):
    if code == 'A':
        return 'R'
    if code == 'B':
        return 'P'
    return 'S'

def your_translator(code):
    if code == 'X':
        return 'R'
    if code == 'Y':
        return 'P'
    return 'S'

def score(play, you):
    if play in ['RP', 'PS', 'SR']:
        #you win
        score = 6 + VALUES.get(you)
        return score
    if play in ['RR', 'PP', 'SS']:
        #you tie
        score = 3 + VALUES.get(you)
        return score
    return VALUES.get(you)

def your_play(elf_play, outcome):
    if outcome == 'X':
        #you need to lose, get what the elf_play beats
        return WINNER.get(elf_play)
    if outcome == 'Y':
        #you tie
        return elf_play
    #you win
    return LOSER.get(elf_play)

rows = []
for line in lines:
    row = {'elf' : line[0], 'input' : line[2]}
    rows.append(row)

df = pd.DataFrame(rows)
df['elf_play'] = df.apply(lambda x: elf_translator(x['elf']), axis=1)
df['your_play'] = df.apply(lambda x: your_translator(x['input']), axis=1)
df['game_play'] = df['elf_play'] + df['your_play']
df['your_score'] = df.apply(lambda x: score(x['game_play'], x['your_play']), axis=1)
print(df['your_score'].sum())

#part 2
df = pd.DataFrame(rows)
df['elf_play'] = df.apply(lambda x: elf_translator(x['elf']), axis=1)
df['your_play'] =  df.apply(lambda x: your_play(x['elf_play'], x['input']), axis=1)
df['game_play'] = df['elf_play'] + df['your_play']
df['your_score'] = df.apply(lambda x: score(x['game_play'], x['your_play']), axis=1)
print(df['your_score'].sum())