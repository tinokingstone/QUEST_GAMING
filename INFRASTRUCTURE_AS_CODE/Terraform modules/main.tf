
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "dev_environment" {
  name     = "${terraform.workspace}-environment"
  location = "uk south"
}


module "network" {
  source              = "Azure/network/azurerm"
  version             = "3.0.1"
  resource_group_name = azurerm_resource_group.dev_environment.name
  subnet_prefixes     = ["10.0.1.0/24"]
}
