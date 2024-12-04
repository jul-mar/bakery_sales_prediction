import itertools
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def find_best_feature_combination(data, max_features=None):
    """
    Find the feature combination with the highest R² score using statsmodels OLS
    
    Parameters:
    data (pd.DataFrame): DataFrame containing features and target
    max_features (int, optional): Maximum number of features to consider
    
    Returns:
    dict: Dictionary with best combination details
    """
    # Prepare feature list (excluding the first columns like VPI and target)
    features_list = [
        'Kuchen', 'Saisonbrot', 'is_holiday', 
        'Temp_Very_Cold', 'Temp_Cold', 'Temp_Mild', 'Temp_Warm', 'Temp_Hot', 
        'Cloud_Clear', 'Cloud_Partly_Cloudy', 'Cloud_Cloudy', 
        'Wind_Light', 'Wind_Moderate', 'Wind_Strong', 
        'Weather_Good', 'Weather_Light_Issues', 'Weather_Moderate', 'Weather_Severe', 'Weather_Unknown'
    ]
    
    # Target variable
    target = 'Umsatz_total'
    
    # If max_features not specified, use all features
    if max_features is None:
        max_features = len(features_list)
    
    # Store results
    results = []
    
    # Scale the features
    scaler = StandardScaler()
    
    # Try combinations from 1 to max_features
    for n in range(1, max_features + 1):
        for combo in itertools.combinations(features_list, n):
            # Select features for this combination
            X = data[list(combo)]
            y = data[target]
            
            # Scale features
            X_scaled = scaler.fit_transform(X)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
            
            # Add constant term for intercept
            X_train_with_const = sm.add_constant(X_train)
            
            # Fit OLS model
            try:
                model = sm.OLS(y_train, X_train_with_const).fit()
                
                # Store results
                results.append({
                    'features': combo,
                    'r2': model.rsquared,
                    'adj_r2': model.rsquared_adj,
                    'n_features': len(combo),
                    'aic': model.aic,
                    'bic': model.bic
                })
            except Exception as e:
                print(f"Error processing combination {combo}: {e}")
    
    # Convert results to DataFrame and sort
    results_df = pd.DataFrame(results)
    
    # Sort by adjusted R² (to penalize adding too many features)
    results_sorted = results_df.sort_values('adj_r2', ascending=False)
    
    # Top 10 combinations
    top_10 = results_sorted.head(10)
    
    return {
        'top_10_combinations': top_10,
        'full_results': results_sorted
    }

# Load the data
data = pd.read_csv('/workspaces/bakery_sales_prediction/0_DataPreparation/Trainingsdaten.csv')

# Find best feature combinations
result = find_best_feature_combination(data)

# Print top 10 combinations
print("Top 10 Feature Combinations:")
print(result['top_10_combinations'])

# Optional: Save full results to CSV
result['full_results'].to_csv('feature_combination_results.csv', index=False)