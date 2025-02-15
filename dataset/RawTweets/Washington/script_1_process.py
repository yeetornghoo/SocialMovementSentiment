import pandas as pd
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection
'''
# LOAD AND PREPARE DATASET
df = pd.read_csv("_dataset/dataset.csv", sep=";")
df['tweet_text'] = df['text']

# EXCLUDE NONE ENGLISH TEXT
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("_dataset/01-post-translate-dataset.csv", df)
'''

# DATA CLEANING
#df = pd.read_csv("_dataset/01-post-translate-dataset.csv", sep=",")
df = pd.read_csv("_dataset/03-post-spelling-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("_dataset/02-post-cleaning-dataset.csv", df)

# SPELLING CORRECTION
df = pd.read_csv("_dataset/02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)

# REMOVE USELESS COLUMN
df = df[["tweet_id", "tweet_created_dt", "retweets", "favorites", "tweet_text"]]
df = df[df['tweet_text'].notna()]
FileController.save_df_to_csv("_dataset/03-post-spelling-dataset.csv", df)

# FILTER WORD OF TWEET
df = pd.read_csv("_dataset/03-post-spelling-dataset.csv", sep=",")
df['ttl_tweet_text_word'] = df['tweet_text'].str.split().str.len()
df = df.loc[(df['ttl_tweet_text_word'] > 2)]
df.drop(columns=['ttl_tweet_text_word'], inplace=True)

# SAVE FILE
FileController.save_df_to_csv("_dataset/final-dataset.csv", df)

# LOG
LogController.log("Execution of 'script_1_process.py' is completed.")
