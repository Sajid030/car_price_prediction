
# Car Price Prediction



## Table of Contents

 - [Demo](#demo)
 - [Overview](#overview)
 - [Motivation](#motivation)
 - [Installation](#installation)
 - [Deployement on Heroku](#deployement-on-heroku)
 - [Directory Tree](#directory-tree)
 - [Bug / Feature Request](#bug--feature-request)
 - [Future scope of project](#future-scope)









## Demo
Link:

![video](https://user-images.githubusercontent.com/126476034/227976477-9adf48a2-9bdd-4054-8f23-1d14dfeb5adc.gif)
https://user-images.githubusercontent.com/126476034/227976477-9adf48a2-9bdd-4054-8f23-1d14dfeb5adc.mp4
![video](https://i.imgur.com/zBCa20P.gif)

## Overview

This is a Flask web app which predicts price of cars.You need to fill out the details of your car and can see for how much price you can sell your car.
## Motivation

I started to learn Data Sience during second year of my college as this subject intrigued me quite a lot. So i started with Machine Learning first and came to know mathematics behind all supervised as well as unsupervised models. Finally it is important to work on application (real world application) to actually make a difference.
## Installation

The Code is written in Python 3.9.16. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

```bash
pip install -r requirements.txt
```
## Deployement on Heroku

Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.
## Directory Tree

```
├── static 
│   ├── css
│         ├── style.css
├── template
│   ├── index.html
├── Procfile
├── README.md
├── app.py
├── Prediction.ipynb
├── test.pkl
├── requirements.txt

```
## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/Sajid030/car_price_prediction/issues) here by including your search query and the expected result

## Future Scope

- Use multiple Algorithms
- Optimize Flask app.py
- Front-End 
