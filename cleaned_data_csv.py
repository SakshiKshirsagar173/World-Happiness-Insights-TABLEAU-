import pandas as pd

# List of datasets with their corresponding year
files = {
    2015: "2015.csv",
    2016: "2016.csv",
    2017: "2017.csv",
    2018: "2018.csv",
    2019: "2019.csv"
}

dfs = []

for year, file in files.items():
    df = pd.read_csv(file)

    # Standardize column names for each year
    column_mapping = {
        "Country": "Country",
        "Country or region": "Country",

        "Happiness Score": "Happiness Score",
        "Happiness.Score": "Happiness Score",
        "Score": "Happiness Score",

        "Economy (GDP per Capita)": "GDP per Capita",
        "Economy..GDP.per.Capita.": "GDP per Capita",
        "GDP per capita": "GDP per Capita",

        "Family": "Social Support",
        "Social support": "Social Support",

        "Health (Life Expectancy)": "Healthy Life Expectancy",
        "Health..Life.Expectancy.": "Healthy Life Expectancy",
        "Healthy life expectancy": "Healthy Life Expectancy",

        "Freedom": "Freedom",
        "Freedom to make life choices": "Freedom",

        "Generosity": "Generosity",

        "Trust (Government Corruption)": "Corruption",
        "Trust..Government.Corruption.": "Corruption",
        "Perceptions of corruption": "Corruption"
    }

    df = df.rename(columns=column_mapping)

    # Keep only needed columns
    final_columns = [
        "Country", "Happiness Score",
        "GDP per Capita", "Social Support",
        "Healthy Life Expectancy", "Freedom",
        "Generosity", "Corruption"
    ]

    df = df[final_columns]
    df["Year"] = year  # Add year column

    dfs.append(df)

# Combine all years into one dataset
combined = pd.concat(dfs, ignore_index=True)

# Save cleaned dataset
combined.to_csv("World_Happiness_2015_2019_Clean.csv", index=False)

print("✅ Cleaned dataset saved as 'World_Happiness_2015_2019_Clean.csv'")
print(combined.head())
