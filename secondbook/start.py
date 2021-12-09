employers = {"Vasya":8000,
            "Misha":7500,
            "Ura":3000,
             "ALex":9000}
top_homless = []

for key,val in employers.items():
    if val <= 6000:
        top_homless.append((key, val))

print(top_homless)