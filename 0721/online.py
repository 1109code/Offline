# target = input()
# target_list = []

# for i in target[1:-1:3]:
#     target_list.append(int(i))

# target_dict = {}

# for i, j in enumerate(target_list):
#     target_dict[str(i)] = str(j)
# result = []
# for i in target_dict.keys():
#     if target_dict[int(i)] == target_dict[int(i)+1]:
#         pass
#     else:
#         result.append(target_dict[i])
# result.append(target_dict[int(len(target_list)-1)])

# print(result)
##########################################
# target = input()
# target_list = []

# result = []

# for i in target[1:-1:3]:
#     target_list.append(int(i))
    
# for i in range(len(target_list)-1):
#     if target_list[i] == target_list[i+1]:
#         pass
#     else:
#         result.append(target_list[i])

# result.append(target_list[-1])

# print (result)
########################################
target = input()
target_list = []

result = []

for i in target[1:-1:3]:
    target_list.append(int(i))
    
for i, j in enumerate(target_list):
    if i == len(target_list)-1:
        break
    elif target_list[i] == target_list[i+1]:
        pass
    else:
        result.append(j)

result.append(target_list[-1])

print (result)