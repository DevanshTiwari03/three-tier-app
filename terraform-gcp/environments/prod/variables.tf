variable "project_id" {
	description = "GCP project ID for the prod environment."
	type        = string
}

variable "region" {
	description = "GCP region for the prod environment."
	type        = string
	default     = "us-central1"
}

variable "zone" {
	description = "GCP zone for the prod environment."
	type        = string
	default     = "us-central1-a"
}

variable "vpc_name" {
	description = "Name of the prod VPC."
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
