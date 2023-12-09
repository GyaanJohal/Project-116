from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def website():
    return render_template("index.html",index_variable="Gyaan")
app.run(debug=True)