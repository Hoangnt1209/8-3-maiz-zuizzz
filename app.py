from flask import Flask,render_template


app = Flask(__name__)


# Define a route to serve your HTML file
@app.get("/")
def get_html():
    # Assuming your HTML file is named index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)