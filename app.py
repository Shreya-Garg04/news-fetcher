from flask import Flask,render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

API="3d3fb9c23ddf4195bc28366c40944fd1"
  
def fetch_news(query):
    from_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    
    url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&language=en&sortBy=publishedAt&apiKey={API}"
    
    print("API URL:", url)  # Good for debugging

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        articles = data.get("articles", [])
        return articles[:20]  # Return top 20 articles
    else:
        print(" API failed: ", r.status_code)
        return []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        query = request.form.get('query')
        articles = fetch_news(query)
        return render_template("index.html", articles=articles , query=query)
    else:
        return render_template("index.html", articles=None, query=None)
@app.route('/about')
def about():
    print("🔍 About page loaded")
    return render_template("about.html")

@app.route('/contact')
def contact():
    print("🔍 About contact loaded")
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)    