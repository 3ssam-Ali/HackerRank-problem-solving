def minion_game(string):
    # your code goes here
    Stuart=0 #consonants
    Kevin=0 #vowel
    v= 'AEIOU'
    for i in range(len(string)):
        if string[i] in v: Kevin+=len(string)-i
        else: Stuart+=len(string)-i
    if Stuart==Kevin: print('Draw')
    else: print('Stuart'if Stuart>Kevin else 'Kevin', max(Kevin,Stuart))

if __name__ == '__main__':
    s = input()
    minion_game(s)