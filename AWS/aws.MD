AWS core services:

compute - access to crup resources
Storage - storage of data
Databases - hosted database services
Networking underpins other services


#creating an instance
- aws ec2 run-instances --image-id {IMAGE_ID} --count {AMOUNT_OF_INSTANCES} --instance-type {MACHINE_SIZE} --key-name {KEY_PAIR_NAME} --subnet-id {SUBNET_ID}

#stops an instance
- aws ec2 terminate-instances --instance-ids {instance_id}

###learn what jq doesnt and how to extract info about the instances from the cli 

#get infoabout instances
- export UBUNTU_AMI=$(aws ec2 describe-instances | jq '.Reservations[0].Instances[0].ImageId' | tr -d '"')

#creating a keypair
- aws ec2 create-key-pair --key-name my-cli-key --query KeyMaterial --output text > cli-key.pem


#getting instance metadata
- curl -w "\n" http://169.254.169.254/latest/meta-data/
- curl -w "\n" http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key