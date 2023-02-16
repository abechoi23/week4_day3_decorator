# vowelOne
# Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.
# All non-vowels including non alpha characters (spaces,commas etc.) should be included.
# Examples:
# vowelOne "abceios" -- "1001110"

# vowelOne "aeiou, abc" -- "1111100100"


# def vowel_binary(string):
#     vowels = 'aeiou'
#     result = ''
#     for one in string:
#         if one.lower() in vowels:
#             result += '1'
#         else:
#             result += '0'
#     return result


def vowel_binary(astring):
    return ''.join(['1' if letter.lower() in {'a','e','i','o','u'} else '0' for letter in astring])