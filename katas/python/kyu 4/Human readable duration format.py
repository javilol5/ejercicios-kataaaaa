#https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if seconds == 0:
        return "now"
    units = [("year", 365 * 24 * 60 * 60) , ("day", 24 * 60 * 60) , ("hour", 60 * 60) , ("minute", 60) , ("second", 1),]
    parts = []
    
    for name, unit_seconds in units:
        value, seconds = divmod(seconds, unit_seconds)
        if value > 0:
            parts.append(f"{value} {name}" + ("s" if value > 1 else ""))
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " and " + parts[-1]