from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mission")
def about():
    return render_template("mission.html")

@app.route("/standarts")
def standarts():
    return render_template("standarts.html")

@app.route("/common-gases")
def common_gases():
    return render_template("common_gases.html")

@app.route("/dangers")
def dangers():
    return render_template("dangers.html")

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/brands')
def brands():
    return render_template('brands.html')

if __name__ == "__main__":
    app.run(debug=True)