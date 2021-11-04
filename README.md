### 1. Methods for running project ###
##### method 1: run executable #####
```console
user:~/truss-sampler$ ./normalizer < sample.csv > out.csv
```
##### method 2: run normalizer.py #####
```console
user:~/truss-sampler$ python3 normalizer.py < sample.csv > out.csv
```
##### method 3: test.py; inputs from sample-inputs, outputs to sample-outputs #####
```console
user:~/truss-sampler$ python3 test.py
```

### 2. Methods for pulling project for usage ###
##### method 1: run directly after pull #####
```console
user:~/truss-sampler$ ./normalizer < sample.csv > out.csv
```
##### method 2: use docker-compose #####
```console
user:~/truss-sampler$ docker-compose up -d --build
user:~/truss-sampler$ docker run -it truss_normalizer bash
root@xxxxx/app# ./normalizer < sample.csv > out.csv
```
##### method 3: pull from docker hub #####
```console
user:~$ docker pull howardtingting/truss-sampler:latest
user:~$ docker run -it howardtingting/truss-sampler:latest bash
root@xxxxx/app# ./normalizer < sample.csv > out.csv
```
