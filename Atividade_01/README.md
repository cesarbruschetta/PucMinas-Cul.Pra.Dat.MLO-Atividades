# Atividade 01

## Objetivo: 
ETL utilizando o Pyspark.

## Etapas a serem desenvolvidas:

- [Download do arquivo](./iris.txt)
- Criar uma task pre-processamento para validar se os dados se encontram no formato correto utilizando Pyspark:

    - sepal_length range( 4.3,7.9)
    - sepal_width range(2.0,4.4)
    - petal_length range(1.0,6.9)
    - petal_width range(0.1,2.5)
    - classEncoder range(0,2)
    - class ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

- Utilizar a lib `pydeequ` para gerar o data quality report. (Gerar o report após a leitura do arquivo e após ter realizado o tratamento dos dados.)

- Criar dataset tratado no formato parquet.

## OBD

- Todos os dados que não se encontram no formato ou range correto devem ser excluídos do dataset.
- Criar um arquivo com os registros removidos contendo a mensagem do erro conforme exemplo:

```csv
sepal_length,sepal_width,petal_length,petal_width,class,classEncoder,messageError
5.1,3.5,1.4,0.2,Iris-setosa,0, sepal_width maior que 4.4
```