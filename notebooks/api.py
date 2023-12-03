from flask import Flask
import subprocess

app = Flask("spark")

@app.route('/submit_spark_job')
def submit_spark_job():
    command = [
        'spark-submit',
        '--master', 'local[*]',
        '--name', 'arrow-spark',
        '--jars', '/home/jovyan/work/postgresql-42.2.27.jre7.jar',
        '/home/jovyan/work/pipeline.py'
    ]
    
    subprocess.run(command)
    
    return 'Spark job submitted successfully!'

if __name__ == '__main__':
    print("pyspark api is starting")
    app.run(host='0.0.0.0', port=5000)
    print("pyspark api is running")
