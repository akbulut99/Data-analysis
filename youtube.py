import pandas as pd
youtube = pd.read_csv("USvideos.csv")
youtube.head(n=5)
youtube.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1,inplace=True)
len(youtube.columns)
len(youtube.index)
youtube["likes"].mean()
youtube["dislikes"].mean()
youtube[youtube["views"].max() == youtube["views"]]["title"].iloc[0]#en yüksek görüntülemeyi alan video bilgisi
youtube[youtube["views"].min()==youtube["views"]]["title"].iloc[0]#en düşük görüntülemeyi alan video bilgisi
youtube.groupby("category_id").mean()[["comment_count"]] #kategorilere göre yorum sayılarının ortalamasını bulduk
youtube["category_id"].value_counts()
def countTitleCount(title):
    return len(title)
youtube["title_length"] = youtube["title"].apply(countTitleCount)

def countTag(tags):
    tagList = tags.split("|")
    return len(tagList)
youtube["tag_count"] = youtube["tags"].apply(countTag) 
likelist = []
def likesAnddislikes(likes,dislikes):
    likesList = list()
    dislikesList = list()
    for key,value in likes.iteritems():
        likesList.append(value)
    for key,value in dislikes.iteritems():
        dislikesList.append(value)
    
    likeanddislikeratio = list()
    for like,dislike in zip(likesList,dislikesList): 
        if like + dislike == 0:
            likeanddislikeratio.append(0)
        else:
            likeanddislikeratio.append(like/(like + dislike))
    return likeanddislikeratio
        
youtube["likes_dislikes"] = likesAnddislikes(youtube["likes"],youtube["dislikes"]) 


