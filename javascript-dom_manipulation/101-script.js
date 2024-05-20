document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('btn_translate').addEventListener('click', function () {
        const languageCode = document.getElementById('language_code').value;
        
        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                document.getElementById('hello').innerText = data.hello;
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    });
});
