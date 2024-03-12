# Data Loss Protection Service

This repository contains the codebase for the Data Loss Protection (DLP) service. The DLP service is designed to protect sensitive data from unauthorized access and loss. It's writen with python, uses postgresql, redis, fastapi and celery. Tested on macOs with python3.12. 

## Getting Started:

To begin working with the DLP service locally, follow these steps:
```
make init
```

It provide linters & formatters:
```
make lint
make pretty
make plint # (pretty + lint)
```

Also you can run tests:
```
make run_tests
```

To start on local machine:
```
make build
make prepare_local_run
make local_start
```

## Services:
Main service - FastAPI service. Its swagger on [http://127.0.0.1:8000/docs#]. It has 2 endpoints: 
1) /check_for_leaks - it receives message and then create tasks to search for leaks.
2) /get_all_leaks - it shows only leaks with in memory storage! Not usable for horizontall scaling.

Celery-worker - just a celery worker, which serves for finding leaks using regexps from redis.

Admin - flask-admin is used for adding regular expressions to search leakages with. Go to [http://127.0.0.1:8001/admin/dbregexprule/] and create some. In future releases you can see leakeges, they will be stored at database.

## How to use

After running on local machine you can start using this services.

First, you need to go to [http://127.0.0.1:8001/admin/] and add some regular expressions.

After that you can send messages to main-service using [http://127.0.0.1:8000/check_for_leaks]. You can use swagger for this: [http://127.0.0.1:8000/docs#]



## TODO:
1) write tests
2) add mypy
3) shrink docker image & get rid of passwords
4) add slack-service
5) add endpoint to check files for leakage
6) save results of leakage to db