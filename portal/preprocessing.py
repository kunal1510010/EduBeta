import pandas as pd


def read(filename):
    try:
        data =pd.read_csv(filename)
        print(data.head())
    except:
        print('something not working')
