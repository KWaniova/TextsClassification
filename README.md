# TextsClassification
Project for the subject Natural Language Processing on Jagiellonian University

## Description

The project consists of comparing basic machine learning algorithms for text classification in Polish. In the project I used two deep learning models: A linear model and a model with convolutional layers, and two implementations of models from sklearn: LogisticRegression and RandomForest.
The models were trained on texts by 4 Polish authors: Adam Mickiewicz, Juliusz Słowacki, Henryk Sienkiewicz and Władysław Reymont. The texts were taken from [Wolne Lektury] (https://wolnelektury.pl/).

I used the nltk library to preprocess the text, and the TfidfVectorizer from sklearn to vectorise the text.

## Technologies

- Python 3.8
- Nltk
- Sklearn
- Pytorch
- Pandas
- Matplotlib
- Numpy

## Visualization
Model training and results are visualised in the jupyter project.ipynb notebook
The training and testing results for all models can be found in the results folder.