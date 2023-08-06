.. meta::
    :description: Kafka admin via AWS CloudFormation
    :keywords: AWS, CloudFormation, Kafka, Confluent

====================
Kafka Admin Provider
====================

Tool / Lib to transform a simply defined set of kafka topics and transforms the definition into an AWS CloudFormation
template that uses either EWS::Kafka::Topic or Custom::KafkaTopic (via AWS Lambda deployed in your account) to
create/updated/delete your Kafka topics.


Installation
==============

.. code-block:: bash

   python3 -m pip install aws_cfn_kafka_admin_provider


Usage
=======

As CLI
-------

.. code-block:: bash


    aws-cfn-kafka-admin-provider --help
    usage: aws-cfn-kafka-admin-provider [-h] -f FILE_PATH [-o OUTPUT_FILE] [--format {json,yaml}] [_ ...]

    positional arguments:
      _

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE_PATH, --file-path FILE_PATH
                            Path to the kafka definition file
      -o OUTPUT_FILE, --output-file OUTPUT_FILE
                            Path to file output
      --format {json,yaml}  Template format


As lib
-------

.. code-block:: python

    from aws_cfn_kafka_admin_provider.aws_cfn_kafka_admin_provider import KafkaStack

    stack = KafkaStack("/path/to/input/file.yaml")
    stack.render_topics()


Render models
===============

.. code-block:: bash

    # Through makefile
    make data-model

    # Via CLI with

    datamodel-codegen --input-file-type jsonschema \
        --input aws-cfn-kafka-admin-provider-schema.json \
        --output aws_cfn_kafka_admin_provider/model.py

Credits
========

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
