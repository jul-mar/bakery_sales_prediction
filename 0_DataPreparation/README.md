# Data Preparation


## Overview

In this folder we have created a subfolder for each feature we added. We also wrote skripts to merge and transform the data.

## Added features
We tied to find a lot of features that could help us improve the predictions. We created a folder for each feature in which we saved the skripts that we used to import/create the feature and transform the data in a way we could use it.
In the following the features are listed and explained:
- **01_Kreuzfahtrschiffe**: Did a cruise ship arrive in Kiel on this day yes/no. And if yes how many cruise ships did arrive on this day
- **02_Verbrauchspreisindex**: How was the inflation over the years
- **03_Heimspiele**: Was there a soccer game of Holstein Kiel at this day
- **04_Feiertage**: Was there a public Holiday at this day
- **06_Ferientage**: Dates of school holidays over the years
- **07_Wetter**: Here we cleaned up the weather data that was provided. Filled in missing values and one-hot encoded it.
- **08_Maerkte**: Dates of Christmas market and other markets during the years
- **09_Wochentage**: Weekdays were added as a feature 
- **10_Ostertag**: Easter days were added as extra feature
- **11_Silvester**: New Years Eve added as feature
- **12_Wettercode_Ersatz**: We filled in some missing data with data provided by public weather stations
- **13_Jahreszeiten**: Added the season as feature
- **14_Werktag**: Added in business days as features
- **15_Monat_und_zwischen_den_Jahren**: Months were added as feature and the days between christmas and New Years Eve

## Merging data
We discussed in the beginning how each feature should be stroucture (column with date followed by colums holding the feature informations). This allowed us to merge the data on the date colum.

## Data transformation
In the beginning we had the data in wide format as we tought we only need to predict the total revenue.
After we found out that we need to predict the revenues for each product grou we merged all data again in long fomrmat. This data and the scripts can be found in the folder 00_data.
We also one-hot-encoded several features. The scripts which we used can be found in the folders of the features

## Handling missing values
For the weather data we found some alternative souces that we used to fill the gaps. If only single days were missing we took values from the day or the year before.


