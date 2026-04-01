# Especificação da imagem Docker
FROM python:3.12.3-alpine

# Dependências Linux necessárias
RUN apk add --no-cache \
    build-base \
    linux-headers

# Diretório de trabalho
WORKDIR /usr/src/app

# Copiar os arquivos da aplicação e as dependências
COPY . /usr/src/app
COPY requirements.txt /usr/src/app

# Instalar dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pelo Gunicorn
EXPOSE 5000

ENV PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus
RUN mkdir -p /tmp/prometheus

# Configurar o comando de inicialização do Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app.app:app"]