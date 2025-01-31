from fastapi import FastAPI
import requests

app = FastAPI()

NEWS_API_KEY = "cf770cba8f414cd4b116fd6da62e75f2"  
NEWS_API_URL = "https://newsapi.org/v2/everything"

@app.get("/")
def welcome():
    return {"message": "Welcome to the News Chatbot API!"}

@app.get("/news")
def get_news(query: str):
    """
    Fetch news articles based on the user's query.
    """
    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt"
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if "articles" in data:
        return {"articles": data["articles"][:5]}  # Return the top 5 articles

    return {"error": "Could not fetch news"}

