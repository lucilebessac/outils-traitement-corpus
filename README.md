# outils-traitement-corpus
Création d'un corpus image/texte grâce à l'OCR.
Dans le cadre d'un cours intitulé "outils de traitement de corpus" j'ai choisi un corpus de référence et tenté de créer un corpus similaire pouvant servir à effectuer la même tâche.

## Corpus de référence
Mon corpus de référence : https://huggingface.co/datasets/katanaml-org/invoices-donut-data-v1

## À quel modèle le corpus de référence a-t-il servi
Le corpus de référence a servi à spécialiser le modèle Donut qui est un modèle de VDU (Visual Document Understanding) permettant d'extraire des données textuelles d'une image sans utiliser l'OCR et en utilisant des tranformers.

Sources :
https://arxiv.org/abs/2111.15664
https://huggingface.co/docs/transformers/model_doc/donut

## Méthode
Afin de créer un corpus similaire, j'ai scrappé le subreddit tumblr afin de récupérer des images contenant du texte.
Puis j'ai utilisé l'OCR pour extraire le contenu textuel des images

## Intérêt du corpus de référence
Pour une facture donnée, on peut imaginer prédire la catégorie socio prefessionnelle de l'acheteur, la langue qu'il parle, sa banque (puisque la facture contient l'IBAN)...

## Infos sur le corpus de référence
Les infos données sur Hugging Face sont les suivantes :
Ce corpus contient 500 factures au format image, annotées et nettoyées pour spécialiser le modèle Donut qui fait de l'extraction images -> texte sans OCR.

Les données ont été annotées et préparées par Katana ML qui à ce que j'ai compris est une boîte qui offre des services et solutions de déploiement et maintien des modèles d'apprentissage automatique en production.

Le corpus d'origine a été publié le 1e juin 2021. https://data.mendeley.com/datasets/tnj49gpmtz/2
Il contient 1000 factures générées automatiquement en python en se basant sur différents modèles de réelles factures électroniques à travers le monde.


