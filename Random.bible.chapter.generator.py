

response = requests.get(
    "https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-asv/books/isaiah/chapters/1/verses/1.json")
data = response.json()
print(data["text"])
