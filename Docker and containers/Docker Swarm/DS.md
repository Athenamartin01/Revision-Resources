2 types of vm:
- managers
- workers

starting docker swarm 
- docker swarm init

to get tokens:
- docker swarm join-tkoen manager/worker
to join new vm(node) 
- docker swarm join --token given_token 

View nodes:
- docker node ls

removing node:
(from worker line)
- docker swarm leave

(from manager line)
- docker node update --availability drain NODE_NAME
- docker node rm 

# stacks

runs dockercompose.yaml on all nodes
- docker stack deploy --compose-file docker-compose.yaml stack_name

list services on stack
- docker stack services stack_name

remove a stack
- docker stack rm stack_name