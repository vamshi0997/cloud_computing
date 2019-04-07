import sys
filepath = '/input/records.json'  
# order = {}
# line_item = {}
# def create(check, key, temp):
#     print(check)
#     if(check == '"order"'):
#         # print("true")
#         order[key] = [_ for _ in temp]
#     else:
#         # print("false")
#         if(key in line_item):
#             line_item[key].append([_ for _ in temp])
#         else:
#             line_item[key] = [_ for _ in temp]



with open(filepath) as fp:  
   line = fp.readline()
   while line:
        line = line[1:-2]
        temp = line.split(", ")
        # print(temp[0].strip())
        check = temp[0].strip()
        key = temp[1].strip()
        print(check+"+", temp)
        line = fp.readline()






   # cnt = 1
   # while line:
   #     # print("Line {}: {}".format(cnt, line.strip()))
   #     line = fp.readline()
   #     cnt += 1