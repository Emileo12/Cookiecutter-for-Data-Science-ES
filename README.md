# Cookiecuter Personal
![Logotipo del Proyecto](https://repository-images.githubusercontent.com/11407242/86598c80-80ab-11ea-95a2-df46cca01e67)
### Como utilizar y crear plantillas personalizadas con cookiecutter.

Al inicializar esta plantilla se creara un sistema de archivos estandarizados que le falicitara a usted en empezar un proyecto de ciencia de datos. 

Se inicializara un repositorio de git en local de manera automatica para que pueda trabajar en un sistema de versiones. Esencial para el trabajo en equipo y mayormente para su publicacion en la pagina de internet github.com.

Ademas de crear un ambiente virtual para la reproducibilidad del proyecto.



# Requirimientos

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    Esto puede ser instalado con `pip` o `conda` dependiendo cómo tú manejas tus paquetes de Python:

``` bash
pip install cookiecutter
```

o

``` bash
conda install -c conda-forge cookiecutter
```

## Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado escribe esto en la terminal:

```bash
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```

## Estructura de directorios y archivos resultantes

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
