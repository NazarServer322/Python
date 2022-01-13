employers = {"Vasya":8000,
            "Misha":7500,
            "Ura":3000,
             "ALex":9000}
top_homless = []

for key,val in employers.items():
    if val <= 6000:
        top_homless.append((key, val))

#print(top_homless)

top_earmers = [(k, v ) for k ,v in employers.items() if v <= 4000 ]
print(top_earmers)