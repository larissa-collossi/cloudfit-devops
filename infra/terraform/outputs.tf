output "ec2_public_ip" {
  value = aws_instance.fitness_app.public_ip
}