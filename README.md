# 🎬 MovieGraph

MovieGraph is a graph-powered movie discovery and recommendation web application built with **Python, Flask, CognoDB, Cypher, HTML, CSS, and JavaScript**.

The application allows users to search and explore movies, view movie information and relationships, visualize a movie knowledge graph, and discover related movies through graph-based recommendations.

---

## ✨ Features

* 🔎 Movie search
* 🎬 Movie discovery
* ⭐ Movie ratings and release years
* 🎭 Actor information
* 🎥 Director information
* 🏷️ Genre information
* 🕸️ Interactive movie knowledge graph
* 🔗 Graph-based movie recommendations
* 📊 Recommendation scoring
* 🔄 Multi-hop graph traversal
* 🌐 Flask REST-style API
* 🗄️ CognoDB graph database
* 🎨 Interactive web interface
* 📱 Responsive UI

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask
* Neo4j Python Driver

### Database

* CognoDB
* Cypher / openCypher

### Frontend

* HTML5
* CSS3
* JavaScript
* Cytoscape.js

---

## 🧠 Graph Data Model

MovieGraph represents movies and their relationships as a graph.

### Nodes

```text
Movie
Actor
Director
Genre
```

### Relationships

```text
Actor ── ACTED_IN ──> Movie

Director ── DIRECTED ──> Movie

Movie ── HAS_GENRE ──> Genre
```

Example:

```text
Leonardo DiCaprio
        │
     ACTED_IN
        │
        ▼
    Inception
        │
    HAS_GENRE
        │
        ▼
      Sci-Fi
```

---

## 💡 Why a Graph Database?

Movie recommendations are highly relationship-oriented.

A movie can be connected to another movie through:

* Shared actors
* Shared genres
* Shared directors
* Multiple relationship paths

For example:

```text
Inception
    │
    ▼
Actor
    │
    ▼
Related Movie
```

or:

```text
Inception
    │
    ▼
Genre
    │
    ▼
Related Movie
```

A graph database makes these relationships natural to model and allows the application to traverse connected entities directly.

This is particularly useful for multi-hop recommendation queries where a movie can be connected to another movie through one or more intermediate nodes.

---

## 🎯 Recommendation Logic

MovieGraph uses graph relationships to calculate recommendation scores.

The recommendation score is based on shared relationships such as:

```text
Shared Actors × 3
+
Shared Genres × 2
```

For example:

```text
Movie A

2 shared actors
1 shared genre

Score =
(2 × 3) + (1 × 2)

Score = 8
```

Movies with stronger graph relationships receive higher recommendation scores.

---

## 🕸️ Knowledge Graph Visualization

The movie details page contains an interactive graph visualization.

The graph can show connections between:

```text
Movie
 ├── Actor
 ├── Director
 └── Genre
```

This allows users to understand the relationships behind the recommendation system instead of only receiving a list of recommended movies.

---

## 🔄 Multi-Hop Traversal

MovieGraph supports relationship traversal such as:

```text
Movie
  ↓
Actor
  ↓
Related Movie
```

and:

```text
Movie
  ↓
Genre
  ↓
Related Movie
```

These graph paths allow the recommendation system to discover related movies through connected entities.

---

## 📁 Project Structure

```text
moviegraph/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── queries.py
│   ├── seed.py
│   ├── test_queries.py
│   └── mock_data.py
│
├── templates/
│   ├── index.html
│   ├── movie.html
│   └── 404.html
│
└── static/
    ├── style.css
    ├── script.js
    └── movie.js
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd moviegraph
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
MOCK_MODE=false

COGNODB_URI=your_cognodb_uri
COGNODB_USERNAME=your_username
COGNODB_PASSWORD=your_password
```

**Never commit your `.env` file or database credentials to GitHub.**

---

## 🌱 Seed the Database

After configuring the CognoDB connection:

```powershell
python -m database.seed
```

This creates the required movie nodes and relationships.

---

## 🧪 Test Database Queries

Run:

```powershell
python -m database.test_queries
```

This verifies that the application can communicate with the graph database and retrieve movie relationships.

---

## ▶️ Run the Application

Start Flask:

```powershell
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### All Movies

```text
GET /api/movies
```

### Search Movies

```text
GET /api/movies/search?q=Inception
```

### Movie Details

```text
GET /api/movies/Inception
```

### Movie Recommendations

```text
GET /api/movies/Inception/recommendations
```

### Movie Graph

```text
GET /api/movies/Inception/graph
```

### Health Check

```text
GET /health
```

---

## 🧾 Example Cypher Query

Example shared-actor traversal:

```cypher
MATCH (m:Movie {title: "Inception"})
      <-[:ACTED_IN]-(a:Actor)
      -[:ACTED_IN]->(related:Movie)

WHERE related <> m

RETURN
    a.name AS actor,
    related.title AS movie
```

This traverses:

```text
Movie → Actor → Movie
```

to find movies connected through common actors.

---

## 🚀 Future Improvements

Possible future improvements include:

* Larger movie dataset
* Personalized recommendations
* User accounts
* Watchlists
* User ratings
* Advanced recommendation scoring
* More relationship types
* Movie poster/backdrop integration
* Production deployment
* Recommendation explanations
* Advanced graph exploration

---

## 📌 Project Status

MovieGraph currently provides a working graph-based movie exploration and recommendation application using Flask and CognoDB.

---

## 👨‍💻 Author

**Kishan Pandey**

Built as a graph database application project.
