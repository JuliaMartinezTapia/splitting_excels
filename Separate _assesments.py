import pandas as pd
import numpy as np

# Loading the data with Pandas
df = pd.read_excel("Example separate.xlsx", header=3)

# Storing columns as Series in list
list_series = [df[col] for col in df.columns]

# Storing the Series as separate DataFrames
list_df_prev = [pd.DataFrame(series) for series in list_series]

# Including the concepts in Liquidation as a first column in each DataFrame
indice = np.array(list_series[0])
list_df = [df.set_index(indice).reset_index() for df in list_df_prev[1:]]

# Treatment of data: round to two decimals and rename columns
list_df = [df.round(2).rename(columns={"index": list_df_prev[0].columns[0]}) for df in list_df]

# Generate the names for the separate excels
list_names = df.columns[1:]
list_names  = [list_names [i] + ".xlsx" for i in range(len(list_names ))]


# Save dfs as excels in the same path of the notebook
def save_excels(list_df, list_names):
    for i, name in enumerate(list_names):
        list_df[i].to_excel(name, index=False)

save_excels(list_df, list_names)