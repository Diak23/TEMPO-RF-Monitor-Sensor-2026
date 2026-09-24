# Récupérer et contribuer au projet

[Retour à l’accueil](../README.md)

Dépôt : https://github.com/Diak23/-tude-et-r-alisation-d-un-capteur-d-onde-lectromagn-tique

## Récupérer les fichiers

```bash
git clone https://github.com/Diak23/-tude-et-r-alisation-d-un-capteur-d-onde-lectromagn-tique.git capteur-rf
cd capteur-rf
```

Suivre ensuite les instructions du README pour lancer la simulation.

## Préparer une modification

```bash
git switch -c amelioration-documentation
git status
git diff
```

Ajouter uniquement les fichiers voulus, les vérifier, puis créer un commit et une pull request. Utiliser l’authentification GitHub habituelle ; ne jamais placer un jeton dans le code, le README ou l’URL du dépôt.

## Configuration locale

Ne pas publier de clés, mots de passe, profils de navigateur, historiques de commandes ou captures réseau. Les nouvelles acquisitions restent dans `src/exports/`, exclu de Git. Vérifier les identifiants des appareils et les légendes avant de partager de nouveaux exemples.

Ce dépôt démarre avec un nouvel historique et une sélection de fichiers. Il ne reprend pas l’historique du dépôt de travail initial.
