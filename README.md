# SongLongevityAnalysis
Analyze and predict how long songs stay in the top 3, 5, 10, or 20 rankings.

The dataset located at datasets\data.csv is sourced from: https://www.kaggle.com/datasets/edumucelli/spotifys-worldwide-daily-song-ranking?resource=download

Limitations: the dataset only has data covering Jan 1, 2017 to Jan 1, 2018. This means that the machine learning model does not have context for how songs were 
performing before and after the dates of collection. Songs popular outside of the collection dates will likely be seen as less popular than they truly were. Songs
popular in the middle of the collection date (or released after recently after Jan 1, 2017) will likely been seen as more popular than they truly were. This
will negatively affect the model.
