
"""
    Title: init.py
    Author: Akash Dwivedi
    Modified By: Kushagra Agrawal
    Language: Python
    Date Created: 26-07-2021
    Date Modified: 26-08-2021
    Description:
        ###############################################################
        ## Create a webhook on a specific repository   ## 
         ###############################################################
 """
import time
import requests
import json
import os 
import pathlib
import yaml
import git
import click
import sys
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from github import Github
import datetime
from dotenv import load_dotenv



ENDPOINT = "webhook"

load_dotenv()

@view_defaults(
    route_name=ENDPOINT, renderer="json", request_method="POST"
)
class PayloadView():
    # this class will called automatically when webhook will be created successfully on a repository

    def __init__(self, request):
        self.request = request
        self.payload = self.request.json

    # This method will be called when webhook will be created successfully on a repository
    @view_config(header="X-GitHub-Event:ping")
    def payload_ping(self):
        print("Pinged! Webhook created with id {}!".format(self.payload["hook_id"]))
        return {"status": 200}

    # This method will be called when an particular push event will be triggered on an repository
    @view_config(header="X-Github-Event:push")
    def payload_push(self):
        print("No. of commits in push: ", len(self.payload['commits']))
        print("commit msg", self.payload["commits"][0]["message"])
        print("commit added", self.payload["commits"][0]["added"])
        return Response("success")
        

    # This method will be called when an pull request will be happen on a repository
    @view_config(header="X-GitHub-Event:pull_request")
    def payload_pull_request(self):
        print("pull request = ", self.payload['action'])
        print("commits in pull: ", self.payload['pull_request'])
        return Response("success")


         
@click.command()
def init():
    '''
    For initiating the webhook operation 

    Please store config.yaml in the directory 
    Please create the clone of the repository  
    \f
    
   
    '''
    
    path=pathlib.Path().resolve()
    print("Your current directory  is : ", path)
    os.chdir(path)
    try:
        a_yaml_file = open("./config.yaml")
        parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
        project_id=parsed_yaml_file["project_id"]

        response = requests.get("https://app.buildpan.com/api/v1/projects/detail/"+project_id)
        data = response.json()
       

        # print(response.status_code)
        # print(response.json())
        # print("flag1")
        name = data["project"]["repo"]["full_name"].split('/')
        token = data["project"]["githubtoken"]
        username = name[0]
        repo_name = name[1]

        
        # Before creating
        dir_list = os.listdir(path) 
        print("List of directories and files before creation:")
        print(dir_list)
        print()
        

        dictionary ={
            "token" : token,
            "username" : username,
            "repo_name" : repo_name
        }
        
        # Serializing json 
        json_object = json.dumps(dictionary, indent = 4)
        
        # Writing to sample.json
        with open(project_id+'.json',"w") as outfile:
            outfile.write(json_object)
        
    
        
        with open(project_id+'.json') as f:
         data = json.load(f)
         username = data["username"]
         token=data["token"]
         repo_name=data["repo_name"]
          

        access_token =token #"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"
        OWNER = username #"AkashAi7" # github account name
        REPO_NAME =repo_name#"Web-Scrapping-Using-Selenium-Python-"# github repository name
        EVENTS = ["*"]      # Events on github
        HOST = os.getenv('HOST')  # server ip (E.g. - ngrok tunnel)
    
        config = {
            "url": "http://{host}/{endpoint}".format(host=HOST, endpoint=ENDPOINT),
            "content_type": "json"
        }

        # login to github account
        g = Github(access_token)
        # accessing a particular repository of a account
        repo = g.get_repo("{owner}/{repo_name}".format(owner=OWNER, repo_name=REPO_NAME))
        print(repo)

        # creating a webhook on a particular repository
        try:
          repo.create_hook("web", config, EVENTS, active=True)
         
        #   pull
          for i in range(os.getenv('TIME')):
                response = requests.get(os.getenv('PUSH_COMMIT_URL'))
                res=response.content
                # print(res)
                res=str(res)
                index=res.index("'")
                index1=res.index("'",index+1)
                res=res[index+1:index1]
                print("commit found for repo ",res) 
                val=len(res)
              
      
                if val >0 and res==repo_name:
                    repo = git.Repo(path)
                    origin = repo.remote(name='origin')
                    res=origin.pull()
                    print("Looking for Pull Opeartion")
                    time.sleep(10)
                    val=0
                else:
                    print("no files to pull")
                    time.sleep(10)
          
          curtime = datetime.datetime.now()          
          response2 = requests.post(os.getenv('FETCH_LOG_URL'),data={'project_id':project_id,'repo_name':repo_name,'Time ':curtime,'user_name':username})           #success , project id , repo name , current date and time , email id
        #   print("status code is ",response2.status_code)

        except:
            print("webhook already exists on this repository ")
            flag=0
            #   pull

            for i in range(os.getenv('TIME')):
                print("in")
                response = requests.get(os.getenv('PUSH_COMMIT_URL'))
                res=response.content
                print("res")
                res=str(res)
                index=res.index("'")
                index1=res.index("'",index+1)
                res=res[index+1:index1]
                print("commit found for repo ",res) 
                val=len(res)
                print(val)
    
                if val > 0 and res==repo_name:
                    print("1")
                    repo = git.Repo(path)
                    print("2")
                    origin = repo.remote(name='origin')
                    res=origin.pull()
                    print("Looking for Pull Opeartion")
                    flag=flag+1
                    time.sleep(60)
                    curtime = datetime.datetime.now()
                    response2 = requests.post(os.getenv('FETCH_LOG_URL'),data={'project_id':project_id,'repo_name':repo_name,'Time ':curtime,'user_name':username,'message':"pull success",'status':'pull operation performed'})
                    
                    
                else:
                    print("no files to pull")
                    time.sleep(60)
                    flag=0
                    curtime = datetime.datetime.now()
                    response2 = requests.post(os.getenv('FETCH_LOG_URL'),data={'project_id':project_id,'repo_name':repo_name,'Time ':curtime,'user_name':username,'message': "pull failed",'status':'pull operation performed'})


           #success , project id , repo name , current date and time , email id'
    

          
    except:
        print("config file not found")

if __name__ == "__main__":
    config = Configurator()

    config.add_route(ENDPOINT, "/{}".format(ENDPOINT))
    config.scan()

    app = config.make_wsgi_app()
    server = make_server("localhost", 80, app)
   
    init()
   
    server.serve_forever()


