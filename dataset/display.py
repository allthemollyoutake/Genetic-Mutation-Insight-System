import pandas as pd
url = "https://raw.githubusercontent.com/allthemollyoutake/Genetic-Mutation-Insight-System/refs/heads/main/dataset/clinvar_conflicting.csv"
df = pd.read_csv(url, nrows=100)
print(df.head())
print(df.info())
