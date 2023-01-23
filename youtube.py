import pandas as pd
youtube = pd.read_csv("USvideos.csv")
youtube.head(n=5)
youtube.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1,inplace=True)
len(youtube.columns)
len(youtube.index)
youtube["likes"].mean()
youtube["dislikes"].mean()
youtube[youtube["views"].max() == youtube["views"]]["title"].iloc[0]#en yüksek görüntülemeyi alan video bilgisi
b=youtube[youtube["views"].min()==youtube["views"]]["title"].iloc[0]#en düşük görüntülemeyi alan video bilgisi
youtube.groupby("category_id").mean()[["comment_count"]] #kategorilere göre yorum sayılarının ortalamasını bulduk