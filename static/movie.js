const movieLoading = document.getElementById("movieLoading");
const movieError = document.getElementById("movieError");
const movieContent = document.getElementById("movieContent");
const moviePosters = {

    "Inception":
        "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",

    "Interstellar":
        "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",

    "The Dark Knight":
        "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",

    "The Matrix":
        "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",

    "Titanic":
        "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",

    "The Godfather":
        "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",

    "Pulp Fiction":
        "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg"

};


function showError(message) {

    movieLoading.classList.add("hidden");
    movieContent.classList.add("hidden");
    movieError.classList.remove("hidden");

    document.getElementById(
        "movieErrorMessage"
    ).textContent = message;
}


function createPersonList(container, people) {

    container.innerHTML = "";

    people.forEach(person => {

        const element = document.createElement("p");

        element.className = "person-name";

        element.textContent = person.name;

        container.appendChild(element);
    });
}


function createGenres(genres) {

    const container =
        document.getElementById("genres");

    container.innerHTML = "";

    genres.forEach(genre => {

        const tag = document.createElement("span");

        tag.className = "tag";

        tag.textContent = genre.name;

        container.appendChild(tag);
    });
}


async function loadMovie() {

    console.log("Movie title:", movieTitle);

    try {

        const response = await fetch(
            "/api/movies/" +
            encodeURIComponent(movieTitle)
        );

        console.log(
            "Movie response:",
            response.status
        );

        const data = await response.json();

        console.log(
            "Movie data:",
            data
        );


        if (!data.success) {

            throw new Error(
                data.error || "Movie not found."
            );
        }


        // Movie information

        document.getElementById(
            "movieTitle"
        ).textContent =
            data.movie.title;


        document.getElementById(
            "movieRating"
        ).textContent =
            "⭐ " + data.movie.rating;


        document.getElementById(
            "movieYear"
        ).textContent =
            data.movie.release_year;


        document.getElementById(
            "movieDescription"
        ).textContent =
            data.movie.description;
        const poster =
    moviePosters[data.movie.title];

const posterElement =
    document.getElementById("moviePoster");


if (poster) {

    posterElement.src = poster;

    posterElement.alt =
        `${data.movie.title} poster`;

} else {

    posterElement.style.display = "none";

}


        // Relationships

        createGenres(data.genres);

        createPersonList(
            document.getElementById("actors"),
            data.actors
        );

        createPersonList(
            document.getElementById("directors"),
            data.directors
        );


        // IMPORTANT:
        // Hide loading screen now.

        movieLoading.classList.add("hidden");

        movieContent.classList.remove("hidden");


        // Load recommendations separately.

        loadRecommendations();

    } catch (error) {

        console.error(
            "Movie error:",
            error
        );

        showError(error.message);
    }
}


async function loadRecommendations() {

    try {

        const response = await fetch(
            "/api/movies/" +
            encodeURIComponent(movieTitle) +
            "/recommendations"
        );


        const data = await response.json();


        if (!data.success) {
            return;
        }


        const recommendations =
            data.recommendations || [];


        const container =
            document.getElementById(
                "actorRecommendations"
            );


        container.innerHTML = "";


        recommendations.forEach(
            recommendation => {

                const card =
                    document.createElement("div");

                card.className =
                    "recommendation-card";


                card.innerHTML = `
            
    <h4>
        ${recommendation.movie.title}
    </h4>

    <p class="movie-year">
        ${recommendation.movie.release_year}
    </p>

    <span class="connection-count">
        ⭐ ${recommendation.movie.rating}
    </span>

    <div class="recommendation-reason">

        <p>
            🎭 ${recommendation.shared_actors}
            shared actor(s)
        </p>

        <p>
            🎬 ${recommendation.shared_genres}
            shared genre(s)
        </p>

    </div>

    <p class="graph-score">
        Graph score:
        <strong>${recommendation.score}</strong>
    </p>
`;


                card.onclick = function() {

                    window.location.href =
                        "/movie/" +
                        encodeURIComponent(
                            recommendation.movie.title
                        );
                };


                container.appendChild(card);
            }
        );

    } catch (error) {

        console.error(
            "Recommendation error:",
            error
        );

    }
}



async function loadGraph() {

    try {

        const response = await fetch(
            "/api/movies/" +
            encodeURIComponent(movieTitle) +
            "/graph"
        );

        const data = await response.json();

        if (!response.ok || !data.success) {
            console.error("Graph error:", data.error);
            return;
        }

        const elements = [
            ...data.nodes,
            ...data.edges
        ];

        cytoscape({

            container:
                document.getElementById("movieGraph"),

            elements: elements,
            wheelSensitivity:0.15,
            wheelSensitivity: 0.15,
            minZoom: 0.7,
            maxZoom: 2,
            // zoomingEnabled: false,

            style: [

                {
                    selector: "node",

                    style: {
                        "label": "data(label)",
                        "background-color": "#8f9cff",
                        "color": "#ffffff",
                        "text-valign": "center",
                        "text-halign": "center",
                        "font-size": "12px",
                        "width": "45px",
                        "height": "45px"
                    }
                },

                {
                    selector: 'node[type="Movie"]',

                    style: {
                        "background-color": "#8f9cff",
                        "width": "65px",
                        "height": "65px",
                        "font-weight": "bold"
                    }
                },

                {
                    selector: 'node[type="Actor"]',

                    style: {
                        "background-color": "#6fbd8f"
                    }
                },

                {
                    selector: 'node[type="Director"]',

                    style: {
                        "background-color": "#d49a61"
                    }
                },

                {
                    selector: 'node[type="Genre"]',

                    style: {
                        "background-color": "#b678c4"
                    }
                },

                {
                    selector: "edge",

                    style: {
                        "width": 2,
                        "line-color": "#555c6d",
                        "target-arrow-color": "#555c6d",
                        "target-arrow-shape": "triangle",
                        "curve-style": "bezier",
                        "label": "data(label)",
                        "font-size": "9px",
                        "color": "#9da3b0"
                    }
                }

            ],

           layout: {
    name: "breadthfirst",
    directed: true,
    padding: 60,
    spacingFactor: 1.4,
    avoidOverlap: true,
    animate: false
}

        });

    } catch (error) {

        console.error(
            "Graph loading error:",
            error
        );

    }

}

loadMovie();
loadGraph();