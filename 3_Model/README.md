# Model Definition and Evaluation

- **Model Selection**

Various neural networks were considered, including Models with e.g. lag data, Regularisation or tuner models. After evaluation, the model V4_Regularisation was selected due to its superior performance on the validation data. Further investigation and optimization on the test data leaded to the best model on the test data: V7_Regularisation_Less_Neurons.

Each product category has it's own neural network with slightly different hyperparameters and features.

- **Feature Engineering**

Key features such as date, day of the week, promotional events and historical sales data were engineered to enhance model accuracy. To figure out the best Features for each product category, severel linear and not linear correlation tests were made in [**2_BaselineModel**](2_BaselineModel/README.md) complemented by manual tests.

- **Hyperparameter Tuning**

Different Hyperparameter tuners were used. Furthermore, systematic testing and developing intuition leaded to the best approach. The adjustet hyperparameters were:

- Learning rate
- Batch size
- Number of epochs
- Activation functions
- Number of layers
- Number of neurons per layer
- Dropout rate
- Regularization (L2)
- Optimizer (e.g., SGD, Adam, RMSprop)
- Beta values for Adam optimizer (β1, β2)

- **Implementation**

The model was implemented using Python with libraries such as keras and tensorflow. 

- **Evaluation Metrics**

The model's performance was assessed using metrics like Mean Absolute Error (MAE) and Mean Average Procentual Error (MAPE). The progressions of the loss functions and prediction plots were also monitored.