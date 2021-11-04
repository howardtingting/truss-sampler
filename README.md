### Demo Test ###

```console
##### test.py uses sample-inputs directory, outputs to sample-outputs #####
user:~$ python3 test.py
```

##### Methods for pulling project #####

```console
##### method 1: run program using ./normalizer executable (indirectly uses python3) #####
user:~$ git clone https://github.com/howardtingting/truss-sampler.git
user:~$ cd truss-sampler
user:~/truss-sampler$ ./normalizer < sample.csv > out.csv
user:~/truss-sampler$ python3 normalizer.py < sample.csv > out.csv
```

```console
##### method 2: run using python3 #####
user:~$ git clone https://github.com/howardtingting/truss-sampler.git
user:~$ cd truss-sampler
user:~/truss-sampler$ ./normalizer < sample.csv > out.csv
user:~/truss-sampler$ python3 normalizer.py < sample.csv > out.csv
```

```console
##### method 3: use docker-compose #####
user:~$ git clone https://github.com/howardtingting/truss-sampler.git
user:~/Hashbabbler$ docker-compose up -d --build #builds container
user:~$ docker run -it truss_normalizer bash
root@xxxxx/app# ./normalizer < sample.csv > out.csv
```

```console
##### method 4: pull from docker hub #####
user:~$ docker pull howardtingting/truss-sampler:init
user:~$ docker run -it howardtingting/truss-sampler:init bash
root@xxxxx/app# ./normalizer < sample.csv > out.csv
```


