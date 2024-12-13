#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    
    result = []
    while snail_map:
        
        result += snail_map.pop(0)
        
        if snail_map and snail_map[0]:
            for row in snail_map:
                result.append(row.pop())
        if snail_map:
            result += snail_map.pop()[::-1]
        if snail_map and snail_map[0]:
            for row in reversed(snail_map):
                result.append(row.pop(0))
                
    return result