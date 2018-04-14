import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('whatsapp-group-data.csv', index_col=0)

df1 = df.groupby('user')['user'].count().reset_index(name="messages")
df2 = df1.sort_values('messages', ascending=False)

print("Top 10 talkertives")
print(df2.head(10))

print("\n" * 3)

print("The quiet ones")
print(df2.tail(10).sort_values('messages'))

# visualize with a bar chart
df3 = df2.head(25).sort_values('user')
indices = np.arange(df3.shape[0])
labels = df3['user'].values.tolist()
plt.bar(indices, df3['messages'].values.tolist())
plt.xlabel('People', fontsize=10)
plt.ylabel('No. of messages', fontsize=10)
plt.xticks(indices, labels, fontsize=10, rotation=90)
plt.title('Meet the talkertives')
plt.tight_layout()
plt.show()