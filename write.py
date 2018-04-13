import json
data = {}
try:
    with open('data.txt','r') as f:
        data = json.load(f)
except:
    print("No exists")
while(1):
    choice = input()
    if (choice == '0'):
        break
    if (choice == '1'):#添加
        account = input()
        password = input()
        data[account] = password
    if (choice == '2'):#修改
        account = input()
        password = input()
        data[account] = password
    if (choice == '-1'):#删除
        account = input()
        del data[account]
with open("data.txt",'w') as f1:
    json.dump(data,f1)