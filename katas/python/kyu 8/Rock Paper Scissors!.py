#https://www.codewars.com/kata/5672a98bdbdd995fad00000f

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'scissors' and p2 == 'rock':
        return 'Player 2 won!'
    elif p2 == 'scissors' and p1 == 'rock':
        return 'Player 1 won!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p2 == 'scissors' and p1 == 'paper':
        return 'Player 2 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    elif p2 == 'paper' and p1 == 'rock':
        return 'Player 2 won!'