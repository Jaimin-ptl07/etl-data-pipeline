# ETL Data Pipeline

## Project Overview

This ETL (Extract, Transform, Load) Data Pipeline project is designed to process streaming data using Apache Kafka and Apache Spark. The pipeline captures data from a Kafka topic, processes it in real-time, and allows for easy data access for machine learning applications. This project leverages Docker to create isolated environments for different services, ensuring smooth deployment and management.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the ETL Pipeline](#running-the-etl-pipeline)
- [Executing the Project](#executing-the-project)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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
