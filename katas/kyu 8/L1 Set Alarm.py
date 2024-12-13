#https://www.codewars.com/kata/568dcc3c7f12767a62000038

def set_alarm(employed, vacation):
    if employed == vacation:
        return False
    elif employed == False and vacation == True:
        return False
    else:
        return True