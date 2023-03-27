
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

![image](https://camo.githubusercontent.com/47328db8600bb9822cec8f33b53702d52fec47fcec08617840cb0523e6420f85/68747470733a2f2f696d6775722e636f6d2f743645656b496c)
![image](https://user-images.githubusercontent.com/126476034/226076070-286d9121-c3cf-4fab-b5fa-587b0613b6f0.png)
![image](https://user-images.githubusercontent.com/126476034/226075998-d89e7197-38f7-4f3c-8e49-6db5d94bc1d9.png)

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
