terraform {
  required_providers {
    google = {
        source = "hashicorp/google"
        version = "7.32.0"
    }
  }
}
provider "google" {
  # Configuration options
  project = "shared-project-497814"
  region  = "us-central1"
  zone    = "us-central1-a"  
 
  
}