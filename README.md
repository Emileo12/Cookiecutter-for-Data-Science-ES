
# Cookiecutter for Data
![Project Logo](https://repository-images.githubusercontent.com/11407242/86598c80-80ab-11ea-95a2-df46cca01e67)

## How to Use and Create Custom Templates with Cookiecutter

When initializing this template, a standardized file system will be created to help you start a data science project.

A local Git repository will be automatically initialized so you can work in a version control system, which is essential for teamwork and especially for publishing on the internet, like on github.com.
Additionally, a virtual environment will be created for project reproducibility.

We hope you forget about the small details in your project and with this repository, you can focus on what's important in your project!

# Requirements

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    This can be installed with `pip` or `conda` depending on how you manage your Python packages:

```bash
pip install cookiecutter
```

or

```bash
conda install -c conda-forge cookiecutter
```

## Create a New Project

In the directory where you want to save your generated project, type this in the terminal:

```bash
cookiecutter https://github.com/Emileo12/Cookiecutter-for-Data-Science-ES
```
or
```bash
python3 -m cookiecutter https://github.com/Emileo12/Cookiecutter-for-Data-Science-ES
```

Then, you will be prompted to enter your project's name, author name, a brief description, options for which dependencies you want to install, and the Python version. You can also leave it as default by pressing Enter.

## Resulting Directory and File Structure

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so {{ cookiecutter.project_module_name }} can be imported.
    │
    └── {{ cookiecutter.project_module_name }}               <- Source code for use in this project.
        ├── __init__.py    <- Makes {{ cookiecutter.project_module_name }} a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py
