const form = document.getElementById('searchForm');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const query = document.getElementById('query').value;
  const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      resultsDiv.innerHTML = '';

      data.forEach(tvShow => {
        const article = document.createElement('article');

        const title = document.createElement('h2');
        title.textContent = tvShow.show.name;
        article.appendChild(title);

        const link = document.createElement('a');
        link.href = tvShow.show.url;
        link.target = '_blank';
        link.textContent = 'More info';
        article.appendChild(link);

        if (tvShow.show.image?.medium) {
          const img = document.createElement('img');
          img.src = tvShow.show.image.medium;
          img.alt = tvShow.show.name;
          article.appendChild(img);
        }

        const summary = document.createElement('div');
        summary.innerHTML = tvShow.show.summary || 'No summary available.';
        article.appendChild(summary);

        resultsDiv.appendChild(article);
      });
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});
