
# IMDb Movie Scraper for Mobile Devices

## Descripción del Proyecto

Este proyecto está diseñado para capturar solicitudes móviles de la página de IMDb y extraer información clave de una película a partir de una URL proporcionada. Utilizando técnicas de web scraping, el objetivo es obtener datos como el título, año de lanzamiento, calificación y director de la película, y presentarlos en un formato JSON.

## Características

- **Extracción de Datos Específicos**: Obtención de título, año de lanzamiento, calificación y director de la película.
- **Enfoque Móvil**: Adaptado para capturar datos de la versión móvil de IMDb.
- **Fácil Integración**: Solo se necesita proporcionar la URL de una película para comenzar a extraer información.

## Requisitos

Asegúrate de tener instalados los siguientes paquetes en tu entorno de desarrollo:

- Python 3.x
- Requests
- BeautifulSoup4

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Uso

1. Clona el repositorio:

   ```bash
   [git clone https://github.com/tu-usuario/IMDb-Mobile-Scraper.git](https://github.com/BluerZu/ScrapyBasicIMDB)
   cd ScrapyBasicIMDB
   ```

2. Asegúrate de tener un entorno virtual activado y las dependencias instaladas.

   ```bash
   pip install -r requirements.txt
   ```

4. Corre el script de scraping con la URL de la película deseada:

   ```bash
   python main.py
   ```

   Asegúrate de que el archivo `main.py` esté configurado para recibir y procesar la URL de la película correctamente.

## Ejemplo de Entrada

Para obtener información de la película "Joker: Folie a Deux", puedes usar la URL:

```python
movie_url = "https://m.imdb.com/title/tt11315808"
```

El script extraerá el título, el año de lanzamiento, la calificación y el director de la película.
