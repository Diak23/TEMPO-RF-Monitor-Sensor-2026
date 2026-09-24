# Démonstration

[Accueil](../README.md)

## Voir les sorties sans installer l’application

![Puissance simulée](images/simulation.png)

Le fichier [mesures.csv](../examples/simulation/mesures.csv) contient 826 enregistrements issus d’une session synthétique de deux bandes. Toutes les lignes portent `simulated=True`. Le graphique est reconstruit à partir de ce CSV ; il ne s’agit pas d’une capture de l’interface.

## Reproduire le résumé sans interface graphique

Depuis la racine, lancer `python scripts/analyse_simulation.py`. Le script utilise uniquement la bibliothèque standard de Python. Il lit l’exemple livré et refuse les lignes non simulées, les valeurs non finies et une énergie incompatible avec puissance × durée. Voir le [résumé calculé](RESULTATS_SIMULATION.md).

## Essai de 30 secondes

1. Installer les dépendances et lancer `python src/main.py` depuis la racine du projet.
2. Ouvrir **Sources / Acquisition** et sélectionner uniquement **Simulation RF**.
3. Choisir **Durée limitée**, durée **30 s**, période **100 ms**.
4. Cliquer sur **Démarrer** puis consulter **Tableau de bord** et **Mesures**.
5. Attendre l’arrêt et la confirmation de l’export.
6. Consulter **Graphiques** et les fichiers dans `src/exports/acquisition_<date>_<heure>/`.

Les sorties sont `mesures_capteur_rf.csv`, `synthese_capteur_rf.csv` et les graphiques PNG. Le graphique RSSI est vide si seule la simulation RF est activée.

Pour une nouvelle session indépendante, utiliser **Effacer** après l’arrêt ou relancer le programme. Le signal comporte un bruit aléatoire : les courbes ne sont pas identiques à chaque exécution.

## Sources physiques

Désactiver la simulation pour une session exclusivement expérimentale. Installer `requirements-hardware.txt` pour le MCP3208, configurer SPI et effectuer une calibration. Pour Wi-Fi et BLE, configurer les interfaces et outils correspondants.

Une session graphique est nécessaire ; un terminal distant sans affichage ne suffit pas. Les instructions ont été confrontées au code, mais l’interface et le matériel restent à vérifier sur la machine cible.

