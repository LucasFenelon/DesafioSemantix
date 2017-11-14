from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import *

def nasa_main():
    spark = SparkSession.builder.master("local[2]").appName("nasaDataSets").getOrCreate()

    print "Execucao Dataset access_log_Aug95 ********************************************"
    examine_dataset(spark.sparkContext, "Documents/access_log_Aug95")
    print "Execucao Dataset access_log_Jul95 ********************************************"
    examine_dataset(spark.sparkContext, "Documents/access_log_Jul95")
    print "******************************************************************************"

def examine_dataset(sc, file):
    sql = SQLContext(sc)
    df = sql.read.format("csv").load(file)
    df_split = split(df["_c0"], " ")
    df = df.withColumn("host", df_split.getItem(0))
    df = df.withColumn("host2", df_split.getItem(1))
    df = df.withColumn("host3", df_split.getItem(2))
    df = df.withColumn("timestamp", df_split.getItem(3))
    df = df.withColumn("timestamp2", df_split.getItem(4))
    df = df.withColumn("request", df_split.getItem(5))
    df = df.withColumn("request2", df_split.getItem(6))
    df = df.withColumn("request3", df_split.getItem(7))
    df = df.withColumn("responseStatus", df_split.getItem(8))
    df = df.withColumn("countBytes", df_split.getItem(9))
    df = df.select("host",
                   "timestamp",
                   concat("request", "request2", "request3").alias("request"),
                   "responseStatus",
                   "countBytes",
                   substring("timestamp", 2, 11).alias("dia"))
    print 'contagem de hosts unicos eh %s' % (df.groupBy("host").count().filter("count = 1").count())
    print 'contagem de response status 404 eh %s' % (df.filter("responseStatus = 404").count())
    print 'soma de bytes eh %s' % (df.agg(sum("countBytes").cast("long")).rdd.first())
    print 'Quantidade de erros 404 por dia: '
    df.filter("responseStatus = 404").groupBy("dia").count().sort('dia', ascending=True).show(31)
    print 'As 5 URLs que mais causaram erro 404 foram: '
    df.filter("responseStatus = 404").groupBy("host").count().sort('count', ascending=False).limit(5).show()

if (__name__ == "__main__"):
    nasa_main()