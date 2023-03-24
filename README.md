# Web Crawler Challenge

[![Run Tests](https://github.com/luandadantas/jus-crawler-challenge/actions/workflows/run_tests.yaml/badge.svg)](https://github.com/luandadantas/jus-crawler-challenge/actions/workflows/run_tests.yaml)

Web Crawler that crawls/scrapes machine information at [Vultr](https://www.vultr.com/products/bare-metal/#pricing) and [Hostgator](https://www.hostgator.com/vps-hosting).

This project is the result of a technical challenge described in [this document](challenge_description.md).


## Pre-configuration

Ensure you have [Python](https://www.python.org/downloads/) installed on your machine. If you can run the following command without problems, it means that your machine already has python installed and will show you the python version it is using.

```bash
python3 --version
```

Python 3.10 was used for development, and it is recommended that you use this version or a newer one.

It´s also recommended to have a specific virtualenv for this project. You can create your virtual environment using the tool of your choice or create one by running:

```bash
python3 -m venv .venv
```

and then activating it
```bash
source .venv/bin/activate # macos or linux
```


## Run Locally
Follow the step by step to configure the project locally:

Clone the project

```bash
git clone https://github.com/luandadantas/jus-crawler-challenge.git
```

Go to the project directory

```bash
cd jus-crawler-challenge
```

Install dependencies. Be sure to activate your virtualenv before giving this command

```bash
pip install -r requirements.txt
```

Run the project

```bash
python3 main.py
```

## Running Tests

To run tests, run the following command

```bash
  python -m pytest tests/ --disable-socket
```


## Roadmap

- [x] Scrape data and collect content from Vultr
- [x] Write/Print on screen the data collected from Vultr
- [x] Previous step + save content from Vultr website in JSON file
- [x] Previous step + save content from Vultr website in CSV file
- [x] Create all previous steps for Hostgator website.


## Feedback

If you have any feedback, please reach out at ludanttas@gmail.com