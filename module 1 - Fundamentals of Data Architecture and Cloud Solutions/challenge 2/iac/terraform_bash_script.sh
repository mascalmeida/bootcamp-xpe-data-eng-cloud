# Script to run the terraform solution
## terraform initialization
echo -e ">> terraform initialization <<<\n"
terraform init
## format the terraform structure
echo -e "\n>> format the terraform structure <<<\n"
terraform fmt
## validate the terraform code
echo -e "\n>> validate the terraform code <<<\n"
terraform validate
## create the plan to deploy
echo -e "\n>> create the plan to deploy <<<\n"
terraform plan
## apply the terraform code to create the strucutre
echo -e "\n>> apply the terraform code to create the strucutre <<<\n"
terraform apply -auto-approve
## destroy (delete) everything
#echo -e "\n>> destroy (delete) everything <<<\n"
#terraform destroy -auto-approve

echo -e "\n>> finish... bye-bye <<<"