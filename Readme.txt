Practice code from cmu cloud computing code exercises. This code create a backend/frontend to run python codes.
The goal is to deploy both as Kubernetes services.
Steps:
1- Code servers for backend amd UI.
2- Create docker container (first create docker files.) then using: 
  cd playground_server; docker build --rm --tag pyservice:latest .
  cd playground_ui; docker build --rm --tag playground:latest . 
3- Test the code by running containers:
  docker run -d -p 80:6000 pyservice:latest
  curl -X POST -H "Content-Type: application/json" -d '{"code": "print(5)"}' localhost:80/py/eval
  we can also run the plagyround same way but need to update the pythonServiceHostName accordingly.
4- deploy to kubernetes:
  1- complete the config.yaml.
  2- deploy using : 
    kubectl create -f config.yaml
    check: 
    kubectl get deployments
    kubectl get services (get the ip for loadblancer)
5- check the ui from browser. 