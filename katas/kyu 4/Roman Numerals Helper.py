#https://www.codewars.com/kata/51b66044bce5799a7f000003

class RomanNumerals:
    def to_roman(val : int) -> str:
    
        num = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    
        syms = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]
    
        roman_numeral = ""
        i = 0
        while val > 0:  
    
            for _ in range(val // num[i]):  
                roman_numeral += syms[i]  
                val -= num[i]  
            i += 1
            
        return roman_numeral
    
    
    
    
    

    def from_roman(roman_num : str) -> int:
        roman_map = { 'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000 }
    
        total = 0
        prev_value = 0

        for char in reversed(roman_num):  
            current_value = roman_map[char]  
        
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
        
            prev_value = current_value

        return total