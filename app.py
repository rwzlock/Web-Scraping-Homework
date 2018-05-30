from flask import Flask, jsonify
import scrape_mars
import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

app = Flask(__name__)

@app.route("/")
def welcome():
    mars_db = db.mars_db.find()
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/scrape"
    )


@app.route("/scrape")
def scrape():
    use mars_db
    scrape_mars.scrape();
    db.mars_db.insert(scraped_dict)
    return jsonify(scraped_dict)


if __name__ == '__main__':
    app.run(debug=True)