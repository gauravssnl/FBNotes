# FBNotes
Get all comments from a Facebook Note/Post by using  official facebook-sdk

Visit 
http://developers.facebook.com/tools/explorer/ and get your Graph API Access Token for using Facebook Graph API Explorer .Just selelct all those permission which you want to use.

## 1. Getting Facebook Profile Name & ID :

```python
import facebook
token = "YOUR_ACCESS_TOKEN"
account_data = graph.get_object("me")
print("Name:", account_data["name"])
print("Profile ID: ", account_data["id"])
```

## 2. Selecting Facebook Note/Post & Getting its post-id

```python
posts = graph.get_object("me/feed?since=10 February 2017 & until=11 February 2017")
note_data = posts["data"][0]
print("Post/Note Title: ",note_data["message"])
note_postid = note_data["id"]
print("Post/ Note ID: ", note_postid)
```

## 3. Getting Comments & total number of comments

```python
# get comment data . Not all comments will be returned by facebook API
comments_data = graph.get_object(note_postid + "/comments")
# get total number of comments
comments_data = graph.get_object(note_postid + "?fields=comments.summary(true)")
comments_count = comments_data["comments"]["summary"]["total_count"]
print("Post/Note Comments count: ", comments_count) 
```

## 4. Getting total comments on Facebook Note/Post

```python
comments_data = graph.get_object(note_postid + "/comments?limit=" + str(comments_count))
cc = 0
print("No.","\t", "Comment")
for comment in comments_data["data"]:
 print(cc," ", comment["message"])
 cc += 1
```
