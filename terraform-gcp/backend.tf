resource "google_compute_instance" "vm" {

  name = "terraform-vm"

  machine_type = "e2-micro"

  zone = "us-central1-a"

  boot_disk {

    initialize_params {

      image = "debian-cloud/debian-12"
    }
  }

  network_interface {

    network = "default"

    access_config {}
  }
}
terraform {

backend "gcs" {
  bucket = "rishi-terraform-state-1234"
  prefix = "terraform/state"
}

}

resource "google_compute_network" "vpc-1"{
  name=  "vpc-1"
  
}


