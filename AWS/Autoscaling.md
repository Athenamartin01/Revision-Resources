AUTOSCALING:
- auto-scaling group: dynamic pool of instance with upper/lower bound for instance count 
- launch template: initial config for instances
- scaling policy: rules for scaling 

#creating a security group
- aws ec2 create-security-group --description "QA Sample SG" --group-name QASGSAMPLE2020