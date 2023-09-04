
# meta arguements

- depends_on
resource "aws_iam_role_policy" "example" {
    name   = "example-admin"
    role   = aws_iam_role.owner
}

resource "aws_instance" "example" {
    ami           = "ami-2757f631"
    instance_type = "t2.micro"
    depends_on    = [aws_iam_role_policy.example]
}

- count #creates 3 instances
resource "aws_instance" "instance_name" {
    count = 2
    ami = ""
    type = ""
    tags = {
        name = "machine ${count.index}"
    }
}

- for_each

- provider
terraform {
    required_providers {
        aws{

        }
    }
}
- lifecycle

lifecycle{
    create_before_destroy = true
    ignore_changes = [tags , ami, instance_type]

}

- timeouts
resource "" "" {
    timeouts {
        create = "5m"
        delete = "2h"
    }
}
