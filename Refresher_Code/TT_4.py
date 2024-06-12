list_1 = ['india', 'america', 'russia', 'iceland', 'china']

# op = []
# for item in list_1:
#     if item[0] == "i" and item not in op:
#         op.append(item)
# print(op)

op = []
op = [item for item in list_1 if item[0] == "i" and item not in op]
print(op)
print(tuple(op))
print(set(op))
#print(dict(op))
print(','.join(op))
