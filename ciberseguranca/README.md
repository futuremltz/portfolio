# Cibersegurança — Portfólio

Projetos de segurança da informação com foco em defesa, detecção, análise e boas práticas: ferramentas próprias, laboratórios, auditorias autorizadas e investigações forenses.

Cada projeto fica em sua própria pasta, com README próprio descrevendo o objetivo, o ambiente de testes, os achados e as correções.

## Aviso ético

Todos os testes deste repositório foram feitos **apenas em ambientes próprios, laboratórios isolados ou plataformas criadas para treinamento** (TryHackMe, Hack The Box, PortSwigger Academy, DVWA, OWASP Juice Shop). O conteúdo tem fins educacionais e defensivos. Não use estas ferramentas em sistemas sem autorização por escrito.

## Projetos

| # | Projeto | Área | Ferramentas | Nível | Status |
| --- | --- | --- | --- | --- | --- |
| 01 | [Verificador de força de senha](./01-verificador-senha) | Criptografia / Privacidade | Python | Iniciante | Planejado |
| 02 | [Gerenciador de senhas local](./02-gerenciador-senhas) | Criptografia aplicada | Python / Rust | Iniciante/Intermediário | Planejado |
| 03 | [Writeups de CTF](./03-writeups-ctf) | Ofensiva e defensiva | Python, Bash | Iniciante | Planejado |
| 04 | [Homelab de segurança](./04-homelab) | Redes / Hardening | pfSense, Proxmox, Linux | Iniciante/Intermediário | Planejado |
| 05 | [Scanner de portas](./05-scanner-portas) | Redes | Python / Go | Intermediário | Planejado |
| 06 | [Analisador de logs](./06-analisador-logs) | Blue team | Python, SQL | Intermediário | Planejado |
| 07 | [SIEM caseiro](./07-siem-caseiro) | Monitoramento | Wazuh / Elastic, Docker | Intermediário | Planejado |
| 08 | [Honeypot com estatísticas](./08-honeypot) | Inteligência de ameaças | Cowrie, Python | Intermediário | Planejado |
| 09 | [Auditoria de app vulnerável](./09-auditoria-web) | Pentest web | Burp Suite, Python | Intermediário | Planejado |
| 10 | [Scanner de segurança para CI](./10-scanner-ci) | DevSecOps | Python, GitHub Actions | Intermediário/Avançado | Planejado |
| 11 | [Detector de intrusão (IDS)](./11-ids) | Análise de tráfego | Python + Scapy / Rust | Avançado | Planejado |
| 12 | [Análise forense de incidente](./12-analise-forense) | Forense digital | Volatility, Autopsy | Avançado | Planejado |
| 13 | [Hardening de servidor Linux](./13-hardening-linux) | Hardening | Lynis, Bash | Intermediário | Planejado |
| 14 | [Agregador de inteligência de ameaças](./14-threat-intel) | Inteligência de ameaças | Python, SQL | Intermediário | Planejado |
| 15 | [Detector de phishing](./15-detector-phishing) | ML defensivo | Python, scikit-learn | Intermediário | Planejado |
| 16 | [Auditoria de configuração de nuvem](./16-auditoria-nuvem) | Segurança em nuvem | Prowler, Terraform | Avançado | Planejado |
| 17 | [Laboratório Active Directory](./17-lab-active-directory) | Blue team | Windows Server, Wazuh | Avançado | Planejado |

> Status: **Planejado** → **Em andamento** → **Concluído**. Atualize a tabela conforme avança.

## Tecnologias

- **Linguagens:** Python, Bash, Go, Rust, C
- **Ferramentas:** Burp Suite, Wireshark, Nmap, Wazuh, Elastic Stack, Volatility, Autopsy
- **Infraestrutura:** Linux, Docker, Proxmox/VirtualBox, pfSense/OPNsense
- **Referências:** OWASP Top 10, MITRE ATT&CK

## Estrutura do repositório

```
ciberseguranca/
├── README.md                  ← este arquivo
├── 01-verificador-senha/
│   ├── README.md
│   ├── src/
│   └── tests/
├── 09-auditoria-web/
│   ├── README.md
│   └── relatorio.md           ← relatório no formato profissional
└── ...
```

## Padrão de cada projeto

1. **Objetivo** — o que o projeto protege, detecta ou investiga
2. **Ambiente** — onde foi testado (sempre isolado ou autorizado)
3. **Como funciona** — arquitetura e decisões técnicas
4. **Achados** — evidências, severidade e impacto
5. **Mitigação** — como corrigir ou se defender
6. **Aprendizados** — o que aprendi e próximos passos

> Nunca publique credenciais, chaves, dados pessoais reais ou IPs de terceiros. Revise com `git diff` antes de cada commit.

## Contato

- LinkedIn: [seu-perfil](https://linkedin.com/in/seu-perfil)
- E-mail: seu-email@exemplo.com
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
