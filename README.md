# Monitoramento e Observabilidade em DevOps

Repositório base para o desenvolvimento de um ambiente de monitoramento e observabilidade de uma aplicação Python+Flask com Prometheus e Grafana.

Monitoramento e observabilidade são pilares essenciais em qualquer estratégia DevOps.
Enquanto o **monitoramento** se concentra em coletar e exibir métricas predefinidas (como uso de CPU, memória, e tempo de resposta), a **observabilidade** vai além, permitindo entender o estado interno do sistema com base em logs, métricas e traces.
Juntos, esses conceitos ajudam a identificar, diagnosticar e resolver problemas de forma proativa, aumentando a confiabilidade e a eficiência de sistemas em produção.

## Prometheus e Grafana

**Prometheus** é uma ferramenta de monitoramento open-source amplamente utilizada em ambientes DevOps. Ele coleta métricas em tempo real de sistemas e serviços, armazenando-as em um banco de dados orientado a séries temporais. É ideal para criar alertas baseados em condições configuradas.

**Grafana**, por outro lado, é uma ferramenta de visualização que se conecta a diversas fontes de dados, incluindo Prometheus. Ele permite criar dashboards interativos para analisar métricas e dados em tempo real, tornando-o uma ferramenta essencial para a observabilidade.

A combinação de **Prometheus e Grafana** nos permite:

- Coletar métricas detalhadas de aplicações e infraestrutura;
- Configurar alertas para condições anormais;
- Visualizar e analisar dados de forma clara e personalizada.

## Exercícios Propostos

1. **Coleta de Métricas**:
Configurar o uso do `prometheus_flask_exporter`¹ para expor métricas da aplicação Flask ao Prometheus.

2. **Conexão com Grafana**:
Configurar o Grafana para usar o Prometheus como fonte de dados².

3. **Criação de um Dashboard**:
Elaborar um dashboard simples no Grafana, que exiba ao menos três métricas das requisições HTTP, coletadas pela aplicação, como tempo de resposta, requisições com sucesso (status code 200) e requisições com erro (em nossa aplicação, status code 400).

¹[Documentação prometheus_flask_exporter](https://github.com/rycus86/prometheus_flask_exporter)

²[Documentação Integrando Prometheus e Grafana](https://grafana.com/docs/grafana/latest/datasources/prometheus/configure-prometheus-data-source/)

## Executando a Aplicação

O ambiente completo já está configurado com `docker-compose`, bastando executar o comando:

```
docker-compose up --build
```

- A aplicação responderá nas seguintes rotas: 
   - http://localhost:5000/health-check (HTTP 200, OK)
   - http://localhost:5000/hello?name=guijac (HTTP 200, OK)
   - http://localhost:5000/hello (HTTP 400, Bad Request)
- O Prometheus estará disponível em: http://localhost:9090
- O Grafana estará disponível em: http://localhost:3000 (credenciais padrão: admin / admin).