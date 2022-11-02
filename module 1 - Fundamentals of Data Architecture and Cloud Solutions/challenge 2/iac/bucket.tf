# Creating bucket resource

## Ref: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket
resource "aws_s3_bucket" "datalake" {
  # Settings parameters
  bucket = "${var.base_bucket_name}-${var.owner}-${var.goal}-${var.by}"
  acl    = "private"
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    goal = "learning"
  }
}