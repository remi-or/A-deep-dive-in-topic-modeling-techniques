# This snippet requires you to install Hugging Face's datasets module
from datasets import load_dataset
import pandas as pd

Dataframe = pd.DataFrame({})

questions = load_dataset('squad')['train']['question'][:3000]
Dataframe = Dataframe.append(pd.DataFrame({'Text' : questions, 'Source' : 'squad'}))

questions = load_dataset('hotpot_qa', 'distractor')['train']['question'][:3000]
Dataframe = Dataframe.append(pd.DataFrame({'Text' : questions, 'Source' : 'hotpot'}))

questions = load_dataset('eli5')['train_eli5']['title'][:3000]
Dataframe = Dataframe.append(pd.DataFrame({'Text' : questions, 'Source' : 'eli5'}))

questions = load_dataset('imdb')['train']['text'][:3000]
Dataframe = Dataframe.append(pd.DataFrame({'Text' : questions, 'Source' : 'imdb'}))

Dataframe = Dataframe.reset_index().drop(columns='index')