# House Price Prediction & Customer Segmentation

A full-stack machine learning project for predicting house prices and segmenting customers using regression and clustering workflows.

## Overview

This repository contains a dual-purpose ML project that combines house price prediction and customer segmentation. It includes end-to-end data processing, model training, evaluation, serialization, and a Streamlit application for interactive prediction and analysis.

## Features

- House price regression using XGBoost, LightGBM, and Gradient Boosting
- Customer segmentation with K-Means, DBSCAN, and hierarchical clustering
- Data preprocessing with imputation, scaling, and feature engineering
- Training pipelines with model comparison and serialized artifacts
- Streamlit app for real-time price prediction and batch CSV processing
- Project documentation, issue templates, and a reusable repo checklist

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
   git clone https://github.com/ali-ezz/House-Price-Prediction-Customer-Segmentation.git
   cd House-Price-Prediction-Customer-Segmentation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify that the primary data files are present:
   - `archive (2)/output.csv`
   - `clustering_customers.csv`

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Or run training and evaluation scripts:

```bash
python train_model.py
python train_model_full.py
python train_model_fast.py
python train_stacked.py
```

## Project Structure

- `README.md` — project overview and usage
- `LICENSE` — open source license
- `.gitignore` — ignored files for Python and environment artifacts
- `requirements.txt` — Python dependencies
- `.env.example` — environment variable template
- `CONTRIBUTING.md` — contribution guidelines
- `.github/` — GitHub issue and PR templates
- `tests/` — automated repository sanity checks
- `app.py` — Streamlit application entry point
- `train_model.py` — model training pipeline
- `train_model_full.py` — extended training pipeline
- `train_model_fast.py` — faster training pipeline
- `train_stacked.py` — model stacking pipeline
- `archive (2)/output.csv` — house price dataset
- `clustering_customers.csv` — customer segmentation dataset
- `models/` — model artifacts and results

## Results

This project stores model outputs and comparison metrics under `models/`. Key artifacts include:

- `models/model_comparison.csv`
- `models/processed_data.csv`
- `models/best_pipeline.pkl`

Use these artifacts to compare model performance and reproduce predictions.

## Future Improvements

- Add structured tests for training pipelines and model scoring
- Refactor components into a `src/` package for cleaner imports
- Add a Docker setup for reproducible deployment
- Add a lightweight API endpoint for production inference

## License

This repository is licensed under the MIT License. See `LICENSE` for details.
