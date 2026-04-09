from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np

app = FastAPI(title="Iris Classifier API")

# Allow browser clients to call the API from different origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Train model at startup
iris = load_iris()
model = LogisticRegression(max_iter=1000)
model.fit(iris.data, iris.target)
class_names = ["setosa", "versicolor", "virginica"]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/predict")
async def predict(sl: float, sw: float, pl: float, pw: float):
    features = np.array([[sl, sw, pl, pw]])
    pred = int(model.predict(features)[0])
    return {"prediction": pred, "class_name": class_names[pred]}
