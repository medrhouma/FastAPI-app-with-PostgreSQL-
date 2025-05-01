import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    
    # Trouver tous les éléments avec class="ind" (indentation niveau 0)
    elements = soup.find_all("td", class_="ind")
    
    # Filtrer uniquement ceux qui ont une indentation de 0 (width = 0)
    top_level_elements = [e for e in elements if e.get("width") == "0"]

    # Pour chaque élément de haut niveau, on récupère le commentaire associé
    comments = [e.find_next("span", class_="commtext") for e in top_level_elements]

    # Mots-clés à rechercher
    keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0}

    # Pour chaque commentaire, analyser le contenu
    for comment in comments:
        if comment:
            comment_text = comment.get_text().lower()
            words = [w.strip(".,/:;!@()[]{}") for w in comment_text.split()]
            for word in words:
                for key in keywords:
                    if word == key:
                        keywords[key] += 1

    # Affichage
    print(keywords)
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.title("Mentions of Programming Languages in HN Post")
    plt.show()

if __name__ == "__main__":
    main()
