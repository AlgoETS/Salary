# Salary in Canada

En utilisant les donnée venant de 2023 2024 Salary Guide_PDF.pdf de randstak, nous allons créer un modèle de prédiction de salaire pour les différents métiers en fonction de la région, de l'expérience et du niveau d'étude.

## Objectif
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

   ```bash
   pip install -r requirements.txt
   ```

2. run pdf salary scraper

   ```bash
   python src/pdf.py
   python src/pdf_salary_scraper.py
   python stackoverflow_scraper.py
   ```

3. run jupyter notebook

   ```bash
   jupyter notebook
   ```

# Structure de projet ?

Cette structure s’inspire de Cookie Cutter Data Science

La qualité du code de science des données est une question d'exactitude et de reproductibilité.

```
├── .devcontainer      <- Fichiers de configuration pour VSCode
├── .github            <- Fichiers de configuration pour Github
├── README.md          <- The top-level README for developers using this project.
├── data               <- Données utilisées pour le projet
│   ├── pdf            <- Données venant du pdf
│   ├── pickle         <- Données venant du pdf transformées en pickle
|
├── docs               <- Documentation du projet et de la stratégie
│   ├── notebooks      <- Jupyter notebooks
│   ├── reports        <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── sandbox
│   ├── __init__.py    <- Makes src a Python module
│   ├── output         <- Output pdf de ta stratégie
│   ├── salary_exploration.ipynb        <- Jupyter de ta stratégie
│
├── src              <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module and les fonctions sont accessibles depuis n'importe quel fichier
│   ├── analyse.py                  <- Fichier contenant les fonctions liées à l'analyse
│   ├── config.py                   <- Fichier contenant les fonctions liées à la configuration
│   ├── pdf_salary_scraper.py       <- Fichier contenant les fonctions liées à la collecte des données pour le pdf
│   ├── pdf.py                      <- Fichier contenant les fonctions liées à la collecte des données pour le pdf
│   ├── stackoverflow_scraper.py    <- Fichier contenant les fonctions liées à la collecte des données pour stackoverflow
│   ├── test.py                     <- Fichier contenant les fonctions liées aux tests
│   ├── utils.py                    <- Fichier contenant les fonctions liées aux utils
├── web                <- Web du projet
├── wiki               <- Wiki du projet
│
├── .pre-commit-config.yaml <- Configuration de pre-commit
├── pyproject.toml          <- Configuration de poetry
├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`
├── sample.env              <- Fichier d'exemple pour le fichier .env
```

