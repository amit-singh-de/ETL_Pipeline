# ETL_Pipeline
This is a basic etl pipeline which uses Postgres,Airflow,Flask& Postgres.

## Steps to run ->
1. Do a git clone
2. setup docker and install docker compose
3. go the cloned directory, and run docker-compose up -d , you will 3 container running named airflow,pyspark and postgres
4. the containers will soon be started
5. to visit airflow , go to localhost:8080
6. to visit jupyter notebook , go to localhost:8888
7. for the flask application use localhost:5000
8. for postgres use localhost:5432
9. set up a new airflow connection name-> spark_api, host-> pyspark, port-> 5000 , then you are good to run the dag

## All the setup will be taken care automatically by docker-compose(pretty self-explanatory)


# ETL FLOW

user.csv(in the notebooks directory) --read & transform -->  Pyspark--load-->Postgres

# Requirements:

## Data Source:

Use the provided CSV file (users.csv) as the source data.
Sample users.csv structure:
csv
Copy code
id,first_name,last_name,email
1,John,Doe,john.doe@example.com
2,Jane,Smith,jane.smith@example.com
Transformation:

Create a new column in the dataset called hashed_email that contains the SHA-256 hash of the user's email address.
## Destination:
1.Use Apache Spark for ETL operations.
2.Load the transformed data into a PostgreSQL database.
3.Design the database schema appropriately for storing the user data.
## Docker:

1.Containerize your solution using Docker.
2.Write a Dockerfile to package your Spark application.
3.Use Docker Compose to set up the PostgreSQL database.
## Airflow:

1.Create an Apache Airflow DAG (Directed Acyclic Graph) to orchestrate the ETL process.
2.Schedule the DAG to run daily.
