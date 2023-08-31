# SongLongevityAnalysis
Analyze and predict how long songs stay in the top 3, 5, 10, or 20 rankings.

The dataset used for this project is stored as a zip file in this repo. Extract the zip file to the datasets directory.

The dataset is sourced from: https://www.kaggle.com/datasets/edumucelli/spotifys-worldwide-daily-song-ranking?resource=download

## Limitations
The dataset only has data collected from Jan 1, 2017 to Jan 1, 2018. Thus, songs popular outside of the collection dates will 
likely be seen as less popular than they truly were, and songs popular in the middle of the collection date range (or released recently after 
Jan 1, 2017) will likely been seen as more popular than they truly were. This will impact the model, and will introduce bias.
