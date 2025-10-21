from flask import Flask, render_template, request, redirect, url_for
from core.company import get_all_companies
from core.inward import get_all_inwards, insert_inward

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Inward page
@app.route("/inward", methods=["GET", "POST"])
def inward():

    if request.method == "POST":
        # Retrieve form data here
        company = request.form.get("company")
        dc_no = request.form.get("dc_no")
        po_no = request.form.get("po_no")
        heat_no = request.form.get("heat_no")

        insert_inward(company, dc_no, po_no, heat_no)
        print(company, dc_no, po_no, heat_no)
        return redirect(url_for("inward"))

    return render_template("inward.html")


# Testing
@app.route("/test")
def test():
    print(get_all_companies())
    print(get_all_inwards())

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
