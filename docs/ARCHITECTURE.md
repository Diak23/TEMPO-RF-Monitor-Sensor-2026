# Architecture et limites

[Accueil](../README.md)

La voie analogique suit la chaîne **antenne → filtre → LNA → détecteur RF → MCP3208 → Raspberry Pi**. Les pilotes Wi-Fi et BLE constituent une voie numérique complémentaire.

| Calcul présent dans le code | Interprétation |
|---|---|
| `V = code × VREF / 4095` | Convention ADC utilisée dans le logiciel |
| `P_detecteur = P_ref + (V − V_ref) / pente` | Conversion calibrée, pente en V/dB |
| `G_net = gain_LNA − pertes` | Bilan en dB dépendant du montage et de la fréquence |
| `P_antenne = P_detecteur − G_net` | Estimation en dBm au connecteur d’antenne |
| `P_W = 10 ** ((P_dBm − 30) / 10)` | Conversion en watts |
| `E = somme(P_W × durée_s)` | Énergie RF estimée selon les durées retenues |

Les réglages par défaut ne sont pas une calibration mesurée. Vérifier dynamique, saturation, gains, pertes et réponse temporelle avec le matériel réel.

Le RSSI Wi-Fi décrit la liaison active, pas l’ensemble des émissions environnantes. Le programme utilise la période configurée pour estimer l’énergie RF/Wi-Fi ; elle peut différer du temps réellement écoulé et ne mesure pas le temps d’émission des paquets.

Pour BLE, la durée est approximée à partir de la longueur avec une hypothèse à 1 Mbit/s. Les pertes de capture, canaux et variantes de PHY limitent l’interprétation. Les catégories Apple/AirPods/iBeacon reposent sur des heuristiques et ne garantissent pas l’identité d’un appareil.

Ne pas interpréter une somme de sources qui se recouvrent, ou qui mélangent simulation et mesures, comme une exposition totale. Les alertes sont des seuils configurables, pas une évaluation sanitaire. Aucune mesure d’énergie absorbée par une personne n’est réalisée.

Conserver les réglages, la configuration matérielle et les conditions de chaque essai. Le CSV marque chaque ligne par `simulated` ; la synthèse ne remplace pas une fiche de calibration.

