import queue
import random
import string
import time

# Requests queue
requests_queue = queue.Queue()


generate_id = (
    lambda: f"#{''.join(random.choices(string.ascii_letters, k=3))}{random.randint(1000000, 9999999)}"
)

usleep = lambda x: time.sleep(x / 1000.0)


def generate_request():
    # Generate new requestId
    request_id = generate_id()
    # Add new request to queue
    requests_queue.put(request_id)
    print(f"Create new request: {request_id}")


def process_request():
    # Check if requests exists
    if not requests_queue.empty():
        # Remove next request from queue
        request_id = requests_queue.get()
        # Processing request
        print(f"Processing request: {request_id}")
    else:
        # Queue is empty
        print("Not found requests in queue")


try:
    while True:
        generate_request()
        process_request()
        # Pause between processing
        usleep(random.randint(500, 1000))
except KeyboardInterrupt:
    # Handle press Ctrl + C
    print("Exit")
