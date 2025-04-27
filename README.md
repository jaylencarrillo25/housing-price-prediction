# Seattle Housing Price Prediction Model

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Predicting Seattle home prices using machine learning to support first-time buyers and inform real estate decisions.

Dataset used:

https://www.kaggle.com/datasets/samuelcortinhas/house-price-prediction-seattle 

## Dependencies
This project requires the following Python libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- jupyter
- joblib

## Setting Up the Environment
1. Clone the repository

`git clone https://github.com/jaylencarrillo25/housing-price-prediction.git`

`cd housing-price-prediction`

2. Install all dependencies by running

`pip install -r requirements.txt`

3. Launch Jupyter Notebook

`jupyter notebook`

## Running the Data Processing Pipeline
1. Open Sprint3_Housing_Modeling.ipynb in Jupyter Notebook.
2. Run all cells by clicking Kernel → Restart & Run All.
3. The notebook will automatically load the data, preprocess it, and prepare it for model training.

## Evaluating Models
- The following machine learning models are trained and evaluated within the notebook:
 - Linear Regression
 - Ridge Regression
 - Random Forest Regressor

- Evaluation metrics calculated for each model include:
 - Root Mean Squared Error (RMSE)
 - Mean Absolute Error (MAE)
 - R² score

- Model performances are printed and compared at the end of the notebook.

## Reproducing Results
- After setting up the environment, open Sprint3_Housing_Modeling.ipynb and select Kernel → Restart & Run All.
- This will fully rerun the preprocessing, model training, evaluation, and generate all results automatically.
- No manual intervention is needed.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         housing_predictor and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── housing_predictor   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes housing_predictor a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

