import requests

def find_img():
    url = "https://commons.wikimedia.org/w/api.php"

    # Coordonnées géographiques de la boîte englobante de la France
    bbox = "-4.59235,41.380007,9.560016,51.148506"

    params = {
        "action": "query",
        "format": "json",
        "generator": "random",
        "prop": "imageinfo|coordinates",
        "iiprop": "url",
        "colimit": "1",
        "ggsbbox": bbox,
        "ggslimit": "1",
        "iiurlwidth": "500"
    }

    found_image = False

    while not found_image:
        response = requests.get(url, params=params)
        data = response.json()

        if "query" in data and "pages" in data["query"]:
            for page in data["query"]["pages"].values():
                if "coordinates" in page:
                    image = {
                        "title": page["title"],
                        "url": page["imageinfo"][0]["url"],
                        "lat": page["coordinates"][0]["lat"],
                        "lon": page["coordinates"][0]["lon"]
                    }
                    print(image)
                    found_image = True
                    return image

        if not found_image:
            print("No image found with coordinates, trying again...")

def download_img(image):
    url = image["url"]

    # téléchargement de l'image
    response = requests.get(url)
    if response.status_code == 200:
        with open("image.jpg", "wb") as f:
            f.write(response.content)
            print("Image téléchargée avec succès")
    else:
        print(response)
        print("Échec du téléchargement de l'image")
