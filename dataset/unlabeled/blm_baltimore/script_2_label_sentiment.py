import pandas as pd
from Controller import FileController, DataNLP
from Lexicon.DepecheMood import DepecheMoodController
from Lexicon.EmoSenticNet import EmoSenticNetController
from Lexicon.NRC import NrcController

# NLP TOKEN
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df.drop(['text'], axis=1, inplace=True)
df = DataNLP.run(df)
FileController.save_df_to_csv("04-post-nlp-dataset.csv", df)

# CHECK SENTIMENT
df = pd.read_csv("04-post-nlp-dataset.csv", sep=",")
df = NrcController.run(df)

# REMOVE COLUMNS
df.rename(columns={"nrc_sentiment": "sentiment", "nrc_sentiment_count": "sentiment_count",
                   "nrc_sentiment_score": "sentiment_score", "created_at": "tweet_created_dt"}, inplace=True)
df = df[["tweet_text", "sentiment", "sentiment_count", "sentiment_score", "tweet_created_dt"]]
FileController.save_df_to_csv("05-post-sentiment-dataset.csv", df)
