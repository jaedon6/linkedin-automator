import time
import concurrent.futures
from methods import withdrawl, fetch_urns


t1 = time.perf_counter()

fetch_urns()

with open("entityURNs.txt", "r") as file:
    global urns
    urns = file.read().splitlines()


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(withdrawl, urns)

    for result in results:
        print(result)

t2 = time.perf_counter()

print(f"\t\nCompleted Process in {round(t2-t1)} second(s)")
