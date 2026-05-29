output "vpc_id" {
	description = "The ID of the dev VPC."
	value       = module.network.vpc_id
}

output "vpc_name" {
	description = "The name of the dev VPC."
	value       = module.network.vpc_name
}

output "vpc_self_link" {
	description = "The self link of the dev VPC."
	value       = module.network.vpc_self_link
}
