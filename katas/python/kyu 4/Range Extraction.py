#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    sol = []
    primera = args[0]

    for num in range(1, len(args) + 1):
        if num == len(args) or args[num] != args[num - 1] + 1:
            if num - args.index(primera) > 2:
                sol.append(f"{primera}-{args[num - 1]}")
            else:
                sol.extend(map(str, args[args.index(primera):num]))
            if num < len(args):
                primera = args[num]

    return ",".join(sol)