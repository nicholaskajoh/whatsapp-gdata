import pandas as pd

df = pd.read_csv('whatsapp-group-data.csv', index_col=0)

longest_message = df.iloc[0]
longest_message_length = len(longest_message['text'])

for index, row in df.iterrows():
    if len(row['text']) > longest_message_length:
        longest_message_length = len(row['text'])
        longest_message = row

words_count = len(longest_message['text'].split(' '))
longest_message_text = longest_message['text'][:280] + "..." \
                        if len(longest_message['text']) > 280 else longest_message['text']
o = "The longest message, made up of %s words was sent by %s at %s %s. It says: \"%s\""
print(o % (
    words_count,
    longest_message['user'],
    longest_message['date'],
    longest_message['time'],
    longest_message_text
))