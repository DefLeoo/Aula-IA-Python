import pandas as pl
import matplotlib.pyplot as plt

df = pl.read_csv('questionario.csv')

with open('questionario.txt', 'w') as f:
    df.to_string(f)