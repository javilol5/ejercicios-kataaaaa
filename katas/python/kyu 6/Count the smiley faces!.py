#https://www.codewars.com/kata/583203e6eb35d7980400002a

def count_smileys(arr):
    x= [':)',';)',':D',';D',':-)',':-D',':~)',':~D',';-)',';-D',';~)',';~D']
    total_count = 0


    for str in x:
    
        total_count += arr.count(str)
    
    return total_count