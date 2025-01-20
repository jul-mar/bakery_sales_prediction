# Model Definition and Evaluation

1. Model Selection

Various neural networks were considered, including Models with e.g. lag data, Regularisation or tuner models. After evaluation, V7 was selected due to its superior performance in capturing sales patterns.

2. Feature Engineering

Key features such as date, day of the week, promotional events and historical sales data were engineered to enhance model accuracy. To figure out the best Features for each Model, severel linear and not linear correlation tests were made in 2_BaselineModel complemented by manual tests.

3. Hyperparameter Tuning

Different Hyperparameter tuners were used. Then, systematic testing and developing intuition leaded to the best approach.

4. Implementation

The model was implemented using Python with libraries such as keras and tensorflow.

5. Evaluation Metrics

The model's performance was assessed using metrics like Mean Absolute Error (MAE) and Mean Average Procentual Error (MAPE).