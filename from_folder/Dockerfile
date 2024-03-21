# The Spark version needs to agree with the version in ./spark/Dockerfile.spark-base, and also the version supported
# by Pathling: https://pathling.csiro.au/docs/server/configuration#spark-compatibility
# Update Jasmin
FROM jupyter/pyspark-notebook:spark-3.3.2
#FROM jupyter/pyspark-notebook:spark-3.3.0
# Use this if you need an ARM-based image:
# FROM jupyter/pyspark-notebook:aarch64-spark-3.3.0

# Update Jasmin https://archive.apache.org/dist/spark/spark-3.3.2/
ENV PATHLING_VERSION=6.2.1
ARG SPARK_SCALA_VERSION=2.12 
#2.13 test if datalake works with 2.12
ENV DELTA_LAKE_VERSION=2.3.0
# https://mvnrepository.com/artifact/ch.cern.sparkmeasure/spark-measure
ENV SPARKMEASURE_VERSION=0.23
#ENV PATHLING_VERSION=5.4.0
#ARG SPARK_SCALA_VERSION=2.12
#ENV SPARKMEASURE_VERSION=0.21

USER root
RUN echo "spark.jars.packages org.apache.spark:spark-sql-kafka-0-10_${SPARK_SCALA_VERSION}:${APACHE_SPARK_VERSION},au.csiro.pathling:library-api:${PATHLING_VERSION},ch.cern.sparkmeasure:spark-measure_2.13:0.21,io.delta:delta-core_${SPARK_SCALA_VERSION}:${DELTA_LAKE_VERSION}" >> /usr/local/spark/conf/spark-defaults.conf
#muss als comma-seperated list oben drüber rein
#RUN echo "spark.jars.packages ch.cern.sparkmeasure:spark-measure_2.13:0.22" >> /usr/local/spark/conf/spark-defaults.conf
#bin/pyspark --packages ch.cern.sparkmeasure:spark-measure_2.13:0.22
# https://pathling.csiro.au/docs/encoders#spark-cluster-configuration
USER ${NB_UID}
RUN /opt/conda/bin/pip install --quiet --no-cache-dir install pathling==${PATHLING_VERSION} && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" 

RUN /opt/conda/bin/pip install --quiet --no-cache-dir install sparkmeasure==${SPARKMEASURE_VERSION} && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" 

# This caches the download of the dependencies specified earlier.
RUN source /usr/local/bin/before-notebook.d/spark-config.sh 
#&& \
#   python -c "from pyspark.sql import SparkSession; SparkSession.builder.getOrCreate()"
