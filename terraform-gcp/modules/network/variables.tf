variable "project_id" {
	description = "GCP project ID where the VPC will be created."
	type        = string
}

variable "vpc_name" {
	description = "Name of the VPC network."
	type        = string
}

variable "auto_create_subnetworks" {
	description = "Creates a standard auto mode VPC when true."
	type        = bool
	default     = true
}

variable "routing_mode" {
	description = "The network-wide routing mode to use."
	type        = string
	default     = "REGIONAL"
}

variable "delete_default_routes_on_create" {
	description = "Whether to delete default internet routes when the VPC is created."
	type        = bool
	default     = false
}
