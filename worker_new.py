import requests
import json

def calcPartialSum(start, stop, step):
    """ Leibniz formula for arctan(1) = pi/4 """
    mysum = 0
    for i in range(start, stop):
        x = (i + 0.5) * step
        mysum += 4.0 / (1.0 + x**2)

    return mysum


def main():
    # GET steps
    response = requests.get("http://localhost:2000/block_info")
    # extract start, stop, step from response
    block_info = json.loads(response.text)
    print(block_info)
    psum = calcPartialSum(block_info["start"],block_info["stop"],block_info["step"]) 
    sum = str(psum)

    # POST sum
    response = requests.post("http://localhost:2000/result", data=sum)

    print(f"sent: {sum}") # to keep track of work

if __name__ == '__main__':
    main()