import pandas as pd

df = pd.read_csv('whatsapp-group-data.csv', index_col=0)

first_msg = df.iloc[0]
last_msg = df.iloc[-1]
print("Number of messages from %s %s to %s %s: %s" \
        % (first_msg['date'], first_msg['time'], last_msg['date'], last_msg['time'], df.shape[0]))