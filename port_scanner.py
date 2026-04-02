import socket
import threading
from queue import Queue

target = "100.115.95.206"
queue = Queue()
open_ports = []


# This helps us see progress
def worker():
    while not queue.empty():
        port = queue.get()
        # Print every 100 ports so you know it's alive
        if port % 100 == 0:
            print(f"--- Checking port {port}... ---")

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            # connect_ex returns 0 on success
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN!")
                open_ports.append(port)
            s.close()
        except:
            pass
        finally:
            queue.task_done()  # Tells the queue the job is finished


# 1. Fill Queue
for port in range(1, 1025):
    queue.put(port)

# 2. Start Threads
print(f"Starting scan on {target}...")
for _ in range(100):
    t = threading.Thread(
        target=worker, daemon=True
    )  # daemon=True stops threads if you Ctrl+C
    t.start()

# 3. Wait for Queue to be empty
queue.join()

print("-" * 30)
print(f"Scan Complete. Open ports: {open_ports}")
