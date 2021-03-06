resource "aws_s3_bucket" "dl" {
  bucket = "datalake-edu-igti-edc-tf"
  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }

  # server_side_encryption_configuration {
  #   rule {
  #     apply_server_side_encryption_by_default {
  #       sse_algorithm = "AES256"
  #     }
  #   }
  # }
}


resource "aws_s3_bucket" "stream" {
  bucket = "igti-edu-streaming-bucket"
  #acl    = "private"

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }

  # server_side_encryption_configuration {
  #   rule {
  #     apply_server_side_encryption_by_default {
  #      sse_algorithm = "AES256"
  #    }
  #  }
  #}
}