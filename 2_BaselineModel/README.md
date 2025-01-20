# Baseline Model

Es wurden für jede der 6 Warengruppe ein Modell erstellt, welches einen Stochastic Gradient Descent (SGD) Regressor zur Vorhersage der Umsätzen für die jeweilige Warengruppe implementiert. Die Kombination der Modelle dient als Baseline-Modell für die Umsatzprognose der Bäckerei.


- **Feature Selection**

Für jede der 6 Modelle wurden individuell die Features ausgewählt, die in der Kombination die besten Evaluationsmetriken (insbesondere MAPE) im Trainings und Validierungsdatensatz ergaben. Die Auswahl erfolgte anhand von Korrelationsmatrizen und Untersuchungen auf gegenseite Information (mutual information).


- **Implementation**

Zum Trainieren der 6 unterschiedlichen Modelle wurden nur die Daten herangezogen die für die entsprechende Warengruppe relevant sind.
Das Modelltraining erfolgte dann mit einem SGD-Regressor aus der Scikit-Learn Bibliothek. Hierbei wurde mit "invscaling" eine sich über die Zeit reduzierende Lernrate gewählt. 

- **Evaluation**

Die Modelle wurden anhand mehrerer Metriken evaluiert:

Mean Absolute Error (MAE): Misst die durchschnittliche absolute Abweichung
Mean Squared Error (MSE): Bestraft größere Abweichungen stärker
Mean Absolute Percentage Error (MAPE): Gibt die prozentuale Abweichung an
Adjusted R²: Berücksichtigt die Modellkomplexität bei der Bewertung der Vorhersagequalität

Zusätzlich wurden die Ergebnisse visuell durch einen Scatter Plot von tatsächlichen vs. vorhergesagten Werten dargestellt.

