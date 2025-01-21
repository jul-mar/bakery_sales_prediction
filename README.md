# Sales Forecasting for a Bakery Branch

## Repository Link

https://github.com/jul-mar/bakery_sales_prediction

## Description

This project focuses on sales forecasting for a bakery branch, utilizing historical sales data spanning from July 1, 2013, to July 30, 2018, to inform inventory and staffing decisions. We aim to predict future sales for six specific product categories: Bread, Rolls, Croissants, Confectionery, Cakes, and Seasonal Bread. Our methodology integrates statistical and machine learning techniques, beginning with a baseline linear regression model to identify fundamental trends, and progressing to a sophisticated neural network designed to discern more nuanced patterns and enhance forecast precision. The initiative encompasses data preparation, crafting bar charts with confidence intervals for visualization, and fine-tuning models to assess their performance on test data from August 1, 2018, to July 30, 2019, using the Mean Absolute Percentage Error (MAPE) metric for each product category.

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
