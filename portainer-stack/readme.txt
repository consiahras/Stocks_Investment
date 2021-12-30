#To deploy portanainer stack manually:
docker stack deploy --compose-file=portainer-agent-stack.yml portainer

#to deploy portainer stack to raspberry pi :
docker stack deploy --compose-file=portainer-stack-raspberry.yml portainer
