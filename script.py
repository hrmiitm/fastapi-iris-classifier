
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np

iris = load_iris()
model = LogisticRegression(max_iter=1000)
model.fit(iris.data, iris.target)
class_names = ["setosa", "versicolor", "virginica"]

# Test with the unique sample
features = np.array([[5.1, 3.9, 5.1, 0.7]])
pred = int(model.predict(features)[0])
print(f"Prediction: {pred}")
print(f"Class name: {class_names[pred]}")
print(f"Result JSON: {{\"prediction\": {pred}, \"class_name\": \"{class_names[pred]}\"}}")
