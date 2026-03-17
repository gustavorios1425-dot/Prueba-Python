# Este es nuestro archivo de configuración para Bake
target "default" {
    dockerfile = "Dockerfile"
    context = "."
    tags = ["galactic10/mi-python-app:latest"]
}
