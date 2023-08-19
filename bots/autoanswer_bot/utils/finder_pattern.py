import re


def survey_patterns_finder(string):
    pattern = r'Input_2: @\w+|Input_2: \w+'
    ans = re.findall(pattern=pattern, string=string)[0][9:]
    return ans


def order_patterns_finder(string):
    pattern = r'Ссылка_на_Телеграм: \w+|Ссылка_на_Телеграм: @\w+'
    ans = re.findall(pattern=pattern, string=string)[0][20:]
    return ans
