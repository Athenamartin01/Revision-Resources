variable "ami-id" {
    description = "AMI ID of ubuntu 18.04LTS eu-west-2"
    default     = "ami-0eb260c4d5475b901"
}

variable "instance-type" {
    description = "Free tier EC2 Instance type"
    default     = "t2.micro"
}
