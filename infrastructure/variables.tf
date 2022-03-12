variable "base_bucket_name" {
  default = "datalake-igti-tf"
}
variable "ambiente" {
  default = "producao"
}
variable "numero_conta" {
  default = "611727732233"
}
provider "aws" {
  region = "us-east-2"
}