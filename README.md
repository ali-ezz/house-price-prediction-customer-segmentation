# House Price Prediction and Customer Segmentation Pipeline

A production-ready ML repository for regression and clustering workflows that predict house prices and segment customers using Python, Streamlit, and explainable model pipelines.

## Overview

This repository implements a complete machine learning workflow for:

- predicting house prices from real estate feature data
- segmenting customers based on demographic and transaction behavior

It includes data preparation, model training, evaluation, serialized artifacts, and a Streamlit interface for interactive prediction and analysis.

## Features

- Regression models for house price prediction using XGBoost, LightGBM, and Gradient Boosting
- Clustering workflows for customer segmentation using K-Means, DBSCAN, and hierarchical clustering
- Automated preprocessing with imputation, scaling, encoding, and feature engineering
- Serialized models and comparison metrics for reproducible evaluation
- Streamlit app for interactive prediction and batch CSV upload
- GitHub issue and PR templates for structured feedback

## Topics

- house-price-prediction
- customer-segmentation
- machine-learning
- streamlit
- regression
- clustering
- data-science

## Tech Stack

- Python 3.12+
- pandas
- numpy
- scikit-learn
- xgboost
- lightgbm
- streamlit
- plotly
- matplotlib
- seaborn
- joblib
- pytest

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ali-ezz/house-price-prediction-customer-segmentation.git
   cd house-price-prediction-customer-segmentation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Confirm the primary datasets exist:
   - `archive (2)/output.csv`
   - `clustering_customers.csv`

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Train or evaluate models using scripts:

```bash
python train_model.py
python train_model_full.py
python train_model_fast.py
python train_stacked.py
```

## Project Structure

- `README.md` — project overview and usage guide
- `LICENSE` — open source license
- `.gitignore` — ignored files for Python and environment artifacts
- `requirements.txt` — Python dependencies
- `.env.example` — environment variable template
- `CONTRIBUTING.md` — contribution guidelines
- `.github/` — GitHub issue and PR templates
- `tests/` — automated repository tests
- `app.py` — Streamlit application entry point
- `train_model.py` — model training pipeline
- `train_model_full.py` — extended training pipeline
- `train_model_fast.py` — faster training pipeline
- `train_stacked.py` — stacking pipeline
- `archive (2)/output.csv` — house price dataset
- `clustering_customers.csv` — customer segmentation dataset
- `models/` — model artifacts and results

## Results

Key artifacts stored in `models/` include:

- `models/model_comparison.csv`
- `models/processed_data.csv`
- `models/best_pipeline.pkl`

Use these artifacts to reproduce evaluation metrics and predictions.

## Future Improvements

- Add package structure under `src/` for cleaner imports
- Add API deployment support for production inference
- Add more structured model validation tests
- Add Docker packaging for reproducible environment setup

## License

This repository is licensed under the MIT License. See `LICENSE` for details.
