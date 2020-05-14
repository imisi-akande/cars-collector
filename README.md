# Scraping Cars data
<p align="center">
  <img src="./images/cars.png">
</p>

The aim of the project is to scrape car prices, statuses,  models, mileage and year

### Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Data](#data)
4. [Running the code](#running)
5. [Results](#results)

### Introduction<a name="introduction"></a>
In this repository, I will be scraping cars with its individual attributes. The aim of this 
project is to perform further analyses on the scraped data :

### Prerequisites<a name="prerequisites"></a>
*Steps to install*
- Run `python3 -m pip install --user virtualenv` to install virtualenv on MACOS or `py -m pip install --user virtualenv` on Windows
- Go to the project root directory and run `python3 -m venv cars_env` or `py -m venv cars_env` on Windows
- Run `source cars_env/bin/activate` to activate the virtual environment on MAC or `.\env\Scripts\activate` on Windows
- Run `pip install -r requirements.txt` to install used packages

---------------------------------------------------------------------------------------------------------------------
*Packages to install*
- virtualenv
- Scrapy

### Data<a name="data"></a>
scrape cars data

### Running the code<a name="running"></a>
- [`cars_crawler`] - This folder embeds the project
- [`spiders`] - This folder consists of a single spider(cars) which is the file that consists of the code that crawl the web.
*how to scrape the cars data*
- Run `scrapy crawl cars -o cars.csv -o cars.xml -o cars.json` to generate all files
at once.

### Results<a name="results"></a>
csv, json and xml files generated