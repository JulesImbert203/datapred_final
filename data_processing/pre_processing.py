import pandas as pd
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import numpy as np

# Text summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

df = pd.read_csv("../data/corpus_france_gas.csv")
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
df = df.sort_values(by=['date', 'time'])
df_cleaned = df.drop_duplicates(subset='body', keep='first')


# Function to summarize long article into small condensed texts that can be given as an input to the sentiment analysis function
def summarize(text_to_summarize, max_length=512):
    return summarizer(text_to_summarize, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

df_preprocessed = df_cleaned[['datetime', 'body']].copy()
df_preprocessed['summary'] = ''
df_preprocessed.reset_index(drop=True, inplace=True)

"""
def can_summarize(text, summarize_function):
    try:
        summarize_function(text)
        return True
    except:
        return False

def find_max_length(summarize_function, initial_text, max_length):
    low, high = 0, max_length
    while low <= high:
        mid = (low + high) // 2
        if can_summarize(initial_text[:mid], summarize_function):
            low = mid + 1
        else:
            high = mid - 1
    return high

initial_text = df_preprocessed['body'].iloc[0]

max_length = find_max_length(summarize, initial_text, len(initial_text))

print("Longueur maximale sans plantage:", max_length)
"""


# Fonction pour diviser et résumer le texte en morceaux
def split_and_summarize(body, max_length):
    n = len(body)
    if n <= max_length:
        return summarize(body, max_length)
    
    # Déterminer le nombre de morceaux
    p = max(1, n // max_length + 1)
    part_size = (n + p - 1) // p  # Calculer la taille des morceaux
    bodys = [body[i * part_size: min(n, (i + 1) * part_size)] for i in range(p)]
    
    # Résumer chaque morceau et concaténer les résumés
    pre_summaries = [summarize(part, max_length=200) for part in bodys]
    pre_summary = ' '.join(pre_summaries)
    
    # Résumer la concaténation des résumés sans dépassement
    if len(pre_summary) > max_length:
        return summarize(pre_summary[:max_length], max_length=200)
    return summarize(pre_summary, max_length=512)

calculated_max_length = 1023

# Mettre à jour la colonne 'summary' avec les résumés
leng = len(df_preprocessed)
for k in range(leng):
    body = df_preprocessed.iloc[k]['body']
    summary = split_and_summarize(body, max_length=calculated_max_length)
    df_preprocessed.at[k, 'summary'] = summary

print(df_preprocessed)

df_preprocessed.to_csv("preprocessed_data/preprocessed.csv", index=False)
