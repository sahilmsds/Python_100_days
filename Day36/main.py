import requests

STOCK_NAME = "YOUR_STOCK"  # Back to Reliance
COMPANY_NAME = "STOCK_COMPANY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_key = "YOUR_API_KEY"
NEWS_API = "YOUR_API_KEY"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": alpha_key
}

news_params = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME,
    "language": "en",  # Added language parameter
    "sortBy": "publishedAt"  # Added sorting parameter
}

try:
    # Get stock data
    print("Fetching stock data...")
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    
    stock_data = response.json()
    
    # Debug: Print the response to see what we're getting
    print("Stock API Response keys:", stock_data.keys())
    
    # Check if we have the expected data structure
    if "Time Series (Daily)" not in stock_data:
        print("Error: 'Time Series (Daily)' not found in response")
        if "Error Message" in stock_data:
            print("API Error:", stock_data["Error Message"])
        elif "Note" in stock_data:
            print("API Note:", stock_data["Note"])
        else:
            print("Full response:", stock_data)
        exit()
    
    data = stock_data["Time Series (Daily)"]
    data_list = [value for key, value in data.items()]
    
    # Check if we have enough data
    if len(data_list) < 2:
        print("Error: Not enough historical data available")
        exit()
    
    yesterday_data = data_list[0]
    yesterday_close = float(yesterday_data["4. close"])
    
    day_before_yesterday = data_list[1]
    day_before_yesterday_close = float(day_before_yesterday["4. close"])
    
    # Calculate difference and percentage
    difference = yesterday_close - day_before_yesterday_close
    
    # Fixed percentage calculation
    diff_percentage = round(100 * (difference / day_before_yesterday_close), 2)
    
    print(f"Yesterday's close: {yesterday_close}")
    print(f"Day before yesterday's close: {day_before_yesterday_close}")
    print(f"Percentage change: {diff_percentage}%")
    
    up_down = "🔺" if diff_percentage > 0 else "🔻"
    
    # Check if change is significant (using 0.5% threshold for testing)
    if abs(diff_percentage) > 0.5:
        print("Significant change detected. Fetching news...")
        
        # Get news data
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        news_response.raise_for_status()
        news_data = news_response.json()
        
        # Check if we have articles
        if "articles" not in news_data:
            print("Error: No articles found in news response")
            print("News API Response:", news_data)
            exit()
        
        articles = news_data["articles"]
        
        if len(articles) == 0:
            print("No news articles found for", COMPANY_NAME)
            exit()
        
        # Get first 3 articles
        three_articles = articles[:3]
        
        # Format articles
        formatted_articles = []
        for article in three_articles:
            title = article.get('title', 'No title available')
            description = article.get('description', 'No description available')
            
            formatted_message = f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {title}\nBrief: {description}\n"
            formatted_articles.append(formatted_message)
        
        # Print formatted articles
        for i, article in enumerate(formatted_articles, 1):
            print(f"\n--- Article {i} ---")
            print(article)
            
    else:
        print(f"Change of {diff_percentage}% is not significant enough (threshold: 1%)")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except KeyError as e:
    print(f"Key error - missing expected data: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")