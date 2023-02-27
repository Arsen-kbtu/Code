import json
with open("sample-data.json") as read_file:
  y=json.load(read_file)
for i in range(0, 3):
  for j, k in y["imdata"][i]['l1PhysIf']["attributes"].items():
    if j == 'dn':
        print(k, end="    ")
    if j == "mtu":
        print(k, end="    ")
    if j == "speed":
        print(k, end="    ")
    