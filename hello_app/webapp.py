# Entry point for the application.
from . import app    # For application discovery by the 'flask' command. 
from . import views  # For import side-effects of setting up routes. 
from flask import Flask, Response, render_template
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/')
def supervise():
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
    for c, d in zip(x, y):
        result=('{:>15}     {:<15}'.format(c, d))

    df = pd.DataFrame(x,columns=['Id'])
    df['Name'] = y
    print(df)


    return render_template("contact.html",tables=[df.to_html(classes='data', header="true")])




if __name__ == '__main__':
    app.run()

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')
