ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
rev_dict = {}
for key, value in ascii_dict.items():
    rev_dict.update({value:key})
print(rev_dict)