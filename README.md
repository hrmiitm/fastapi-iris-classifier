---
title: Iris Classifier FastAPI
emoji: 🌸
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
---

# Iris Classifier FastAPI

A FastAPI app that classifies iris flowers using a Decision Tree classifier.

## Endpoints
- `GET /health` → `{"status": "ok"}`
- `GET /predict?sl=5.1&sw=3.9&pl=5.1&pw=0.7` → `{"prediction": 2, "class_name": "virginica"}`
