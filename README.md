# Web_Services

Calculation of pi with two different communication systems. Client-Server and Master-Workers using Python, Flask, Rest API, http requests and Web Services. 

- Activate virtualenv
```
source bin/activate
```

- Install depedencies
```
pip install -r requirements.txt
```

- Run Client-Server
```
python3 servernum.py
python3 clientnum.py <number of steps>
```

- Run Master-Workers
```
python3 master_new.py
python3 worker_new.py

# hardcoded number of workers = 5. You can run all workers at the same time.
```

- Sample http requests for servernum.py
```
curl -XGET "localhost:3000/pi?numsteps=10000000"
```
