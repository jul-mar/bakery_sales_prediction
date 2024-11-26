
import pandas as pd
import numpy as np

# Read the Verbraucher Preisindex CSV
# Quelle: https://www.destatis.de/DE/Themen/Wirtschaft/Preise/Verbraucherpreisindex/Publikationen/Downloads-Verbraucherpreise/verbraucherpreisindex-lange-reihen-xlsx-5611103.xlsx?__blob=publicationFile
# Read the CSV with semicolon separator and specify encoding if needed
df_vpi = pd.read_csv("/workspaces/bakery_sales_prediction/0_DataPreparation/Verbraucherpreisindex/Verbraucherpreisindex.csv", sep=';', header=None, 
                        names=['Jahr', 'Monat', 'VPI'], 
                        encoding='utf-8')  # Adjust encoding if needed


# Create a mapping of German month names to numbers
month_mapping = {
    'Januar': 1, 'Februar': 2, 'März': 3, 'April': 4, 
    'Mai': 5, 'Juni': 6, 'Juli': 7, 'August': 8, 
    'September': 9, 'Oktober': 10, 'November': 11, 'Dezember': 12
}

df_vpi['Monat'] = df_vpi['Monat'].map(month_mapping)

# Von Komma zu Punktdecimalzahlen ändern
df_vpi['VPI'] = df_vpi['VPI'].str.replace(',', '.')
df_vpi['VPI'] = df_vpi['VPI'].astype(float)


df_vpi['Datum'] = pd.to_datetime(df_vpi['Jahr'].astype(str) + '-' + df_vpi['Monat'].astype(str) + '-01')


# Keep only Datum and VPI
df_vpi = df_vpi[['Datum', 'VPI']]

# Create a date range for all days
date_range = pd.date_range(start='2013-07-01', end='2018-07-31', freq='D')

# Create a new DataFrame with this date range
df_vpi_daily = pd.DataFrame({'Datum': date_range})

# Merge with original VPI data, using the month start as the key
df_vpi_daily['year_month'] = df_vpi_daily['Datum'].dt.to_period('M')
df_vpi['year_month'] = df_vpi['Datum'].dt.to_period('M')

# Merge and cleanup
df_vpi_daily = df_vpi_daily.merge(df_vpi[['year_month', 'VPI']], on='year_month')
df_vpi_daily = df_vpi_daily[['Datum', 'VPI']]

df_vpi_daily.to_csv('/workspaces/bakery_sales_prediction/0_DataPreparation/Verbraucherpreisindex/vpi_daily.csv', index=False)
