# Multithreading is using multiple threads to handle different subprocesses concurrently.

# This is good for handling multiple IO bound tasks simultaneously.
# The interpreter would easily switch context between threads when one is blocked by IO operation

# Advantage: Threads use less memory than creating multiple processes

import threading
import time

def download(url):
    print(f"Starting download: {url}")
    time.sleep(2)  # Simulate download time
    print(f"Finished download: {url}")

urls = ["url1", "url2", "url3"]

threads = []
for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All downloads completed")

# This simpler way to use multithreading in Python:
# Use the ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    executor.map(download, urls)