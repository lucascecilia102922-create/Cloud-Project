provider "kubernetes" {}

resource "kubernetes_namespace" "loja_veloz" {
  metadata {
    name = "loja-veloz"
  }
}