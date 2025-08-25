import pandas as pd

# List of datasets with their years
files = {
    "2015": "2015.csv",
    "2016": "2016.csv",
    "2017": "2017.csv",
    "2018": "2018.csv",
    "2019": "2019.csv"
}

# Empty list to hold dataframes
dfs = []

for year, file in files.items():
    df = pd.read_csv(file)
    df["Year"] = int(year)   # Add Year column
    dfs.append(df)

# Combine all
combined = pd.concat(dfs, ignore_index=True)

# Save to new CSV
combined.to_csv("World_Happiness_2015_2019.csv", index=False)
