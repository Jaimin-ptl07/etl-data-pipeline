# Base image
FROM openjdk:8-jdk-slim

# Install python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set environment variables for Spark and Kafka packages
ENV PYSPARK_PYTHON=python3
ENV SPARK_HOME=/opt/spark

# Install necessary Python packages
RUN pip3 install pyspark kafka-python

# Copy the Spark Kafka Streaming script to the container
COPY spark_kafka_streaming.py /app/spark_kafka_streaming.py

# Set the working directory
WORKDIR /Data Platform

# Command to run the Spark Kafka Streaming job
ENTRYPOINT ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:3.5.3", "spark_kafka_streaming.py"]
