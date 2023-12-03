from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sha2

def main():
    # Creating a Spark session
    spark = SparkSession.builder.appName("pipeline").getOrCreate()

    try:
        # Reading data
        file_path = "/home/jovyan/work/users.csv"
        df = spark.read.csv(file_path, header=True)

        # Your transformations or other operations with df
        # For example, convert 'id' column to integer
        df = df.withColumn("id", df["id"].cast("int"))

        # Adding a new column with hashed email address
        from pyspark.sql.functions import sha2, col
        df = df.withColumn("hashed_email", sha2(col("email"), 256))

        # Writing to PostgreSQL or other operations
        # For example, writing to PostgreSQL
        postgres_url = "jdbc:postgresql://postgres:5432/etl_pipeline"
        table_name = "users"
        postgres_properties = {
            "user": "postgres",
            "password": "postgres",
            "driver": "org.postgresql.Driver",
        }

        df.write \
            .format("jdbc") \
            .option("url", postgres_url) \
            .option("dbtable", table_name) \
            .option("user", postgres_properties["user"]) \
            .option("password", postgres_properties["password"]) \
            .option("driver", postgres_properties["driver"]) \
            .mode("overwrite") \
            .save()
        print("data loaded to postgres successfully")

    finally:
        # Stop the Spark session in a finally block to ensure it gets stopped even if an exception occurs
        if "spark" in locals():
            spark.stop()

if __name__ == "__main__":
    main()
