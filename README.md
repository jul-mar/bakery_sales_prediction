# Sales Forecasting for a Bakery Branch

## Repository Link

https://github.com/jul-mar/bakery_sales_prediction

## Description

As part of the "Einführung in Data Science und maschinelles Lernen" course at opencampus.sh, this project develops a machine learning solution for sales forecasting at a bakery branch. The system predicts sales across six distinct product categories: Bread, Rolls, Croissants, Confectionery, Cakes, and Seasonal Bread, by training on historical data from July 2013 to July 2018, with testing performed on data spanning August 2018 to July 2019.

The solution architecture demonstrates data science principles through multiple neural networks, with dedicated models for each product category. The final implementation evolved through systematic experimentation, progressing from baseline SGD regressors to neural network configurations. The feature set encompasses temporal variables, event data (including cruise ship arrivals and local events), weather conditions, and seasonal indicators, selected through rigorous correlation analysis.

The model architecture implemented with the Keras/TensorFlow framework showcases machine learning best practices, incorporating regularization techniques and optimized hyperparameters specific to each product category. The data preprocessing pipeline demonstrates handling of missing values through alternative data sources and temporal interpolation, while categorical variables undergo one-hot encoding.

Performance evaluation employs industry-standard metrics, with Mean Absolute Percentage Error (MAPE) as the primary measure, supplemented by MAE for absolute accuracy assessment. 

### Task Type

Regression

### Results Summary

-   **Best Model:** V4_Regularisation
-   **Evaluation Metric:** MAPE on validation data

-   **Result by Category** (Identifier):
    -   **Bread** (1): 18.53 %
    -   **Rolls** (2): 12.08 %
    -   **Croissant** (3): 19.48 %
    -   **Confectionery** (4): 21.81 %
    -   **Cake** (5): 14.73 %
    -   **Seasonal Bread** (6): 34.17 %

-   **Result Total** (weighted average): 17.87 %

## Documentation

1.  [**Data Import and Preparation**](0_DataPreparation/README.md)
3.  [**Dataset Characteristics (Barcharts)**](1_DatasetCharacteristics/README.md)
4.  [**Baseline Model**](2_BaselineModel/README.md)
5.  [**Model Definition and Evaluation**](3_Model/README.md)
6.  [**Presentation**](4_Presentation/README.md)

## Cover Image

![](CoverImage/cover_image.png)
