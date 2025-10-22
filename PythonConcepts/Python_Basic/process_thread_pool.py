from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def square(n):
    return n*n


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1,2,3,4])
    submit_ = executor.submit(square, 10)
    as_comp_future = [executor.submit(square, i) for i in range(5)]

    for i in as_completed(as_comp_future):
        print(i.result())

    print(list(results))

executor = ThreadPoolExecutor(max_workers=2)
executor.submit(square, 5)
executor.shutdown(wait=True)

if __name__== "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        submit_ = executor.submit(square, 10)
        print(submit_.result())

        map_ = executor.map(square, [1,2,3,4,5,6])
        for i in map_:
            print(i, end=", ")



"""
---

| Feature             | Thread                              | Process                               | ThreadPoolExecutor / ProcessPoolExecutor                       |
| ------------------- | ----------------------------------- | ------------------------------------- | -------------------------------------------------------------- |
| **Memory**          | Shares memory with parent process   | Separate memory                       | Same as underlying type (thread or process)                    |
| **Parallelism**     | Limited for CPU-bound tasks (GIL)   | True parallelism on multi-core CPU    | Same as underlying type                                        |
| **Overhead**        | Light                               | Heavy                                 | Pool creates workers once and **reuses** them → lower overhead |
| **Crash impact**    | Can affect entire process           | Independent; other processes continue | Same as underlying type                                        |
| **Communication**   | Shared memory, use locks for safety | Needs IPC (Queue, Pipe, SharedMemory) | Same as underlying type                                        |
| **Task submission** | Manual thread creation              | Manual process creation               | Use `submit()`, `map()`, `as_completed()`                      |
| **Result handling** | Manual (shared list, queue)         | Manual (Manager, Queue)               | Automatically via **Future objects**                           |
| **Shutdown**        | Manual (join threads)               | Manual (join processes)               | Auto-shutdown with `with` statement or `shutdown()`            |
| **Best for**        | I/O-bound tasks                     | CPU-bound tasks                       | Same, but simplifies task management & reuse                   |

---

### **Key Takeaways**

1. **Threads:** Lightweight, share memory, good for I/O, limited CPU parallelism.
2. **Processes:** Heavy, separate memory, true CPU parallelism, need IPC for communication.
3. **Pools:** Reuse threads/processes, manage tasks and results easily, limit max workers, reduce overhead.
4. **Futures:** Provide safe and convenient access to task results, exceptions, and status.

---
"""
