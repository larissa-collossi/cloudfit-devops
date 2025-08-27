output "ec2_public_ip" {
  value = aws_instance.cloudfit_instance.public_ip
}