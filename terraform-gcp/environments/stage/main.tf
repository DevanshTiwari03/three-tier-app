terraform {
	required_providers {
		google = {
			source  = "hashicorp/google"
			version = "7.32.0"
		}
	}
}

provider "google" {
	project = var.project_id
	region  = var.region
	zone    = var.zone
}

module "network" {
	source = "../../modules/network"

	project_id                      = var.project_id
	vpc_name                        = var.vpc_name
	auto_create_subnetworks         = var.auto_create_subnetworks
	routing_mode                    = var.routing_mode
	delete_default_routes_on_create = var.delete_default_routes_on_create
}
