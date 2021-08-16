import matplotlib.pyplot as plt
import seaborn as sns

def average_word_count(list_of_texts):
    """
    Returns the average word count of a list of texts.
    """
    total_count = 0
    for text in list_of_texts:
        text = text.replace("'", ' ')
        total_count += len(text.split(' '))
    average_count = total_count / len(list_of_texts)
    return average_count


# Criteria on which to split the database
Separe_on = 'Source'
# Storage where key is the database's label and the entry is avg word count
hist = {}

for label in set(Dataframe.loc[:, Separe_on]):
    mask = Dataframe.loc[:, Separe_on] == label
    sub_df = Dataframe.loc[mask, :]
    hist[label] = average_word_count(list(sub_df.loc[:, 'Text']))

plt.bar(x=[i for i in range(len(hist.keys()))],
        height=[hist[label] for label in hist],
        tick_label=[label for label in hist])
plt.ylabel('Average word count')
plt.title('Average word count by dataset')
plt.show()