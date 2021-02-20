from threading import Thread, Lock
from flask import Flask, request
from flask_restful import Resource, Api, reqparse 
import json
import time
import os 

WORKERS_COUNT = 5
NUM_STEPS = 100000000
STEP = 1.0 / NUM_STEPS
BLOCK_COUNT = int(NUM_STEPS / WORKERS_COUNT)

class Shared_data:
    registered_worker_count = 0 # workers that have assigned their block
    sum = 0.0
    mutex = Lock()
    responded_worker_count = 0 # workers that have responded with a result

app = Flask(__name__)
api = Api(app)

data = Shared_data()

@app.route('/block_info')    
def steps():
    global data, WORKERS_COUNT, NUM_STEPS
    start = data.registered_worker_count * BLOCK_COUNT
    stop = start + BLOCK_COUNT
    if data.registered_worker_count == WORKERS_COUNT : stop = NUM_STEPS
    data.mutex.acquire()
    data.registered_worker_count += 1
    data.mutex.release()    
    resp = {"step": STEP, "start": start, "stop": stop}
    return json.dumps(resp)

@app.route('/result', methods = ['POST'])
def results():
    global data, WORKERS_COUNT, NUM_STEPS
    print("pid ",os.getpid())
    partial_sum = float(request.data)
    print("partial_sum: ",partial_sum)

    data.mutex.acquire()
    data.sum += partial_sum
    data.responded_worker_count += 1
    data.mutex.release()    
    
    print("responded_worker_count: ",data.responded_worker_count)
    if data.responded_worker_count >= WORKERS_COUNT:
        pi_calc()
        endTime = time.time()
        print(f"All workers ({WORKERS_COUNT}) responded, start again")
        print(f"Time elapsed {endTime-startTime} seconds")
    elif data.responded_worker_count < WORKERS_COUNT: 
        print("waiting for the other workers..")
    return "ok" 

# final calculation 
def pi_calc():
    global data, STEP    
    result = data.sum * STEP
    print (f"pi = {result} with {NUM_STEPS} numsteps")
    
if __name__ == '__main__':
    startTime = time.time()
    app.run(host="0.0.0.0",port=2000,debug=True,threaded=True,processes=1)