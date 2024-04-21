# outils-traitement-corpus
Dépôt Git pour le cours d'outils de traitement de corpus

## Tâche à réaliser
Je souhaite créer un corpus permettant l'extraction de données textuelles d'un fichier image (type facture, devis, note de frais, carte d'identité, passeport, IBAN) ou tout autre image comportant du texte structuré.
Je considère cette tâche comme correspondant à de l'extraction d'information et la sous-tâche serait l'extraction de données textuelles depuis une image.

## Corpus répondant à la tâche
Le corpus suivant répond à cette tâche : https://huggingface.co/datasets/katanaml-org/invoices-donut-data-v1

## À quel type de prédiction peut servir le corpus ?
Pour une facture donnée, on peut imaginer prédire la catégorie socio prefessionnelle de l'acheteur, la langue qu'il parle, sa banque (puisque la facture contient l'IBAN)...
 
## À quel modèle il a servi ?
Ce corpus a servi à spécialiser le modèle Donut qui est un modèle de VDU (Visual Document Understanding) permettant d'extraire des données textuelles d'une image sans utiliser l'OCR et en utilisant des tranformers.
Je n'ai pas encore compris ce qu'était un transformer, j'essaierai de faire des recherches pour la prochaine fois.

OCR signifie Optical Character Recognition - soit reconnaissance optique de charactères

Sources :
https://arxiv.org/abs/2111.15664
https://huggingface.co/docs/transformers/model_doc/donut

## Infos sur le corpus
Les infos données sur Hugging Face sont les suivantes :
Ce corpus contient 500 factures au format image, annotées et nettoyées pour spécialiser le modèle Donut qui fait de l'extraction images -> texte sans OCR.

Les données ont été annotées et préparées par Katana ML qui à ce que j'ai compris est une boîte qui offre des services et solutions de déploiement et maintien des modèles d'apprentissage automatique en production.
Je ne sais pas si Katana ML a utilisé son outil Sparrow pour extraire et annoter les données, ou si ils en procfitent juste pour faire de la pub pour leur outil.

Le corpus d'origine a été publié le 1e juin 2021. https://data.mendeley.com/datasets/tnj49gpmtz/2
Il contient 1000 factures générées automatiquement en python en se basant sur différents modèles de réelles factures électroniques à travers le monde.


