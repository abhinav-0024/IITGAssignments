import requests
import csv

url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Nobel%20Laureattes.csv"
response = requests.get(url)
filename = "nobel_laureates.csv"
with open(filename, "wb") as file:
    file.write(response.content)
country_prizes = {}

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        birth_country = row[4] 
        if birth_country:
            if birth_country in country_prizes:
                country_prizes[birth_country] += 1
            else:
                country_prizes[birth_country] = 1
sorted_countries = sorted(country_prizes.items(), key=lambda x: x[1], reverse=True)
print("Top 20 Countries with Most Nobel Prizes:")
for i, (country, count) in enumerate(sorted_countries[:20]):
    print(f"{i+1}. {country}: {count} prizes")
