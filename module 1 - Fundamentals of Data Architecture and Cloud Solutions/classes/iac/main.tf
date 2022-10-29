# HCL - Hashicorp Configuration Language
# Declarative language

## Ref: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket
resource "aws_s3_bucket" "datalake" {
  # Settings parameters
  bucket = "${var.base_bucket_name}-${var.owner}-${var.area}-${var.by}"
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

resource "aws_s3_bucket_object" "spark_code_ch1" {
  bucket = aws_s3_bucket.datalake.id
  key    = "spark_code/etl_with_spark_from_tf.py"
  acl    = "private"
  source = "../../challenge 1/scripts/etl_with_spark.py"
  etag   = filemd5("../../challenge 1/scripts/etl_with_spark.py")
}

provider "aws" {
  region = var.provider_region
}