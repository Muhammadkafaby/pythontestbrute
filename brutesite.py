import requests
import threading

# Description: This is a brute force script
url = "https://camo.githubusercontent.com/add76353a9c954e6b6cc0e1d79d0825d08b96b85ef6e4728dc5b882029274d42/68747470733a2f2f76697369746f722d62616467652d64656e6f2e64656e6f2e6465762f4d7568616d6d61646b61666162792e4d7568616d6d61646b61666162792e737667"

# Counter to keep track of the number of requests
count = 0
lock = threading.Lock()

def send_request():
    global count
    while True:
        response = requests.get(url)
        with lock:
            count += 1
            print(f"Request {count}: Status Code {response.status_code}")

# Number of threads to use
num_threads = 1000000000

# Create and start threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()