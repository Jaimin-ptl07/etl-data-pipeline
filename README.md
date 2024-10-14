# ETL Data Pipeline

## Project Overview

This ETL (Extract, Transform, Load) Data Pipeline project is designed to process streaming data using Apache Kafka and Apache Spark. The pipeline captures data from a Kafka topic, processes it in real-time, and allows for easy data access for machine learning applications. This project leverages Docker to create isolated environments for different services, ensuring smooth deployment and management.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the ETL Pipeline](#running-the-etl-pipeline)
- [Usage](#usage)

## Technologies Used

- **Apache Kafka**: For managing real-time data streams.
- **Apache Spark**: For processing streaming data.
- **Docker**: For containerization of services.
- **Python**: For scripting the ETL process.
- **Git**: For version control.

## Project Structure

```plaintext
ETL-Data-Pipeline/
│
├── docker-compose.yml
├── Dockerfile
├── spark_kafka_streaming.py
├── kafka_producer.py
└── kafka_consumer.py
```
## Setup Instructions

### Clone the Repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/your-username/etl-data-pipeline.git
cd etl-data-pipeline
```

**Install Docker**
Ensure you have Docker and Docker Compose installed on your machine. You can download Docker from the official Docker website.

**Build the Docker Images**
Navigate to the project directory and build the Docker images:
```bash
docker-compose build
```

**Run the Docker Containers**
Start the ETL pipeline and its dependencies:
```bash
docker-compose up
```

## Running the ETL Pipeline

**Step 1: Start the Docker Services**
Open your terminal and navigate to the project directory. 
Run the following command to start the services:

```bash
docker-compose up
```
This command will start Zookeeper, Kafka, and Spark services as defined in the docker-compose.yml file.

**Step 2: Open a New Terminal for Data Production**
In a new terminal window (leave the first terminal running), execute the following command to run the Kafka producer:
```bash
docker exec -it etl-data-pipeline_etl_1 python kafka_producer.py
```
This will simulate data production, sending messages to the Kafka topic defined in your producer script.

**Step 3: Start the Spark Streaming Job**
In the terminal where you started the Docker services, the Spark streaming job (spark_kafka_streaming.py) will automatically start consuming messages from Kafka once the containers are up.

**Step 4: Monitor Spark UI**
Access the Spark UI at http://localhost:8080 to monitor the Spark job and see the streaming data processing in real-time.

## Usage
The pipeline will continuously process streaming data from Kafka. You can modify the producer and consumer scripts to change the data being sent and processed.

