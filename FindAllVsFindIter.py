import re

my_string = 'abc123ABC123abc'
pattern = re.compile(r'123')
# matches = pattern.finditer(my_string)
# for match in matches:
#     print(match)
#     print(match.span(), match.start(), match.end())
#     print(match.group()) # returns the string

# print()
# # findall()
# pattern = re.compile(r'123')
# matches = pattern.findall(my_string)
# for match in matches:
#     print(match)


#print()
# match
match = pattern.match(my_string)
print(match)
pattern = re.compile(r'abc')
match = pattern.match(my_string)
print(match)

#print()
# search
match = pattern.search(my_string)
print(match)