import os
import time
import threading
from multiprocessing import Process, Queue

# ======================
# Worker for Multiprocessing
# ======================
def worker(name):
    print(f"Process {name} running with PID: {os.getpid()}")

# ======================
# Functions for Multithreading
# ======================
def print_numbers():
    for i in range(5):
        print("Number:", i)
        time.sleep(0.5)

def print_letters():
    for ch in "ABCDE":
        print("Letter:", ch)
        time.sleep(0.5)

# ======================
# IPC using Queue (Inter-Process Communication) lets separate processes exchange data.
# ======================
def producer(q):
    for i in range(5):
        q.put(i)
        print("Produced:", i)

def consumer(q):
    while not q.empty():
        item = q.get()
        print("Consumed:", item)

# ======================
# Multithreading with Shared Memory
# ======================
counter = 0
lock = threading.Lock()  # For race condition safety

def increment():
    global counter
    for _ in range(1000):
        counter += 1  # Unsafe increment (may cause race condition)

def increment_safe():
    global counter
    for _ in range(1000):
        with lock:    # Safe increment
            counter += 1

# ======================
# Main execution
# ======================
if __name__ == "__main__":

    # ---- Single Process Example ----
    print("Single Process ID:", os.getpid())
    print("Hello from single process\n")

    # ---- Multiprocessing Example ----
    p1 = Process(target=worker, args=('A',))
    p2 = Process(target=worker, args=('B',))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Multiprocessing Finished\n")

    # ---- Multithreading Example ----
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Multithreading Finished\n")

    # ---- IPC using Queue ----
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p1.join()  # Wait producer

    p2.start()
    p2.join()  # Wait consumer

    print("IPC via Queue Finished\n")

    # ---- Multithreading Shared Memory ----
    # Unsafe increment
    counter = 0
    threads = [threading.Thread(target=increment) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("Counter value (unsafe):", counter)

    # Safe increment using Lock
    counter = 0
    threads = [threading.Thread(target=increment_safe) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("Counter value (safe with lock):", counter)




"""
Concise summary of the 5 topics:
---

## **1️⃣ Process**

* **Independent program** with its own memory and PID.
* True parallelism on multi-core CPUs.
* Crash in one process doesn’t affect others.
* Use `multiprocessing.Process` in Python.
* **Interview tip:** Know PID, memory isolation, starting/joining processes.

---

## **2️⃣ Thread**

* **Lightweight unit inside a process**.
* Shares memory with other threads → fast but can cause **race conditions**.
* Good for **I/O-bound tasks**.
* Python threads limited for CPU-bound tasks due to **GIL**.
* **Interview tip:** Difference between thread and process, use cases, GIL impact.

---

## **3️⃣ IPC (Inter-Process Communication)**

* Processes cannot share memory directly → use **Queue, Pipe, SharedMemory**.
* **Queue**: simple, thread/process safe.
* Allows **producer-consumer pattern**, message passing.
* **Interview tip:** Know how to safely exchange data between processes.

---

## **4️⃣ Shared Memory in Threads**

* Threads share process memory → can **read/write same variables**.
* Fast but may lead to **race conditions**.
* **Use Lock** for safe access.
* **Interview tip:** Race conditions vs locks, when to use `threading.Lock()`.

---

## **5️⃣ Race Conditions & Locks**

* **Race condition:** multiple threads access/modify same data → unpredictable results.
* **Lock:** ensures **mutual exclusion**, only one thread can access shared data at a time.
* Python: `threading.Lock()`, `with lock:` syntax.
* **Interview tip:** Explain problem, demonstrate safe vs unsafe increments.

---

### **Other things you should know related to these topics**

1. **Difference table:** Process vs Thread (memory, parallelism, communication, overhead).
2. **Synchronization primitives:** Besides Lock, know **RLock, Semaphore, Event, Condition**.
3. **Producer-Consumer pattern** — both with **threads and processes**.
4. **Deadlocks & starvation** (basic idea) — why locks can sometimes block threads forever.
5. **Python GIL** — impact on CPU-bound threads.
6. **Practical debugging tips:** `print`, logging, or `psutil` to check PIDs, memory, threads.

---
"""