from flask import Flask, Response, render_template
import requests
#import supervisely_lib as sly
#import os
#import numpy as np
#from matplotlib import pyplot as plt
#import json

# import cv2

app = Flask(__name__)



@app.route('/')
def contact():


    auth_token = 'ZowU7fVBiMajzKgwlG5ux6aEVMoL2aLHFhvOeru3uZuaWXvV6IJZNhV7ZRS80icaw16K8hUICZtNNGW6wQjuke3kkb6wtjIxf1DEbob7XIL9TLLJ13Wgc3CVOlaZ3sgv'
    header = {"x-api-key": auth_token, 'Content-Type': "application/json"}

    workspace_data = {"id": 322955}
    workspace_url = 'https://app.supervise.ly/public/api/v3/datasets.info'
    res = requests.get(workspace_url, json=workspace_data, headers=header).json()
    # # workspace_response=res.get("entities")
    # # print(workspace_response)
    # for entity in res["entities"]:
    #     id = entity["id"]
    print(res)

    # project_data = {"id": 77276}
    # project_url = 'https://app.supervise.ly/public/api/v3/projects.stats'
    # response = requests.get(project_url, json=project_data, headers=header).json()
    # print(response)

    return render_template("contact.html", res=res)



