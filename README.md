# ConfIDent schema

This is a schema for the ConfIDent project that describes the necessary metadata requirements of academic events and event series.

## Website

* [https://TIBHannover.github.io/confident_schema](https://TIBHannover.github.io/confident_schema)

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
