import threading

global counter
counter = 0


lock = threading.Lock() # A simple lock

def increment_counter():
    # global counter
    # with lock: # Lock acquired here, released when exiting 'with'
    #     counter += 1
    counter += 1

threads = [threading.Thread(target=increment_counter) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter (should be 100): {counter}") # Without lock, might be < 100
