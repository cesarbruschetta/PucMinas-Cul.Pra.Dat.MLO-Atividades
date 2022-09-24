# Atividade 02

## Objetivo: 

Orquestrar todo o fluxo de processamento necessários para execução de um modelo de machine learning utilizando o airflow.

## Etapas a serem desenvolvidas:

- Criar uma task etl responsável pela leitura do arquivo Iris tratado (Atividade 01) e utilize a lib pandas-schema para verificar se os dados estão no formato correto. Se o arquivo estiver correto continuar para a próxima task e em caso de erro pausar o processamento e enviar mensagem de erro.
    - sepal_length range( 4.3,7.9)
    - sepal_width range(2.0,4.4)
    - petal_length range(1.0,6.9)
    - petal_width range(0.1,2.5)
    - classEncoder range(0,2)
    - class ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

- Criar uma task de grupo que contenha:
    - Execução algoritmo1 de ML para o dataset Iris
    - Execução algoritmo2 de ML para o dataset Iris
      
## OBS1: 

- O processamento deve ser realizado de forma paralela
- Utilizar o MLFlow para gerenciar os modelos criados

