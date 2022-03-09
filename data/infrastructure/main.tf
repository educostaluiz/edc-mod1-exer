# hcl

resource "aws_s3_bucket" "datalake" {
  #parametros de configuração do recurso
  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
  #acl    = "private"

 # server_side_encryption_configuration {
 #   rule {
 #     apply_server_side_encryption_by_default {
 #      sse_algorithm     = "AES256"
 #     }
 #   }
 # }


  tags = {
    IES   = "IGTI"
    CURSO = "EDC"
  }
}

resource "aws_s3_bucket_object" "codigo_spark" {
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/job_from_tf.py"
  acl    = "private"
  source  = "job_emr.py"
  etag   = filemd5("job_emr.py")

}