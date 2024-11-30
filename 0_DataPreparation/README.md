# Data Preparation

## Daten mergen
Im Moment sind alle Basisdaten gemerged. Zusätzlich sind die Anläufe der kreuzfahrtschiffe und die inflationsdaten eingefügt. Allerdings gibt es noch einige Dinge, welche wir ausbessern müssen:
- An manchen Tagen kommen 2 Schiffe an --> das sorgt für das Verdoppeln von Daten im df. Das muss noch gefixt werden (erledigt)
- Im Moment sind noch zu viele Infos über die Schiffe drinnen. Eigentlich reicht eine Spalte mit Kreuzfahrtschiff True/False (erledigt)
- für 2015/2016 fehlen noch kreuzfahrtdaten --> Bugfixing notwendig (erledigt)
- Wettercode muss bereinigt werden (one hot encoding)
- Datenaufbereitung von Kreutzfahrtschiffen im Unterordner und nicht im merge_all_data notebook (erledigt)
- Wochentage als Features hinzufügen (erledit)

Todo Julius:
- Ferien nur Schleswig-Holstein (erledigt)
- Temperatur binnen (erledigt)

