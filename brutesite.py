import threading
import time
import requests

url = "https://camo.githubusercontent.com/add76353a9c954e6b6cc0e1d79d0825d08b96b85ef6e4728dc5b882029274d42/68747470733a2f2f76697369746f722d62616467652d64656e6f2e64656e6f2e6465762f4d7568616d6d61646b61666162792e4d7568616d6d61646b61666162792e737667"
count = 0
num_threads = 10  # Number of threads to use

def send_requests():
    global count
    while count < 1000000000:
        response = requests.get(url)
        print(f"Request {count + 1}: Status Code {response.status_code}")
        count += 1
        time.sleep(1)  # Delay of 1 second between requests

threads = []

# Create and start threads
for i in range(num_threads):
    thread = threading.Thread(target=send_requests)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()