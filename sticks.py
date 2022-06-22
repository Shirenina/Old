from multiprocessing.sharedctypes import Value


def sticks_game():
    print("""Sticks Game!""")
    n1 = input('Player 1, enter your name: ')
    n2 = input('Player 2, enter your name: ')
    sticks = 10
    print('Sticks on the table: 10')
    while sticks>0:
        try:
            p1 = int(input(f'{n1}, enter a num of the sticks you wanna grab: '))
            sticks-=p1
            if sticks==0:
                winner = n2
                return f'{n2} wins!'
            print(f'Sticks on the table: {sticks}')
            p2 = int(input(f'{n2}, enter a num of the sticks you wanna grab: '))
            sticks-=p2
            if sticks==0:
                winner = n1
                return f'{n1} wins'  
            print(f'Sticks on the table: {sticks}')
        except ValueError:
            print('You need to enter a num!')
 
       
print(sticks_game())