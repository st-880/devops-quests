# my first tera.. code

terraform {
    required_providers {
        random = {
            source = "hashicorp/random"
            version = "3.6.0"
        }
    }
}

resource "random_pet" "my_server" {
    length = 2
}
