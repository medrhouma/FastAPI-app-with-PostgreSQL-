    # 🎮 FastAPI Quiz App with PostgreSQL

Ce projet est une application web de quiz développée avec **FastAPI**, **SQLAlchemy** et une base de données **PostgreSQL**. Elle permet d’ajouter des questions avec des choix, et de les consulter via une API REST.

---

## 🚀 Stack utilisée

- 🔧 FastAPI  
- 🗃️ PostgreSQL  
- 🧠 SQLAlchemy  
- ⚙️ Uvicorn  
- 📦 Pydantic  

---

## ⚙️ Installation

### 1. Créer un environnement virtuel

```bash
python -m venv myenv
```

### 2. L’activer

#### Sous Windows :
```bash
.\myenv\Scriptsctivate
```

#### Sous macOS/Linux :
```bash
source myenv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données PostgreSQL

Créer une base de données PostgreSQL et renseigner l’URL de connexion dans un fichier `.env` :

```
DATABASE_URL=postgresql://username:password@localhost:5432/nom_de_la_base
```

### 5. Lancer l’application

```bash
uvicorn main:app --reload
```

### 6. Accéder à la documentation interactive

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

# 📄 Hacker News Job Scraper

Un projet Python simple pour **scraper les offres d’emploi** postées dans les discussions *Ask HN: Who is hiring?* de Hacker News, extraire les commentaires, analyser les technologies mentionnées, et les visualiser avec un graphique.

---

## 📦 Fonctionnalités

- 📥 Récupération des commentaires principaux (niveau d’indentation 0)  
- 🧹 Nettoyage et extraction du texte brut  
- 🔍 Analyse des technologies mentionnées (Python, JavaScript, etc.)  
- 📊 Affichage des résultats dans un graphique avec **Matplotlib**

---

## 🧰 Prérequis

- Python 3.7 ou supérieur  
- Accès à Internet

---

## 👨‍💻 Auteur

- **Mohamed Rhouma**  
- Étudiant à l’ISET Tozeur  
- [🔗 LinkedIn](https://www.linkedin.com/in/rhouma-mohamed-6291b02b4)  
- [💻 GitHub](https://github.com/medrhouma)

    
