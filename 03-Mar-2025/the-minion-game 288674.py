# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    # your code goes here
    v = "AEIOU"
    ks = 0
    ss = 0
    for i in range(len(string)):
        if string[i] in v:
            ks += len(string) - i
        else:
            ss += len(string) - i
    if ks > ss:
        print(f"Kevin {ks}" )
    elif ss > ks:
        print(f"Stuart {ss}")
    else:
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)