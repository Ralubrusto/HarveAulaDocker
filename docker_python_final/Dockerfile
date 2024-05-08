# Insira aqui o comando FROM 
FROM python:3.10.14-slim

RUN pip install mysql-connector-python

# Insira aqui o comando COPY
COPY main.py .
COPY connector.py .

# Insira aqui o comando CMD
CMD ["python", "main.py"]