// Docker Bake configuration file

// Default target
group "default" {
    targets = ["dev", "prod"]
  }
  
  // Variables
  variable "IMAGE_NAME" {
    default = "flask-service"
  }
  
  variable "IMAGE_TAG" {
    default = "latest"
  }
  
  // Development target
  target "dev" {
    dockerfile = "Dockerfile.dev"
    tags = ["${IMAGE_NAME}:dev", "${IMAGE_NAME}:dev-${IMAGE_TAG}"]
  }
  
  // Production target
  target "prod" {
    dockerfile = "Dockerfile.prod"
    tags = ["${IMAGE_NAME}:prod", "${IMAGE_NAME}:${IMAGE_TAG}"]
  }