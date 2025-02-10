# Model Definition and Evaluation

## Model Selection

Multiple neural network architectures were explored, including models incorporating lag data, regularization techniques, and hyperparameter tuners. After extensive evaluation, **V4_Regularisation_Model** demonstrated superior performance on the validation set. Further fine-tuning and evaluation on the test set identified **V7_Regularisation_Less_Neurons_Model** as the best-performing model overall.

Each product category was modeled with its own neural network, each having customized hyperparameters and feature sets tailored to its specific characteristics.

## Feature Engineering

Key features included temporal variables such as date, day of the week, promotional events, and historical sales data. Feature selection for each product category was informed by a combination of **linear and non-linear correlation analyses** conducted in the [**2_BaselineModel**](2_BaselineModel/README.md) stage, complemented by iterative manual testing and domain expertise.

## Hyperparameter Tuning

A combination of automated hyperparameter tuning and manual experimentation was used to optimize model performance. The primary hyperparameters adjusted were:

- Learning rate
- Batch size
- Number of epochs
- Activation functions
- Number of layers
- Neurons per layer
- Dropout rate
- Regularization (L2)
- Optimizer (SGD, Adam, RMSprop)
- Beta values for the Adam optimizer (β1, β2)

These parameters were systematically tested to balance bias and variance, resulting in the best-performing configuration for each model.

## Implementation

The models were implemented using **Python**, leveraging the **Keras** and **TensorFlow** libraries for neural network construction and training.

## Evaluation Metrics

Model performance was measured using the following metrics:
- **Mean Absolute Error (MAE)**: To evaluate absolute prediction accuracy.
- **Mean Absolute Percentage Error (MAPE)**: To understand relative error rates.

Additionally, **loss function progression** and **prediction plots** were closely monitored to diagnose underfitting, overfitting, and overall model behavior.
