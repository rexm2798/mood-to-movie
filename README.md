# 🎬 Mood to Movie Recommender 🎭

A fun and interactive Streamlit web application that recommends movies based on your current mood, detected from a selfie\!

## ✨ Features

  * **Mood Detection:** Analyzes facial expressions from your selfie to determine your dominant emotion (happy, sad, angry, surprise, fear, disgust, neutral). Powered by `DeepFace`.
  * **Selfie Input:** Easily take a photo using your device's camera or upload an existing image.
  * **Movie Recommendation:** Suggests a movie from a curated list based on the detected mood.
  * **Rich Movie Details:** Fetches additional movie information like poster, IMDb rating, genre, and plot using the OMDb API for a better recommendation experience.
  * **IMDb Link:** Provides a direct link to the movie's IMDb page.
  * **Fallback Recommendation:** If OMDb details can't be fetched, a basic recommendation with an IMDb link is still provided.

## ⚙️ How It Works

1.  **User Input:** The user either takes a selfie using the Streamlit camera input or uploads an image file.
2.  **Image Processing (app.py):** The `app.py` script receives the image data, opens it using `Pillow`, displays it on the Streamlit interface, and then saves it to a temporary `.jpg` file.
3.  **Mood Analysis (movie\_recommender.py):**
      * The path to the temporary image file is passed to the `detect_mood_and_recommend` function in `movie_recommender.py`.
      * `DeepFace` is used to analyze the emotion from the image. It returns the dominant emotion (e.g., 'happy', 'sad').
4.  **Movie Selection (movie\_recommender.py):**
      * Based on the detected dominant emotion, the application looks up a corresponding list of movies in `movie.json`.
      * A random movie is selected from that list.
5.  **Fetching Details (movie\_recommender.py):**
      * If an OMDb API key is configured, the application sends a request to the OMDb API to fetch rich details (poster, rating, plot, etc.) about the recommended movie.
6.  **Display (movie\_recommender.py):** The detected mood and the movie recommendation (with detailed information if available) are displayed to the user on the Streamlit interface.

## 🚀 Technologies Used

  * **Python:** The core programming language.
  * **Streamlit:** For building the interactive web application.
  * **DeepFace:** A powerful facial attribute analysis (emotion, age, gender, race) library.
  * **Pillow (PIL):** For image manipulation.
  * **Requests:** For making HTTP requests to the OMDb API.
  * **python-dotenv:** For managing environment variables (like API keys).
  * **OMDb API:** A RESTful web service to obtain movie information.

## 🛠️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

  * Python 3.8+
  * `pip` (Python package installer)

### 1\. Clone the Repository

```bash
git clone https://github.com/your-username/mood-to-movie-recommender.git # Replace with your repo URL
cd mood-to-movie-recommender
```

### 2\. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

### 3\. Activate the Virtual Environment

  * **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
  * **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4\. Install Dependencies

Install all the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

*(If you don't have a `requirements.txt` yet, you can generate one after installing `streamlit`, `deepface`, `Pillow`, `requests`, `python-dotenv` with `pip freeze > requirements.txt`)*.

### 5\. Get an OMDb API Key (Optional, but Recommended)

For fetching rich movie details, you'll need a free API key from OMDb:

1.  Go to [OMDb API](http://www.omdbapi.com/apikey.aspx).
2.  Sign up and request your free API key.
3.  Once you have your key, create a file named `.env` in the root directory of your project (the same directory as `app.py`).
4.  Add the following line to your `.env` file, replacing `YOUR_OMDB_API_KEY` with your actual key:
    ```
    OMDB_API_KEY=YOUR_OMDB_API_KEY
    ```
    *If you don't provide an API key, the app will still recommend movies but with basic details (title and IMDb link only).*

## 🚀 Usage

With the virtual environment activated, run the Streamlit application:

```bash
streamlit run app.py
```

This will open the application in your default web browser.

## 📁 Project Structure

```
.
├── app.py                     # Main Streamlit application
├── movie_recommender.py       # Logic for mood detection and movie recommendation
├── movie.json                 # Curated list of movies categorized by mood
|- packages.txt                #library
└── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🎬 Movie Data (`movie.json`)

The `movie.json` file is a JSON object where keys represent moods (e.g., "happy", "sad", "angry") and values are lists of movie objects. Each movie object contains a `"title"` and an `"imdb_link"`.

Example structure:

```json
{
  "happy": [
    {
      "title": "Singin’ in the Rain",
      "imdb_link": "https://www.imdb.com/title/tt0045152/"
    },
    // ... more happy movies
  ],
  "sad": [
    {
      "title": "Inside Out",
      "imdb_link": "https://www.imdb.com/title/tt2096673/"
    },
    // ... more sad movies
  ],
  // ... other moods
}
```

You can extend or modify this file to include more movies or refine the existing recommendations.


## 🙏 Acknowledgements

  * [Streamlit](https://streamlit.io/)
  * [DeepFace](https://github.com/serengil/deepface)
  * [OMDb API](http://www.omdbapi.com/)