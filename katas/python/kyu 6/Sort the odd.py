#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])
    
    
    odd_index = 0
    
    
    result = []
    
    for num in source_array:
        if num % 2 != 0:  
            result.append(odd_numbers[odd_index])
            odd_index += 1
        else:  
            result.append(num)
    
    return result