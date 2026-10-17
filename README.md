# Daily Weather Story Generator

A small Python project that pulls live weather data from the [OpenWeatherMap API](https://openweathermap.org/api), renders the temperature and humidity of five cities onto a ready-made story template, and saves the results as PNG and PDF files. All generated PDFs are then sent by email through Gmail.

## Features

- Fetches current temperature (°C) and humidity (%) from OpenWeatherMap
- Generates one image per region: **Turkey**, **UK**, and **World**
- Draws the title, today's date, city names, and values onto a template image with Pillow
- Saves each image as both `.png` (for social media stories) and `.pdf`
- Emails all PDFs as attachments with a single command
- Easy to customize: change the cities by editing a few lists

## Example Output

| Turkey | UK | World |
|:---:|:---:|:---:|
| İstanbul, Bursa, Ankara, İzmir, Antalya | London, Edinburgh, Manchester, Liverpool, Glasgow | Seoul, Tokyo, Hokkaido, Melbourne, Sydney |

Each image has the same layout: a title, today's date, and a table of five cities with their temperature and humidity.

## Project Structure

```text
.
├── weather.py              # Fetches weather data, draws the images, saves PNG/PDF
├── sender.py               # Sends the generated PDFs by email
├── story.png               # Blank template image (background and table layout)
├── ClarityCity-Light.ttf   # Font used for all text
└── OFL.txt                 # License of the font (SIL Open Font License 1.1)
```

## Requirements

- Python 3.8+
- A free [OpenWeatherMap API key](https://home.openweathermap.org/api_keys)
- A Gmail account with an App Password (for sending emails)
- Libraries: `requests`, `Pillow`

```bash
pip install requests Pillow
```

## Setup

### 1. Add your OpenWeatherMap API key

In `weather.py`, replace the placeholder:

```python
api = "YOUR API KEY HERE"
```

New OpenWeatherMap keys can take a little while to activate after you sign up.

### 2. Configure email

In `sender.py`, fill in your details:

```python
sender_mail = "YOUR EMAIL ADRESS HERE"
sender_psw = "YOUR EMAIL APP PASSWORD HERE"
reciever = "TARGET EMAIL HERE"
```

Gmail requires an **App Password** instead of your normal password:

1. Enable 2-Step Verification on your Google account.
2. Create an App Password in your Google account security settings.
3. Use that App Password in `sender.py`.

### 3. Choose your cities (optional)

The cities are defined as lists in `weather.py`. Each list holds five city names, followed by a label that is used in the output file names:

```python
uk_list = ["London", "Edinburgh", "Manchester", "Liverpool", "Glasgow", "UK"]
tr_list = ["İstanbul", "Bursa", "Ankara", "İzmir", "Antalya", "TR"]
wrld_list = ["Seoul", "Tokyo", "Hokkaido", "Melbourne", "Sydney", "WORLD"]
```

To add another region, create a new list in the same format and add it to `city_list`.

## Usage

```bash
python weather.py
```

For each region the script will:

1. Open `story.png` and write the title and today's date on it
2. Request the weather for each of the five cities
3. Write each city's name, temperature, and humidity onto the image
4. Save the result as `YYYY-MM-DD <LABEL> .png` and `YYYY-MM-DD <LABEL> .pdf`

When all regions are done, the PDFs are emailed through `sender.py`.

To run it automatically every day, schedule it with `cron` (Linux/macOS) or Task Scheduler (Windows).

## How It Works

- **Weather data:** `weather.py` calls the OpenWeatherMap current weather endpoint with `units=metric`, then reads `main.temp` and `main.humidity` from the JSON response.
- **Image drawing:** Pillow's `ImageDraw` writes the text onto `story.png` at fixed pixel positions, one row per city.
- **PDF export:** The image is converted to RGB and saved as a PDF.
- **Email:** `sender.py` builds an email with `EmailMessage`, attaches every PDF, and sends it via `smtp.gmail.com` on port 587 with TLS.

## Limitations

- **Fixed layout:** Text positions are hardcoded for the template, so each region must have exactly five cities, and long city names may overflow their cell.
- **No error handling:** If a city name isn't found or the API request fails, the script will crash.

## Ideas for Improvement

- Add error handling for failed requests and unknown cities
- Load credentials from environment variables
- Add weather icons or conditions (sunny, rainy, etc.) to each row
- Attach the PNG files to the email as well
- Support a variable number of cities per image
- Add a real multi-day forecast using the forecast endpoint

## Credits

- Weather data by [OpenWeatherMap](https://openweathermap.org/)
- Font: Clarity City from [Google Fonts](https://fonts.google.com/), © 2019 The Clarity City Project Authors, licensed under the [SIL Open Font License 1.1](https://openfontlicense.org). See `OFL.txt` for the full license text.
- Template image (`story.png`): created by the author

## Disclaimer

This project is for personal and educational use.
