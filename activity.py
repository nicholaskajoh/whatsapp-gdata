import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('whatsapp-group-data.csv', index_col=0)

df1 = df.groupby('date')['date'].count().reset_index(name="messages")
df2 = df1.sort_values('messages', ascending=False)

print("Busiest days")
print(df2.head(10))

print("\n" * 3)

print("Least busy days")
print(df2.tail(10).sort_values('messages'))