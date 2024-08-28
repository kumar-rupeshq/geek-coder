# Databricks notebook source
# MAGIC %scala
# MAGIC
# MAGIC //val containerName=dbutils.secrets.get(scope="geekcoders-secret",key="containername1")
# MAGIC //val storageAccountName=dbutils.secrets.get(scope="geekcoders-secret",key="storageaccountname1")
# MAGIC //val sas=dbutils.secrets.get(scope="geekcoders-secret",key="sas")
# MAGIC val containerName="source"
# MAGIC val storageAccountName="gcodersstoragesource001"
# MAGIC val sas="sp=racwdl&st=2024-08-28T17:29:44Z&se=2024-11-09T01:29:44Z&spr=https&sv=2022-11-02&sr=c&sig=SKviOu8AqWiEQOb65ZnlJlPE%2BlNkZc6s%2BL5so%2FB5E9o%3D"
# MAGIC
# MAGIC val config="fs.azure.sas." + containerName + "." + storageAccountName + ".blob.core.windows.net"
# MAGIC
# MAGIC dbutils.fs.mount(source="wasbs://source@gcodersstoragesource001.blob.core.windows.net",
# MAGIC mountPoint="/mnt/raw_blob",
# MAGIC extraConfigs=Map(config -> sas))
# MAGIC

# COMMAND ----------

dbutils.secrets.get(scope="geekcoders-secret",key="containername")
