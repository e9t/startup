#! /usr/bin/python
# -*- coding: utf-8 -*-


# Change me (ex: /home/epark/dev/pkgs/spark-1.5.0-bin-hadoop2.6)
# You may also want to change py4j's path below
SPARK_HOME = ''


def start_spark(core=8, mem=1.5, driver_mem=1, executor_core=1):
    if not SPARK_HOME:
        raise Exception(\
            'Enter path for SPARK_HOME at the startup script `07-spark.py` to use spark')

    PYTHONPATH = ['%s/python' % SPARK_HOME,
                  '%s/python/lib/py4j-0.9-src.zip' % SPARK_HOME]
    PYTHONSTARTUP = '%s/python/pyspark/shell.py' % SPARK_HOME
    PYSPARK_SUBMIT_ARGS = '--driver-memory %dg ' % driver_mem +\
                          '--executor-memory %dm ' % int(mem*1024) +\
                          '--executor-cores %s ' % executor_core +\
                          '--total-executor-cores=%s pyspark-shell' % core

    os.environ['SPARK_HOME'] = SPARK_HOME
    os.environ['PYSPARK_SUBMIT_ARGS'] = PYSPARK_SUBMIT_ARGS
    sys.path.extend(PYTHONPATH)
    print(PYSPARK_SUBMIT_ARGS)
    execfile(PYTHONSTARTUP, globals())


def status_spark():
    if 'sc' in locals() and 'SparkContext' in sc.__repr__():
        print('Spark running')
        return True
    else:
        print('Spark not running')
        return False
