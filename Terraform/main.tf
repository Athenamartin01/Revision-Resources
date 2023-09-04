provider "aws" { #sets up a connection to the aws servers
    access_key =  "KEY NIFO"
    secret_key = "SECRET KEY INFO"
    region = "eu-west-2"
}

resource "aws_instance" "name" { #sets up an instance
    ami = "ami-0eb260c4d5475b901"
    instance_type = "t2.micro"
}