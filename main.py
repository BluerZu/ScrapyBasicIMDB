import requests
from bs4 import BeautifulSoup

# Función para extraer datos básicos de una película desde IMDB
def scrape_imdb_movie(url):
    # Realizar la solicitud a la URL
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code != 200:
        print(f"Error al acceder a la URL: {response.status_code}")
        return None

    # Parsear el contenido de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer el título de la película
    title = soup.find('h1').text.strip()

    # Extraer el año de lanzamiento desde el título
    title_tag = soup.find('title')
    year = 'N/A'
    if title_tag:
        year_search = title_tag.text.split('(')
        if len(year_search) > 1:
            year = year_search[1].split(')')[0]  # Esto extrae solo el año sin incluir 'IMDb'

    # Extraer la calificación de la película
    rating_tag = soup.find('span', class_='sc-d541859f-1 imUuxf')
    rating = rating_tag.text if rating_tag else 'N/A'

    # Extraer el director de la película
    director_tag = soup.find('a', href=lambda href: href and '/name/nm' in href)
    director = director_tag.text.strip() if director_tag else 'N/A'

    # Crear un diccionario con los datos
    movie_data = {
        'Título': title,
        'Año': year,
        'Calificación': rating,
        'Director': director
    }

    return movie_data

# URL de ejemplo para una película en IMDB
# movie_url = "https://m.imdb.com/title/tt1375666/"  # URL de Inception

# movie_url = "https://m.imdb.com/title/tt11315808"  # URL de Joker 2

movie_url = "https://m.imdb.com/title/tt29623480/"  # URL de Robot Salvaje

# Scrapeando la información
movie_info = scrape_imdb_movie(movie_url)

# Mostrar los resultados
if movie_info:
    print(movie_info)
