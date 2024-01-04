# Graphene Python with FastAPI Template for Vercel Deployment of GraphQL API

This repository serves as a cookiecutter template for utilizing the Graphene Python package along with FastAPI and deploying the application to Vercel.

## Overview

This project provides a structured starting point for building GraphQL APIs using Graphene and FastAPI, and deploying the application to Vercel. It's designed to streamline the setup process and enable developers to quickly begin developing GraphQL APIs using these technologies.

## Features

- **Graphene:** Utilizes Graphene, a Python library for building GraphQL APIs.
- **FastAPI:** Integrates FastAPI, a modern web framework for building APIs with Python 3.7+.
- **Vercel Deployment:** Offers configuration files and guidelines to deploy the application to Vercel's platform.

## Requirements

Make sure you have the following installed before using this template:

- Python 3.7+
- [Cookiecutter](https://bit.ly/3H7iFVF)
- Pip (Python Package Installer) or make a virtural environment with [Pipenv](https://bit.ly/4aFnSS1)
- [Vercel CLI](https://bit.ly/3NRSlTg) (for deployment): A Vercel `JSON` file is ready to go in this cookiecutter

## Install with Cookiecutter

```bash
$ cookiecutter https://github.com/mrcartoonster/graphene_cookiecutter.git
```
## Structure

The project structure is organized as follows:

```
{{cookiecutter.project
├── app/
│   ├── main.py          # FastAPI main application file
│   ├── models.py        # GraphQL schema models
│   └── schema.py        # GraphQL schema definitions
├── .vercel/             # Vercel deployment configurations
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any enhancements or fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the maintainers of [CookieCutter](https://bit.ly/4aM6RWk), [Graphene](https://bit.ly/3vllakt), [FastAPI](https://bit.ly/3MUcJBi), and [Vercel](https://bit.ly/3TEGWdb) for their fantastic tools and documentation.
