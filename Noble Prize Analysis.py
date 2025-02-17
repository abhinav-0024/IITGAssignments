import requests
import csv

# Step 1: Download the CSV file
url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Nobel%20Laureattes.csv"
response = requests.get(url)

# Save it locally
filename = "nobel_laureates.csv"
with open(filename, "wb") as file:
    file.write(response.content)

# Step 2: Read the CSV file
country_prizes = {}

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    for row in reader:
        birth_country = row[4]  # Assuming 'Birth Country' is at index 4
        
        if birth_country:  # Ensure it's not empty
            if birth_country in country_prizes:
                country_prizes[birth_country] += 1
            else:
                country_prizes[birth_country] = 1

# Step 3: Convert dictionary to a list and sort
sorted_countries = sorted(country_prizes.items(), key=lambda x: x[1], reverse=True)

# Step 4: Print the top 20 countries
print("Top 20 Countries with Most Nobel Prizes:")
for i, (country, count) in enumerate(sorted_countries[:20]):
    print(f"{i+1}. {country}: {count} prizes")
