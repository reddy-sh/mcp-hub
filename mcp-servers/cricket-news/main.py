import requests
from bs4 import BeautifulSoup

def get_cricket_news():
    """Fetch the latest cricket news from Cricinfo."""
    url = "https://www.espncricinfo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract headlines (adjust selectors based on Cricinfo's structure)
    headlines = [headline.text for headline in soup.select(".headline-class")]  # Replace with actual class
    return headlines

def get_live_scores():
    """Fetch live cricket scores from Cricinfo."""
    url = "https://www.espncricinfo.com/live-cricket-score"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract live scores (adjust selectors based on Cricinfo's structure)
    scores = [score.text for score in soup.select(".score-class")]  # Replace with actual class
    return scores

if __name__ == "__main__":
    print("Latest Cricket News:")
    print(get_cricket_news())

    print("\nLive Cricket Scores:")
    print(get_live_scores())