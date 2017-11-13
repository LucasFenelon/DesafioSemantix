# DesafioSemantx

# Spark (Windows)
  Saudações, para o completo funcionamento desse teste, temos algumas diretivas a serem seguidas:
    1 - Instalação do Python 2.7 (O arquivo para este fim se encontra na pasta Documents "python-2.7.amd64.msi")
    2 - Configuração de duas variáveis de ambiente:
      SETX PYTHON="C:/Python27"
      SETX PATH=$PATH;$PYTHON
    3 - Instalação do PIP através do comando(CMD) "python get-pip.py" (O arquivo para este fim se encontra na pasta Documents)
    4 - Atualização do PIP pelo comando(CMD) pip "python -m pip install -u pip"
    5 - Instalação da biblioteca pyspark pelo comando(CMD) pip "python -m pip install -u pyspark"
    6 - Download do Spark 2.2 no site "https://spark.apache.org/downloads.html"
    7 - Descompactar na pasta "C:/Spark2.2" e configuras as variaveis de ambiente:
      SETX SPARK_HOME="C:/Spark2.2"
      SETX PATH=$PATH;$SPARK_HOME/bin
    8 - Configurar Hadoop local, mover o arquivo "winutils.exe" da pasta Documents para a pasta local "C:/winutils"
    9 - Configurar variaveis de ambiente para o Hadoop:
      SETX HADOOP_HOME="C:/winutils"
      SETX PATH=$PATH;$HADOOP_HOME
    10 - Descompactar os datasets na própria pasta Documents e executar o código do teste pelo comando(CMD) "python nasa_main.py"
