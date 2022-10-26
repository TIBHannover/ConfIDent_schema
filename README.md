[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green.svg)](https://creativecommons.org/licenses/by/4.0/) 
![Build Status](https://github.com/TIBHannover/ConfIDent_schema/workflows/Build%20and%20test%20linkml-runtime/badge.svg)

# ConfIDent schema

This is a schema for the ConfIDent project that describes the necessary metadata requirements of academic events and event series.

## Website

* [https://TIBHannover.github.io/confident_schema](https://TIBHannover.github.io/ConfIDent_schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [confident_schema](src/confident_schema)
        * [schema](src/confident_schema/schema) -- LinkML schema (edit this)
* [datamodel](src/confident_schema/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
