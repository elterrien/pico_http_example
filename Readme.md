# Exemple de requête HTTP avec MicroPython et Raspberry Pico W

Ce projet est un exemple de requête HTTP avec MicroPython et Raspberry Pico W.

## Prérequis

- [MicroPython](https://micropython.org/download/rp2-pico/) installé sur votre Raspberry Pico W
- [Thonny](https://thonny.org/) installé sur votre ordinateur pour éditer le code et le transférer sur votre Raspberry Pico W


## Description

Le script `main.py` exécute les actions suivantes :

- Connexion au réseau WiFi avec les identifiants renseignés dans le fichier `config.py`
- Téléchargement du package `urequests` pour effectuer des requêtes HTTP (il n'est pas installé par défaut)
- Définition des données dans la variable `data` à envoyer dans la requête HTTP 
- Requête HTTP POST pour envoyer des données sur la plateforme [https://rutilusdata.fr/](https://rutilusdata.fr/)
- Affichage du retour de la requête HTTP dans la console

