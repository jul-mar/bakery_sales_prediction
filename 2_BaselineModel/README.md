# Baseline Model

A model was created for each of the 6 product groups, implementing a Stochastic Gradient Descent (SGD) Regressor to predict sales for the respective product group. The combination of these models serves as a baseline model for the bakery's sales forecast.

- **Feature Selection**

For each of the 6 models, features were individually selected that yielded the best evaluation metrics (especially MAPE) in the training and validation datasets when combined. The selection was made based on correlation matrices and investigations of mutual information.

- **Implementation**

To train the 6 different models, only the data relevant for the corresponding product group was used. The model training was then performed using an SGD-Regressor from the Scikit-Learn library. Here, "invscaling" was chosen as a learning rate that reduces over time.

- **Evaluation**

The models were evaluated using several metrics:

Mean Absolute Error (MAE): Measures the average absolute deviation
Mean Squared Error (MSE): Penalizes larger deviations more heavily
Mean Absolute Percentage Error (MAPE): Shows the percentage deviation
Adjusted R²: Takes model complexity into account when evaluating prediction quality

Additionally, the results were visualized through a scatter plot of actual vs. predicted values.