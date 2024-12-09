#https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

def past(h, m, s):
    
    hmili = h * 60 * 60 * 1000
    mmili = m * 60 * 1000
    smili = s * 1000
    
    mili = hmili + mmili + smili
    
    return(mili)