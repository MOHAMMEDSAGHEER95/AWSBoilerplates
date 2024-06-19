provider "aws" {
  region = "eu-west-2"
}

resource "aws_dynamodb_table" "ecommerce" {
  name         = "ecommerce"
  billing_mode = "PAY_PER_REQUEST"

  hash_key     = "PK"
  range_key    = "SK"

  attribute {
    name = "PK"
    type = "S"
  }

  attribute {
    name = "SK"
    type = "S"
  }

  tags = {
    Name        = "ecommerce"
    Environment = "Production"
  }
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.ecommerce.name
}
