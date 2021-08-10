# This snippet requires you to install Hugging Face's datasets module
from datasets import load_dataset
import pandas as pd

Dataframe = pd.DataFrame({})

questions = load_dataset('squad')['train']['question']
Dataframe = Dataframe.append(pd.DataFrame({'Question' : questions, 'Source' : 'squad'}))

questions = load_dataset('hotpot_qa', 'distractor')['train']['question']
Dataframe = Dataframe.append(pd.DataFrame({'Question' : questions, 'Source' : 'hotpot'}))

questions = load_dataset('eli5')['train_eli5']['title']
Dataframe = Dataframe.append(pd.DataFrame({'Question' : questions, 'Source' : 'eli5'}))

Dataframe = Dataframe.reset_index().drop(columns='index')