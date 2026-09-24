# Guide d’utilisation

[Accueil](../README.md) · [Démonstration](DEMONSTRATION.md)

## Choisir son parcours

| Besoin | Parcours |
|---|---|
| Voir le fonctionnement sans installation | Lire la démonstration et les résultats simulés |
| Explorer les données sans affichage graphique | Lancer `python scripts/analyse_simulation.py` |
| Tester l’interface sans matériel | Installer requirements.txt et choisir Simulation RF |
| Acquérir avec le montage | Configurer le matériel, les outils et la calibration |

## Onglets

| Onglet | Usage |
|---|---|
| Tableau de bord | Dernière valeur par source, état et cumul |
| Sources / Acquisition | Sources, interfaces, période, limites et seuils |
| Calibration RF | Paramètres de conversion et bilan de gain |
| Mesures | Enregistrements et marqueur de simulation |
| Appareils BLE | Regroupement indicatif des observations par appareil |
| Graphiques | Sélection et tracé des grandeurs |
| Journal | Événements, erreurs et destination des exports |

## Procédure

Démarrer par une simulation seule. Pour les mesures physiques, activer ensuite une source à la fois et vérifier que ses résultats correspondent à l’instrument ou au signal attendu. Documenter chaque essai avec la [fiche proposée](templates/FICHE_ESSAI.md).

Cliquer sur **Arrêter et sauvegarder** pour finir un essai manuel. Fermer directement la fenêtre ne constitue pas une commande de sauvegarde. Après un essai, utiliser **Effacer** ou redémarrer l’application avant une session indépendante.

## Dépannage

| Symptôme | Contrôle utile |
|---|---|
| Erreur Tkinter | Présence de Tkinter pour le Python utilisé |
| Erreur DISPLAY | Session graphique disponible |
| Erreur SPI | Simulation désactivée intentionnellement ? ADC, accès SPI et spidev configurés ? |
| RSSI Wi-Fi absent | Interface correcte, connexion active et commande iw disponible |
| Capture BLE vide | Interface tshark, extension sniffer, permissions et champs disponibles |
| Graphique RSSI vide en simulation RF | Attendu : cette simulation produit une puissance RF, pas un RSSI |
| Énergie inattendue | Durée retenue, calibration, sources simultanées et ancien cumul |
| Identification BLE surprenante | Classification heuristique à confirmer sur les champs bruts |

Les exports sont écrits sous `src/exports/`. Ils ne sont pas ajoutés automatiquement au dépôt. La simulation ne nécessite aucun mot de passe Wi-Fi dans le code.
