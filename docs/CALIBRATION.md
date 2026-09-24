# Calibration RF et bilan de puissance

[Accueil](../README.md) · [Architecture](ARCHITECTURE.md)

## Ce que le logiciel calcule

Le code utilise une approximation affine de la réponse du détecteur :

```text
P_detecteur_dBm = P_ref_dBm + (V_detecteur − V_ref_detecteur) / pente_V_par_dB
G_net_dB = gain_LNA − perte_filtre − perte_câble − perte_commutateur
P_antenne_dBm = P_detecteur_dBm − G_net_dB
P_W = 10 ** ((P_antenne_dBm − 30) / 10)
```

Les dBm décrivent un niveau de puissance ; les dB décrivent un gain ou une perte. Retrancher un gain en dB à une puissance en dBm ramène le niveau à l’entrée de la chaîne.

## Exemple numérique pédagogique

Avec une référence à 2,10 V pour −40 dBm, une pente de −0,025 V/dB et une tension de 1,85 V :

- Variation : `(1,85 − 2,10) / (−0,025) = 10 dB`.
- Puissance au détecteur : `−40 + 10 = −30 dBm`.
- Pour un gain net hypothétique de 20 dB : `−30 − 20 = −50 dBm` au connecteur d’antenne.
- Cela représente `10⁻⁸ W`, soit 10 nW.

Ces valeurs illustrent les équations ; elles ne constituent pas une calibration du montage.

## Protocole proposé

1. Fixer le plan de référence et la fréquence de l’essai.
2. Appliquer des niveaux connus compatibles avec la chaîne, en tenant compte des atténuateurs et pertes.
3. Mesurer plusieurs couples puissance/tension dans le domaine exploitable.
4. Ajuster une droite et examiner les résidus, sans inclure les zones de saturation.
5. Déterminer le gain net de la chaîne pour chaque fréquence et configuration.
6. Tester des points distincts des points d’ajustement.
7. Archiver valeurs, incertitudes, instruments, date et conditions.

Éviter de compter deux fois les pertes : préciser si les puissances de référence sont données à l’entrée du détecteur ou à l’entrée de la chaîne complète.

## Fiche de calibration à renseigner

| Paramètre | Unité | Valeur mesurée |
|---|---|---|
| Fréquence | MHz | À renseigner |
| VREF ADC | V | À renseigner |
| Référence tension détecteur | V | À renseigner |
| Référence puissance détecteur | dBm | À renseigner |
| Pente détecteur | V/dB | À renseigner |
| Gain net de chaîne | dB | À renseigner |
| Domaine valide | dBm | À renseigner |
| Incertitude / méthode | Selon grandeur | À renseigner |

Le programme ne charge pas cette fiche automatiquement. Les paramètres doivent être saisis dans l’onglet **Calibration RF** ; conserver une copie des réglages avec l’essai.
