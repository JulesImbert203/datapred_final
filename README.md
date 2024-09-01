Voilà le github final du projet d'informatique.

Collaborateurs :

Jules Imbert, Baptiste Auscher, Orel Mazor, Louise Philibert Nicole, Aria Chafai, Antoine Borel De La Roncière.


## Fonctionnement

### 1e étape : Récupération des données
On utilise l'api newsapi pour récupérer des articles de presses concernant certains mots-clés grâce [./data_acquisition/get_from_news_api.py](https://github.com/JulesImbert203/datapred_final/blob/main/data_acquisition/get_from_news_api.py)

### 2e étape : Tri des données
[./data_acquisition/corpus_acquisition.ipynb](https://github.com/JulesImbert203/datapred_final/blob/main/data_acquisition/corpus_acquisition.ipynb) utilise le code de l'étape précédente pour trouver des données pertinentes relatives au thème du projet (ici le prix des énergies sur différents marchés). [./data_acquisition/corpus_sorting.ipynb](https://github.com/JulesImbert203/datapred_final/blob/main/data_acquisition/corpus_sorting.ipynb) enregistre ces différents articles de façon organisé dans des fichiers CSV que l'on trouve dans [./data](https://github.com/JulesImbert203/datapred_final/blob/main/data).

### 3e étape : Traitement des données
Avec des modèles d'intelligence artificielle, les articles sont "pre-processed", c'est-à-dire résumés, dans [./data_processing/pre_processing.py](https://github.com/JulesImbert203/datapred_final/blob/main/data_processing/pre_processing.py), et ce nouveau corpus est ensuite enregistré dans [./data_processing/preprocessed_data](https://github.com/JulesImbert203/datapred_final/blob/main/data_processing/preprocessed_data). Finalement, on utilise des modèles d'analyse de sentiment pour analyser ces articles résumés, dans [./data_processing/processing.ipynb](https://github.com/JulesImbert203/datapred_final/blob/main/data_processing/processing.ipynb). On utilise ensuite ces analyses pour en tirer des graphes que l'on compare avec le cours du prix du kWh des énergies pour y lire une potentielle corrélation. Ces graphes sont tracés dans le fichier [./data_processing/graph.ipynb](https://github.com/JulesImbert203/datapred_final/blob/main/data_processing/graph.ipynb)
