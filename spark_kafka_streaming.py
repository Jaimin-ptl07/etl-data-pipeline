from pyspark.sql import SparkSession

# Create Spark session with Kafka integration
spark = SparkSession.builder \
    .appName("KafkaStream") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "incoming-data") \
    .load()

# Process the stream
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Start the query
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
