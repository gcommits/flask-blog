getFetch()
function getFetch(){
    const url = 'https://api.nasa.gov/planetary/apod?api_key=G0iT7vPXTUsIUqKnVPjXijVygYEbQGhb6z9kRpYn'
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById('nasa').src = data.hdurl
            document.getElementById('title').innerHTML = data.title
            document.getElementById('copyright').innerHTML = ('Copyright: ') + data.copyright
            document.getElementById('description').innerHTML = data.explanation
        })
        .catch(err => {
            console.log('****error')
        });
    }