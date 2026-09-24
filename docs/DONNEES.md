# Dictionnaire des données

[Accueil](../README.md) · [Exemple simulé](RESULTATS_SIMULATION.md)

Les CSV de mesures utilisent UTF-8, un séparateur `;` et le point comme séparateur décimal. Une cellule vide représente une grandeur absente pour cette source, pas une valeur nulle.

| Champ | Unité / type | Interprétation |
|---|---|---|
| timestamp_epoch | s | Horodatage Unix de création de l’enregistrement |
| elapsed_s | s | Temps relatif depuis le démarrage de l’acquisition |
| source | Texte | Simulation RF, MCP3208, Wi-Fi ou BLE Sniffer |
| technology | Texte | Étiquette de source ou classification indicative |
| band | Texte | Bande associée ; le libellé Wi-Fi ne prouve pas le canal utilisé |
| device | Texte | Voie RF, interface ou identifiant BLE |
| rssi_dbm | dBm | RSSI rapporté, lorsqu’il existe |
| adc_code | Entier | Code ADC, réel ou simulé selon simulated |
| voltage_v | V | Tension du détecteur, réelle ou simulée |
| power_detector_dbm | dBm | Puissance calculée au détecteur |
| power_antenna_dbm | dBm | Estimation antenne pour RF ; RSSI recopié pour les sources numériques |
| power_w | W | Conversion de la puissance retenue |
| duration_s | s | Durée utilisée dans le calcul d’énergie |
| energy_j | J | Puissance × durée pour l’enregistrement |
| cumulative_energy_j | J | Cumul propre au couple source/voie ou appareil |
| packet_length_bytes | Octets | Longueur disponible dans la capture BLE |
| pdu_type | Texte | Type de PDU disponible dans la capture |
| channel | Entier | Canal disponible dans la capture BLE |
| alert_level | Texte | VERT, ORANGE ou ROUGE selon les seuils logiciels |
| simulated | Booléen | True pour une donnée synthétique, False pour une observation physique |

## Interprétation temporelle

Pour RF/Wi-Fi, `duration_s` est la période configurée. Elle n’est pas nécessairement égale au temps entre deux points ni à une durée d’émission. Pour BLE, elle est estimée depuis la longueur avec une hypothèse de débit. Le temps CPU, les mises à jour du récepteur et les pertes de capture limitent ces approximations.

Le pilote BLE possède un horodatage de capture, mais l’enregistrement actuel utilise l’heure de traitement. Ne pas assimiler ces horodatages sans analyser le délai de traitement.

## Moyennes et cumuls

Pour une moyenne de puissance linéaire à poids égaux, convertir les niveaux en watts, faire la moyenne, puis revenir en dBm. Si les durées diffèrent, une moyenne temporelle nécessite une pondération. La moyenne arithmétique des dBm n’est pas la moyenne linéaire de puissance.

Ne pas sommer entre elles des valeurs déjà cumulées. Pour l’énergie d’une voie, sommer les contributions `energy_j`. Ne pas fusionner sans justification des sources couvrant le même signal.

## Partage

Les captures réelles peuvent contenir des identifiants d’appareils. Anonymiser les CSV et contrôler aussi les graphiques qui les reprennent avant publication. L’exemple livré contient uniquement des voies simulées.
