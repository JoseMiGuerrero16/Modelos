const textArea = document.getElementById('search-text');
const searchButton = document.getElementById('search-button');

textArea.addEventListener('keydown', (event) => {
    searchButton.style.display = 'block';

    if (event.key === 'Enter') {
        event.preventDefault();
        searchButton.click();
    }
});

textArea.addEventListener('blur', (event) => {
    if (textArea.value === '') {
        searchButton.style.display = 'none';
    }
});

function displaySearch(data) {
    const resultadosBusqueda = document.getElementById('resultados-busqueda');

    resultadosBusqueda.innerHTML = '';

    for (let index = 0; index < data.length; index++) {
        const resultadoBusqueda = document.createElement('div');
        resultadoBusqueda.classList.add('resultado-busqueda');

        const imagen = document.createElement('img');
        imagen.src = data[index].profile_picture;
        imagen.alt = 'profile_picture';
        imagen.draggable = 'false';

        const resultadoMetadata = document.createElement('div');
        resultadoMetadata.classList.add('resultado-metadata');

        const titulo = document.createElement('span');
        titulo.innerHTML = data[index].title;

        const link = document.createElement('a');
        link.href = data[index].link;
        link.textContent = data[index].link;

        console.log(data[index]);

        resultadoMetadata.appendChild(titulo);
        resultadoMetadata.appendChild(link);

        resultadoBusqueda.appendChild(imagen);
        resultadoBusqueda.appendChild(resultadoMetadata);

        resultadosBusqueda.appendChild(resultadoBusqueda);
    }
}

document.getElementById('search-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const consulta = document.getElementById('search-text').value;

    try {
        const response = await fetch('/buscar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ consulta: consulta })
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Success:', data);
            displaySearch(data);
        } else {
            console.error('Error en la respuesta del servidor:', response.status, response.statusText);
        }
    } catch (error) {
        console.error('Error en la solicitud Fetch:', error);
    }
});