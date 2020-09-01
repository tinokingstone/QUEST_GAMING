
module "LoadBalancer" {
  source              = "Azure/compute/azurerm"
  resource_group_name = azurerm_resource_group.dev_environment.name
  vm_hostname         = "LoadBalancer"

  public_ip_dns = ["${terraform.workspace}-load-balancer"]
  nb_public_ip  = "1"

  remote_port                   = "22"
  nb_instances                  = 1
  vm_os_publisher               = "Canonical"
  vm_os_offer                   = "UbuntuServer"
  vm_os_sku                     = "18.04-LTS"
  admin_password                = "colorMusic"
  admin_username                = "app-dev"
  vnet_subnet_id                = module.network.vnet_subnets[0]
  boot_diagnostics              = true
  delete_os_disk_on_termination = true
  nb_data_disk                  = 1
  data_disk_size_gb             = 30
  data_sa_type                  = "Premium_LRS"
  enable_ssh_key                = true
  ssh_key                       = "~/.ssh/id_rsa.pub"
  vm_size                       = "Standard_B1ms"

  tags = {
    environment = "dev"
    costcenter  = "it"
  }

  enable_accelerated_networking = false
}


output "LoadBalancer_vm_private_ips" {
  value = module.LoadBalancer.network_interface_private_ip
}


output "LoadBalancer_vm_public_ip" {
  value = module.LoadBalancer.public_ip_address
}

