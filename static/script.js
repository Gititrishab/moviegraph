const searchInput =
    document.getElementById("searchInput");

const searchButton =
    document.getElementById("searchButton");

const movieGrid =
    document.getElementById("movieGrid");

const topRatedGrid =
    document.getElementById("topRatedGrid");

const loading =
    document.getElementById("loading");

const emptyState =
    document.getElementById("emptyState");

const errorState =
    document.getElementById("errorState");

const errorMessage =
    document.getElementById("errorMessage");

const sectionTitle =
    document.getElementById("sectionTitle");

const movieCount =
    document.getElementById("movieCount");



/*
    Poster mapping.

    These are optional. If an image fails,
    the card automatically falls back to
    a cinematic placeholder.
*/

const posters = {

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



function showState(state) {

    loading.classList.add("hidden");

    emptyState.classList.add("hidden");

    errorState.classList.add("hidden");


    if (state === "loading") {
        loading.classList.remove("hidden");
    }

    if (state === "empty") {
        emptyState.classList.remove("hidden");
    }

    if (state === "error") {
        errorState.classList.remove("hidden");
    }

}



function getGenres(movie) {

    if (!movie.genres) {
        return [];
    }

    if (Array.isArray(movie.genres)) {
        return movie.genres;
    }

    return [];
}



function createMovieCard(movie) {

    const card =
        document.createElement("article");

    card.className =
        "movie-card";


    const poster =
        posters[movie.title];


    const posterHTML = poster

        ? `
            <img
                src="${poster}"
                alt="${movie.title} poster"
                class="movie-poster"
                loading="lazy"
            >
        `

        : `
            <div class="poster-fallback">
                <span>🎬</span>
                <strong>${movie.title}</strong>
            </div>
        `;


    card.innerHTML = `

        <div class="poster-wrapper">

            ${posterHTML}

            <div class="poster-overlay">

                <span class="view-movie">
                    View Movie →
                </span>

            </div>

            <div class="rating-badge">
                ⭐ ${movie.rating}
            </div>

        </div>


        <div class="movie-card-content">

            <h3>
                ${movie.title}
            </h3>

            <div class="movie-card-meta">

                <span>
                    ${movie.release_year}
                </span>

                <span class="meta-dot">
                    •
                </span>

                <span>
                    Movie
                </span>

            </div>

        </div>
    `;


    card.addEventListener(
        "click",
        () => {

            window.location.href =
                "/movie/" +
                encodeURIComponent(movie.title);

        }
    );


    return card;
}



function displayMovies(movies) {

    movieGrid.innerHTML = "";


    if (
        !movies ||
        movies.length === 0
    ) {

        movieCount.textContent = "";

        showState("empty");

        return;

    }


    loading.classList.add("hidden");

    emptyState.classList.add("hidden");

    errorState.classList.add("hidden");


    movieCount.textContent =
        `${movies.length} movies`;


    movies.forEach(movie => {

        movieGrid.appendChild(
            createMovieCard(movie)
        );

    });

}



function displayTopRated(movies) {

    topRatedGrid.innerHTML = "";


    const sorted =
        [...movies]
            .sort(
                (a, b) =>
                    b.rating - a.rating
            )
            .slice(0, 5);


    sorted.forEach(movie => {

        topRatedGrid.appendChild(
            createMovieCard(movie)
        );

    });

}



async function loadAllMovies() {

    showState("loading");


    try {

        const response =
            await fetch("/api/movies");


        const data =
            await response.json();


        if (!response.ok ||
            !data.success) {

            throw new Error(
                data.error ||
                "Unable to load movies."
            );

        }


        displayMovies(
            data.movies
        );


        displayTopRated(
            data.movies
        );


    } catch (error) {

        console.error(
            "Load movies error:",
            error
        );


        errorMessage.textContent =
            error.message;

        showState("error");

    }

}



async function searchMovies() {

    const query =
        searchInput.value.trim();


    if (!query) {

        sectionTitle.textContent =
            "All Movies";

        loadAllMovies();

        return;

    }


    showState("loading");


    movieGrid.innerHTML = "";


    try {

        const response =
            await fetch(
                "/api/movies/search?q=" +
                encodeURIComponent(query)
            );


        const data =
            await response.json();


        if (!response.ok ||
            !data.success) {

            throw new Error(
                data.error ||
                "Search failed."
            );

        }


        sectionTitle.textContent =
            `Results for "${query}"`;


        displayMovies(
            data.movies
        );


    } catch (error) {

        console.error(
            "Search error:",
            error
        );


        errorMessage.textContent =
            error.message;

        showState("error");

    }

}



searchButton.addEventListener(
    "click",
    searchMovies
);


searchInput.addEventListener(
    "keydown",
    event => {

        if (event.key === "Enter") {

            searchMovies();

        }

    }
);


loadAllMovies();