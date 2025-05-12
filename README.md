# Seattle Housing Price Prediction Model
Name: Jaylen Carrillo

Course: INST414 0202

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Predicting Seattle home prices using machine learning to support first-time buyers and inform real estate decisions.

I used a publicly available dataset from Kaggle:  

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

The notebook includes:
- Data loading and cleaning
- Feature engineering (e.g., price per square foot, bath-to-bed ratio)
- Exploratory data analysis
- Training and tuning of three models (Linear Regression, Ridge, Random Forest)
- Performance evaluation using R², MAE, and RMSE


Some reusable code for loading data, creating features, and training models is also included in the `housing_predictor/` folder. While the notebook runs everything from start to finish, these Python scripts are organized for future use in apps or other projects.

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
To fully reproduce the analysis:
1. Set up your environment using the instructions above
2. Open `notebooks/Sprint3_Housing_Modeling.ipynb`
3. Click **Kernel > Restart & Run All**

This will re-run the full pipeline, including data processing, feature creation, training, tuning, and evaluation. No manual edits are required. Results will be consistent if random seeds are not changed.

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

