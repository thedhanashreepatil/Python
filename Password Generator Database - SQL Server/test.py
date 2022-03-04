# import json
# with open("data.json", "r") as data_file:
#     data = json.load(data_file)

f = ['Amazon', 'Noob', 'dadaadadad']
a = 'noob'
a = a.lower()
if a in [b.lower() for b in f]:
    print(True)
else:
    print(False)

# for domain in data:
#     if a.lower() == domain.lower():
#         print(domain)

# if a in [domain.lower() for domain in data]:
#     print(data[a])


