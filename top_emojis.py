import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import emoji
import operator

df = pd.read_csv('whatsapp-group-data.csv', index_col=0)

emojis_dict = {}

for index, row in df.iterrows():
    for char in row['text']:
        if char in emoji.UNICODE_EMOJI:
            if char in emojis_dict:
                emojis_dict[char] += 1
            else:
                emojis_dict[char] = 1

emojis = sorted(emojis_dict.items(), key=operator.itemgetter(1), reverse=True)

for e in emojis[:10]:
    print(e[0], e[1])

# visualize
plot_data = np.array(emojis[:10])
labels = plot_data[:, 0]
sizes = plot_data[:, 1]
plt.axis("equal")
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Most used emojis")
plt.show()