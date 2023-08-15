import re


def patterns_finder(text, pattern):
    ans = re.findall(pattern, text)
    return ans
