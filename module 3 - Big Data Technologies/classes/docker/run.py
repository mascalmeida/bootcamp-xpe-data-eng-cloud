import pandas as pd

url = 'https://raw.githubusercontent.com/mascalmeida/colab_classes/main/datasets/water_potability.csv'

df = pd.read_csv(url)

print('\n', df.columns, '\n')

print(df.head(), '\n')

print(df.shape, '\n')