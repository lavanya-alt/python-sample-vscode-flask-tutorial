
from turtle import pd
import pandas as pd
import requests

from flask import Flask, Response, render_template, request

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def callback():
    auth_token = '4jIbUl4sRrL8GNN0merp1KESByCrZ5HmSHiwOUEtGWSk5aSZb6sfjM9fVvOQFzIFeAUUTAVi8WHvyFd9g0hBLUOEZumyBXFhH0mUyGVEgrXmCP6UYtCe8ixbJDhuDyOZ'
    header = {"x-api-key": auth_token, 'Content-Type': "application/json"}

    project_data = {"workspaceId": 32504}
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
        result = ('{:>15}     {:<15}'.format(c, d))

    df = pd.DataFrame(x, columns=['Id'])
    df['Name'] = y
    print(df)

    return render_template("index_1.html", items=[df.to_html(classes='data', header="true")])


@app.route('/processform', methods=["POST"])
def supervise():
    auth_token = '4jIbUl4sRrL8GNN0merp1KESByCrZ5HmSHiwOUEtGWSk5aSZb6sfjM9fVvOQFzIFeAUUTAVi8WHvyFd9g0hBLUOEZumyBXFhH0mUyGVEgrXmCP6UYtCe8ixbJDhuDyOZ'
    header = {"x-api-key": auth_token, 'Content-Type': "application/json"}

    project_data = {"workspaceId": 32504}
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
        result = ('{:>15}     {:<15}'.format(c, d))

    df_3 = pd.DataFrame(x, columns=['Id'])
    df_3['Name'] = y


    auth_token = 'ZowU7fVBiMajzKgwlG5ux6aEVMoL2aLHFhvOeru3uZuaWXvV6IJZNhV7ZRS80icaw16K8hUICZtNNGW6wQjuke3kkb6wtjIxf1DEbob7XIL9TLLJ13Wgc3CVOlaZ3sgv'
    header = {"x-api-key": auth_token, 'Content-Type': "application/json"}
    projectid = request.form.get('text')
    print(projectid)

    workspace_data = {"id": projectid,"extended" : True}
    workspace_url = 'https://app.supervise.ly/public/api/v3/projects.meta'
    res = requests.get(workspace_url, json=workspace_data, headers=header).json()
    df = pd.DataFrame.from_dict(res, orient="index")
    print(df)

    project_data = {"id": projectid}
    project_url = 'https://app.supervise.ly/public/api/v3/projects.info'
    res_2 = requests.get(project_url, json=project_data, headers=header).json()
    df_2 = pd.DataFrame.from_dict(res_2,orient="index")
    print(df_2)


    return render_template("index_1.html",items=[df_3.to_html(classes='data', header="true")],tables=[df.to_html(classes='data', header="true")], titles=[df_2.to_html(classes='data', header="true")])


if __name__ == '__main__':
    app.run("localhost", 8080)

