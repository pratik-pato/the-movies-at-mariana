let movieData = [];

function loadMovies() {
    var settings = {
        "url": "/movie_app/movies/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function(response) {
        movieData = response;
        generateTableRows(response);
    }).fail(function(xhr, status, error) {
        console.error("Failed to load movies:", error);
    });
}

function applyFilterAndRenderTable(selectedGenres) {
    const filteredData = selectedGenres ?
        movieData.filter((movie) =>
            movie.genres.some((genre) => selectedGenres.includes(genre.genre))
        ) :
        movieData;

    generateTableRows(filteredData);
}

function loadGenreDD() {
    var settings = {
        "url": "/movie_app/genres/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function(response) {
        console.log(response);
        // Populate genre options in the dropdown
        populateGenreDropdown(response);
    });
}

function populateGenreDropdown(genres) {
    var dropdown = $('#genreDropdown');
    var menu = dropdown.find('.menu');
    genres.forEach(function(genre) {
        menu.append(`<div class="item" data-value="${genre.genre}">${genre.genre}</div>`);
    });
    dropdown.dropdown({
        onChange: function(value, text, $selectedItem) {
            const selectedGenres = value.split(',');
            applyFilterAndRenderTable(selectedGenres);
        },
    });
}


function generateTableRows(data) {
    let rows = '';
    data.forEach((movie) => {
        const genres = movie.genres.map((genre) => genre.genre).join(', ');
        rows += `
          <tr>
            <td>${movie.title}</td>
            <td><img src="${movie.poster}" width="100" alt="${movie.title}"></td>
            <td>${genres}</td>
            <td>${movie.imdb_rating}</td>
            <td>${movie.year}</td>
            <td>${movie.runtime}</td>
          </tr>
        `;
    });
    $('#movieTable tbody').html(rows);
    initializeDataTable(data);
    return rows;
}


function initializeDataTable(jsonData) {
    if (table) {
        table.destroy();
    }
    const table = $('#movieTable').DataTable({
        data: jsonData,
        columns: [{
                data: 'title'
            },
            {
                data: 'poster',
                render: (data) => `<img src="${data}" height="100" alt="Poster">`
            },
            {
                data: null,
                render: (data) => data.genres.map((genre) => genre.genre).join(', ')
            },
            {
                data: 'imdb_rating'
            },
            {
                data: 'year'
            },
            {
                data: 'runtime'
            },
        ],
    });
}

$(document).ready(function() {
    loadMovies();
    loadGenreDD();
});