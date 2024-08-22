# Exemplo - Rede e Conectividade - Comp Nuvem 2024
![](/arquitetura.png)

## Passos do Experimento

- Criar VPC (CIDR 10.50.00.00/16)
- Criar 2 instâncias EC2, nas subnets públicas. Reusar o SG launch-wizard-1, que libera a porta 8080 pra internet.
- Criar 2 instâncias RDS, em subnets privadas, cada qual com sua instância associada. Senha: `aulacn2024`.
- Fazer em cada EC2:
```sh
sudo yum update -y && sudo yum install git -y && \
git clone https://github.com/Pedro-V/aula-cn-experimento-redes.git && \
cd aula-cn-experimento-redes && \
./run.sh`
```
- Criar target group pras :8080 das 2 EC2s. Depois, criar um ALB. Liberar geral no SG do ALB.
- Testar.
- Simular queda de um alvo no target group.
- Clicar em "Reset" no painel do AWS Academy.
