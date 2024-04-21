import praw
import os
import requests

# Initialisation de praw (wrapper de l'API reddit)
reddit = praw.Reddit(client_id="14JBbvpP01tPby97id6m4w",
                    client_secret="5ayqREao03PQKDMmxGTLtCVgaP6OcA",
                    user_agent="klmpost")

# Subreddit à scrapper
subreddit_name = "tumblr"
data_path = "../Data/Raw/Images"
# Dossier de stockage des images
if not os.path.exists(data_path):
    os.makedirs(data_path)

# Objet subreddit
subreddit = reddit.subreddit(subreddit_name)

print("En train de scrapper le subreddit :", subreddit_name)

# Pour chacun des 10 dernier posts
for post in subreddit.new(limit=100):
    # Si le post est une image
    if post.url.endswith(('.jpg', '.jpeg', '.png')):
        image_url = post.url
        # Récupère l'image
        image = requests.get(image_url).content
        # Sauvegarde l'image
        with open(os.path.join(data_path, f"{post.id}.jpg"), "wb") as f:
            f.write(image)
        print("Image du post", post.id, "enregistrée dans le fichier",post.id,".jpg")
print("Images enregistrées dans le dossier :", data_path)