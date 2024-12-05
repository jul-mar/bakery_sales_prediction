import itertools
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def find_best_two_feature_combinations(data):
    """
    Findet die besten Kombinationen von 2 Variablen für die lineare Regression
    
    Parameters:
    data (pd.DataFrame): DataFrame mit Features und Zielvariale
    
    Returns:
    pd.DataFrame: Sortierte Ergebnisse der Kombinationen
    """
    # Feature-Liste (ohne Zielvarible)
    features_list = [
        'Brot', 'Broetchen', 'Croissant', 'Konditorei', 'Kuchen', 'Saisonbrot', 'Temp_Very_Cold', 'Temp_Cold', 'Temp_Mild', 'Temp_Warm', 'Temp_Hot', 'Cloud_Clear', 'Cloud_Partly_Cloudy', 'Cloud_Cloudy', 'Wind_Light', 'Wind_Moderate', 'Wind_Strong', 'Weather_Good', 'Weather_Light_Issues', 'Weather_Moderate', 'Weather_Severe', 'Weather_Unknown', 'KielerWoche', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag', 'VPI', 'Heimspiel', 'Feiertag', 'is_holiday', 'Weihnachtsmarkt', 'Markt'
    ]
    
    # Zielvarible
    target = 'Umsatz_total'
    
    # Ergebnisse speichern
    results = []
    
    # Skalierung der Features
    scaler = StandardScaler()
    
    # Kombinationen von 2 Variablen
    for combo in itertools.combinations(features_list, 3):
        # Features für diese Kombination auswählen
        X = data[list(combo)]
        y = data[target]
        
        # Features skalieren
        X_scaled = scaler.fit_transform(X)
        
        # Daten aufteilen
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
        # Konstanten-Term hinzufügen
        X_train_with_const = sm.add_constant(X_train)
        
        # OLS-Modell anpassen
        try:
            model = sm.OLS(y_train, X_train_with_const).fit()
            
            # Ergebnisse speichern
            results.append({
                'Feature 1': combo[0],
                'Feature 2': combo[1],
                'R²': model.rsquared,
                'Adjustiertes R²': model.rsquared_adj,
                'AIC': model.aic,
                'BIC': model.bic,
                'P-Wert (Feature 1)': model.pvalues[1],
                'P-Wert (Feature 2)': model.pvalues[2]
            })
        except Exception as e:
            print(f"Fehler bei Kombination {combo}: {e}")
    
    # Ergebnisse in DataFrame umwandeln und nach adjustiertem R² sortieren
    results_df = pd.DataFrame(results)
    results_sorted = results_df.sort_values('Adjustiertes R²', ascending=False)
    
    return results_sorted

# Daten laden
data = pd.read_csv('/workspaces/bakery_sales_prediction/0_DataPreparation/Trainingsdaten.csv')

# Beste 2-Variablen-Kombinationen finden
result = find_best_two_feature_combinations(data)

# Top 10 Kombinationen ausgeben
print("Top 10 Zwei-Variablen-Kombinationen:")
print(result.head(10))

# Ergebnisse in CSV speichern
result.to_csv('zwei_variablen_kombinationen.csv', index=False)