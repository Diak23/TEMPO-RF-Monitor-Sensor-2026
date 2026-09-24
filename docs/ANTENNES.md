# Antennes : conception et caractérisation

[Accueil](../README.md) · [Matériel](MATERIEL.md)

## Objectif

Documenter les antennes des bandes ciblées, 868 MHz et 2,45 GHz, et relier leur adaptation au fonctionnement de la chaîne de réception. Les fichiers HFSS et les mesures VNA ne figurent pas encore dans cette édition du dépôt.

## Démarche à présenter

1. Définir la fréquence visée, le type d’antenne, l’alimentation et le plan de masse.
2. Documenter les dimensions, matériaux, frontières et ports du modèle électromagnétique.
3. Simuler l’adaptation et le rayonnement sur une plage couvrant la bande visée.
4. Calibrer le VNA au plan de référence choisi, mesurer l’antenne et exporter les données.
5. Comparer simulation et mesure en explicitant les différences de géométrie, connectique et environnement.

## Résultats à joindre

| Résultat | Présentation attendue | État du dépôt |
|---|---|---|
| Géométrie | Dessin coté, unités et matériau | À joindre |
| Adaptation | S11 en dB, fréquence du minimum, valeur à la fréquence cible | À joindre |
| Bande passante | Critère choisi et bornes fréquentielles | À joindre |
| Impédance | Partie réelle et imaginaire au plan de référence | À joindre |
| Rayonnement | Diagramme 3D et coupes avec axes et normalisation | À joindre |
| Gain et efficacité | Définitions et paramètres d’extraction | À joindre |
| Comparaison | Courbes simulation/mesure et conditions | À joindre |

Le minimum de S11 ne résume pas le gain ni l’efficacité. Éviter d’attribuer une variation du niveau reçu à la seule puissance de l’émetteur : orientation, polarisation et environnement influencent aussi la réception.

## Organisation proposée des futurs fichiers

Créer un dossier par bande, séparer modèles, mesures et figures, et accompagner chaque série d’un README précisant instruments, calibration, unités et date. Conserver les données sources avec les figures sélectionnées. Publier uniquement des résultats vérifiés ; aucun chiffre d’antenne n’est présenté ici comme déjà validé.
