# M0_Brief_1

# Développer une Application Web d’Analyse de Sentiment Basée sur une API

## Description du projet

Ce projet consiste à **développer une application web d’analyse de sentiment** reposant sur une architecture client-serveur.  
L’application utilise le modèle **VADER (Valence Aware Dictionary and sEntiment Reasoner)** de la bibliothèque **NLTK**, permettant d’évaluer le sentiment global d’un texte (positif, neutre ou négatif).

Elle se compose de deux parties principales :
- Une **API** développée avec **FastAPI**, qui reçoit un texte et retourne un dictionnaire de scores de sentiment.
- Une **interface utilisateur** développée avec **Streamlit**, permettant d’envoyer le texte à l’API et d’afficher les résultats.

L’objectif est de concevoir une architecture claire, modulaire et réutilisable, séparant la logique de traitement des données de l’interface utilisateur.


## Technologies utilisées

- **Python 3.10+**
- **FastAPI** → création de l’API REST
- **Uvicorn** → serveur ASGI
- **Streamlit** → interface web
- **NLTK + VADER** → analyse de sentiment
- **Pydantic** → validation des données
- **Loguru** → journalisation


## Installation et préparation du modèle

L’installation comprend :
1. La **création d’un environnement virtuel Python** pour isoler le projet.  
2. L’**activation de l’environnement** en fonction du système d’exploitation.  
3. L’**installation des bibliothèques** nécessaires à l’aide du fichier `requirements.txt`.  
4. Le **téléchargement du lexique VADER** requis pour le fonctionnement du modèle NLTK.

Ces étapes garantissent la reproductibilité et la portabilité du projet.

## Objectif du projet

Créer une **application web fonctionnelle** intégrant un modèle d’analyse de sentiment.  
L’utilisateur saisit du texte dans une interface Streamlit, le texte est envoyé à l’API via une requête POST, l’API analyse le contenu à l’aide du modèle VADER et retourne les scores de polarité.  
Les résultats sont ensuite affichés dans l’interface utilisateur.

## Architecture de l’application

L’architecture repose sur deux modules principaux :
- **sentiment_api.py** : l’API FastAPI qui reçoit les textes et renvoie les scores d’analyse.  
- **streamlit_app.py** : l’application Streamlit pour la saisie et l’affichage des résultats.  

Un dossier **logs/** centralise les fichiers de journalisation, assurant un suivi complet des requêtes et des erreurs.

## L’analyseur de sentiment

Le modèle **VADER** analyse la polarité émotionnelle d’un texte en anglais.  
Il calcule quatre scores :
- **neg** : proportion de mots à connotation négative.  
- **neu** : proportion de mots neutres.  
- **pos** : proportion de mots positifs.  
- **compound** : score global compris entre -1 (négatif) et +1 (positif).

Ces mesures permettent d’évaluer de manière quantitative l’émotion exprimée dans un texte.  
Le score composé sert à déterminer le **sentiment global** du texte :  
- supérieur à +0.05 → sentiment positif  
- inférieur à -0.05 → sentiment négatif  
- entre les deux → sentiment neutre  


## Validation des données (Pydantic)

La validation des données est assurée par **Pydantic**, qui garantit que les requêtes envoyées à l’API respectent le format attendu.  
Un modèle de données simple définit un champ unique `texte` qui doit contenir une chaîne de caractères.  


## Journalisation (Loguru)

La **journalisation** permet de suivre l’activité de l’application et de diagnostiquer les erreurs.  
La bibliothèque **Loguru** enregistre :
- les textes analysés,  
- les résultats produits par l’analyse,  
- et les erreurs rencontrées lors du traitement.

Deux fichiers de logs distincts sont créés :
- `logs/sentiment_api.log` pour l’API FastAPI.  
- `logs/streamlit_app.log` pour l’application Streamlit.  

Un système de **rotation automatique des fichiers** empêche la saturation du disque et conserve un historique clair.


## Méthode d’analyse du sentiment

Le traitement du texte suit les étapes suivantes :
1. L’utilisateur saisit un texte dans l’interface Streamlit.  
2. Le texte est transmis à l’API FastAPI via une requête HTTP POST.  
3. L’API utilise **SentimentIntensityAnalyzer** pour calculer les quatre scores de polarité.  
4. Les résultats sont renvoyés au format JSON à l’interface Streamlit.  
5. Streamlit affiche les valeurs et interprète le score composé pour déterminer le sentiment global.  


## Interaction entre Streamlit et l’API

L’interface Streamlit communique avec l’API via la bibliothèque **requests**.  
Le texte saisi est envoyé en JSON, et les résultats sont extraits de la réponse HTTP.  
Les quatre scores (`neg`, `neu`, `pos`, `compound`) sont affichés, accompagnés d’une interprétation textuelle (Positif, Négatif ou Neutre).  
Un message d’information s’affiche en cas d’erreur ou d’absence de texte à analyser.


## Gestion des exceptions

La gestion des exceptions est assurée à deux niveaux :

### Côté Streamlit  
- Gestion des erreurs de connexion à l’API.  
- Information claire à l’utilisateur via des messages d’erreur.  
- Journalisation des anomalies détectées (requête invalide).  

### Côté FastAPI  
- Gestion des erreurs d’analyse ou de traitement.  
- Retour d’un code d’erreur HTTP adapté.  
- Enregistrement détaillé des exceptions dans les fichiers de logs.  

Cette double gestion garantit la **robustesse** et la **fiabilité** de l’application.


## Résultat attendu

L’application affiche :
- les quatre scores de polarité (négatif, neutre, positif, composé)  
- un **sentiment global** (Positif 😀, Négatif 🙁 ou Neutre 😐)  
- une indication visuelle claire pour l’utilisateur  
- des traces de logs pour le suivi technique.  


## Fichier `requirements.txt`

Le fichier `requirements.txt` contient l’ensemble des dépendances du projet :
- FastAPI  
- Uvicorn  
- Streamlit  
- NLTK  
- Requests  
- Loguru  
- Pydantic  
