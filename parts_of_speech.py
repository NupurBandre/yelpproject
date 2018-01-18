from collections import Counter
from itertools import chain

import pandas as pd

from nltk import word_tokenize, pos_tag

df = pd.read_csv('testingxx.csv')


tok_and_tag = lambda x: pos_tag(word_tokenize(x))

df['lower_reviews'] = df['reviews'].apply(str.lower)
df['tagged_reviews'] = df['lower_reviews'].apply(tok_and_tag)

possible_tags = sorted(set(list(zip(*chain(*df['tagged_reviews'])))[1]))

def add_pos_with_zero_counts(counter, keys_to_add):
    for k in keys_to_add:
        counter[k] = counter.get(k, 0)
    return counter


# Detailed steps.
df['pos_counts'] = df['tagged_reviews'].apply(lambda x: Counter(list(zip(*x))[1]))
df['pos_counts_with_zero'] = df['pos_counts'].apply(lambda x: add_pos_with_zero_counts(x, possible_tags))
df['reviews_vector'] = df['pos_counts_with_zero'].apply(lambda x: [count for tag, count in sorted(x.most_common())])

# All in one.
df['reviews_vector'] = df['tagged_reviews'].apply(lambda x:
    [count for tag, count in sorted(
        add_pos_with_zero_counts(
            Counter(list(zip(*x))[1]), 
                    possible_tags).most_common()
         )
    ]
)

df2 = pd.DataFrame(df['reviews_vector'].tolist())
df2.columns = possible_tags
df2.to_csv('taggedOutput_test.csv')
