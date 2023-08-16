import re


def patterns_finder(pattern, string):
    ans = re.findall(pattern=pattern, string=string)[0][9:]
    return ans
