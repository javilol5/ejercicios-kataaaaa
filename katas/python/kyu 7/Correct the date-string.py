#https://www.codewars.com/kata/5787628de55533d8ce000b84

from datetime import date as dt, timedelta as td
import re


def date_correct(stg):
    if stg is None or not stg:
        return stg
    if not re.match(r"\d\d\.\d\d\.\d{4}", stg):
        return
    d, m, y = (int(n) for n in stg.split("."))
    while m > 12:
        m, y = m-12, y+1
    date = dt(y, m, 1) + td(d-1)
    return date.strftime("%d.%m.%Y")