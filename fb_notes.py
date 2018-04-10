import facebook


token = "YOUR_ACCESS_TOKEN"
graph = facebook.GraphAPI(token)
account_data = graph.get_object("me")
print("Name:", account_data["name"])
print("Profile ID: ", account_data["id"])
print("-"*70)
# get post or note  details & post-id
# I want to find post/note created on 10th February 2017 . Modify this as per your need.
# you need not use this if you know your post/note post-id .
posts = graph.get_object("me/feed?since=10 February 2017 & until=11 February 2017")
#print(posts)
#print("-"*70)

# my note  data is at index 0 in posts variable. 
note_data = posts["data"][0]
print("Post/Note Title: ",note_data["message"])
print("-"*70)

# Now, we need to get the note's post-id
# if you have post-id , you can directly use it
# complete post id is actually combination of unique profile-id + post-id (check last numerical part of facebook notes URL)   
note_postid = note_data["id"]
print("Post/ Note ID: ", note_postid)
print("-"*70)

# get comment data . Not all comments will be returned by facebook API
comments_data = graph.get_object(note_postid + "/comments")
#print(comments_data)
#print("-"*70)

# get total number of comments
comments_data = graph.get_object(note_postid + "?fields=comments.summary(true)")
print(comments_data)
print("-"*70)
comments_count = comments_data["comments"]["summary"]["total_count"]
print("Post/Note Comments count: ", comments_count) 
print("-"*70)

#  if we want to fetch total number comments, we have to specify it as limit, otherwise Facebbook API will return less number of comments.
comments_data = graph.get_object(note_postid + "/comments?limit=" + str(comments_count))
#print(comments_data)
#print("-"*70)

# print each comment in different lines
cc = 0
print("No.","\t", "Comment")
for comment in comments_data["data"]:
	print(cc," ", comment["message"])
	cc += 1
print("-" * 70)
# save comments in a file
with open("comments_data.txt", "w") as f:
	data = ""
	for comment in comments_data["data"]:
		data += comment["message"] +"\n"
	f.write(data)
	print("Comments data written to file")

