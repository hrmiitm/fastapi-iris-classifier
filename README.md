---
title: Iris Classifier FastAPI
emoji: 🌸
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
---

# Iris Classifier FastAPI

A FastAPI app that classifies iris flowers using a Logistic Regression classifier.

## Endpoints
- `GET /health` → `{"status": "ok"}`
- `GET /predict?sl=5.1&sw=3.9&pl=5.1&pw=0.7` → `{"prediction": 1, "class_name": "versicolor"}`
