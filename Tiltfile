# -*- mode: Python -*-

docker_build('cs50w-image', '.')
k8s_yaml('kubernetes.yml')
k8s_resource('cs50w', port_forwards=8000)
