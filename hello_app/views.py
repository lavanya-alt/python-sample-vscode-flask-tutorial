from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact1/")
def contact1():
    return render_template("contact1.html")

@app.route("/contact2/")
def contact2():
    return render_template("contact2.html")

@app.route("/contact",methods=["POST"])
def contact():
    auth_token = '4jIbUl4sRrL8GNN0merp1KESByCrZ5HmSHiwOUEtGWSk5aSZb6sfjM9fVvOQFzIFeAUUTAVi8WHvyFd9g0hBLUOEZumyBXFhH0mUyGVEgrXmCP6UYtCe8ixbJDhuDyOZ'
    header = {"x-api-key": auth_token, 'Content-Type': "application/json"}
    project_data = {"workspaceId": 32276}
    project_url = 'https://app.supervise.ly/public/api/v3/projects.list'
    response = requests.get(project_url, json=project_data, headers=header).json()
    x = list()
    y = list()
    for entity in response["entities"]:
        id = entity["id"]
        name = entity["name"]
        x.append(id)
        y.append(name)

    df = pd.DataFrame(x,columns=['Id'])
    df['Name'] = y
    #print(df)
    return render_template("contact.html",tables=[df.to_html(classes='data', header="true")])  

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
