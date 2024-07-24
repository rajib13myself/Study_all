"Power of the list"
numbers = [1, 2, 3, 4, 5]
power = 4
pow_num = [n ** power for n in numbers]
print(f"{numbers} of the {power} is: ",pow_num)

"String functions"
str = "The value of six numbers is 275"
print(f"\nTotal length of the given string is: ", len(str))
index = 7

left_str = str[:index+2]
right_str = str[index+2:]

print(f'\nLeft of string with {index}: ', left_str)
print(f'\nRight of the string with {index+1}:', right_str)

start_char = ' '
end_char = 's'

str_startpoint = str.find(start_char)
str_1stendpoint = str.find(end_char)
str_2ndendpoint = str.find(end_char, str_1stendpoint + 1)


if str_startpoint != -1 and str_2ndendpoint != -1 and str_2ndendpoint > str_startpoint:
    trim_str = str[:str_startpoint] + ' ' + str[str_2ndendpoint:]
else:
    trim_str = str

print(f'\nOriginal string is: ', str)
print(f'\nTrimed between of {str_startpoint} and {str_2ndendpoint} string is: ', trim_str)
