# FBNotes
Get all comments from a Facebook Note/Post by using  official facebook-sdk

Visit 
http://developers.facebook.com/tools/explorer/ and get your Graph API Access Token for using Facebook Graph API Explorer .Just selelct all those permission which you want to use.

## 1. Getting Facebook Profile Name & ID :

'''python
import facebook
token = "YOUR_ACCESS_TOKEN"
account_data = graph.get_object("me")
print("Name:", account_data["name"])
print("Profile ID: ", account_data["id"])
'''
