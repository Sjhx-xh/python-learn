my_dict = [
    {"name":"wang","grade":1,"salary":3000},
    {"name":"zhou","grade":2,"salary":5000},
    {"name":"lin","grade":3,"salary":7000},
    {"name":"zhang","grade":1,"salary":4000},
    {"name":"liu","grade":4,"salary":6000, }
]
for item in my_dict:
    if item["grade"] == 1:
        item["grade"] += 1
        item["salary"] *= 2
print(my_dict)