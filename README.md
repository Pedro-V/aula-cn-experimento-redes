# Passos do Experimento

1. Criar VPC (CIDR 10.50.00.00/16)
2. Criar 2 instâncias EC2, nas subnets públicas. Reusar o SG launch-wizard-1, que libera a porta 8080 pra internet.
3. Criar 2 instâncias RDS, em subnets privadas, cada qual com sua instância associada. Senha: `aulacn2024`.
4. Fazer em cada EC2:
  - `sudo yum update -y && sudo yum install git -y`
  - `git clone https://github.com/Pedro-V/aula-cn-experimento-redes.git`
  - `cd aula-cn-experimento-redes`
  - `./run.sh`
5. Criar target group pras :8080 das 2 EC2s. Depois, criar um ALB. Liberar geral no SG do ALB.
6. Testar.
7. Simular queda de um alvo no target group.
8. Derrubar tudo.
