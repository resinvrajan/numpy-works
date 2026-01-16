import pandas as pd
df=pd.read_csv("ipl_case_study\ipl_data.csv")
print(df.shape)
print(df.head())
print(df.tail())
print(df.columns)
print(df.isnull().sum())
print(df.info())
df["match_id"].fillna(549,inplace=True)
df["season"].fillna(df["season"].mode()[0],inplace=True)
df["city"].fillna(df["city"].mode()[0],inplace=True)
df["team1"].fillna("unknown",inplace=True)
df["team2"].fillna("unknown",inplace=True)
df["winning_team"].fillna("unknown",inplace=True)
df["player_of_match"].fillna("unknown",inplace=True)
df["venue"].fillna(df["venue"].mode()[0],inplace=True)
round_score=round(df["runs_scored"].mean())
df["runs_scored"].fillna(round_score,inplace=True)
round_wiket=round(df["wickets"].mean())
df["wickets"].fillna(round_wiket,inplace=True)

print(df.isnull().sum())
# analysis

# matches per season
print("matches per season",df["season"].value_counts())
# top match count season
print("top match count season",df["season"].value_counts().idxmax())
# total match won by each team
print("total match won by each team",df["winning_team"].value_counts())
print("avg runs per season =======",df.groupby("season")["runs_scored"].mean())
print("venue wise match count======",df["venue"].value_counts())
print("venue-wise avg runs ====",df.groupby("venue")["runs_scored"].mean())
print("city wise match count====== \n",df["city"].value_counts())
print("city-wise avg runs ==== \n",df.groupby("city")["runs_scored"].mean())
print(" winning team with highest avg run===",df.groupby("winning_team")["runs_scored"].mean().idxmax())
print("top 3 venues teams====",df["venue"].value_counts().head(3))