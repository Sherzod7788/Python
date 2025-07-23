## Homework 12
# Exercise 1: Threaded Prime Number Checker
# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

class PrimeCheckerThread(threading.Thread):
    def __init__(self, start, end, result_list):
        super().__init__()
        self.start_num = start
        self.end_num = end
        self.result_list = result_list

    def run(self):
        for num in range(self.start_num, self.end_num + 1):
            if is_prime(num):
                self.result_list.append(num)


def threaded_prime_checker(start_range, end_range, num_threads):
    threads = []
    primes_found = []


    primes_lock = threading.Lock()

    
    class ThreadSafeList(list):
        def append(self, item):
            with primes_lock:
                super().append(item)

    thread_safe_primes = ThreadSafeList()


    range_size = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        start = start_range + i * range_size
        
        end = end_range if i == num_threads - 1 else start + range_size - 1

        thread = PrimeCheckerThread(start, end, thread_safe_primes)
        threads.append(thread)
        thread.start()

   
    for thread in threads:
        thread.join()

    
    primes_found = sorted(thread_safe_primes)
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes_found)


if __name__ == "__main__":
    threaded_prime_checker(start_range=1, end_range=100, num_threads=4)

# 2.Exercise 2: Threaded File Processing
# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

import threading
from collections import Counter
import re


class WordCountThread(threading.Thread):
    def __init__(self, lines, result_dict, lock):
        super().__init__()
        self.lines = lines
        self.result_dict = result_dict
        self.lock = lock

    def run(self):
        local_counter = Counter()
        for line in self.lines:
            words = re.findall(r'\b\w+\b', line.lower())
            local_counter.update(words)
        
        with self.lock:
            for word, count in local_counter.items():
                self.result_dict[word] = self.result_dict.get(word, 0) + count


def threaded_file_word_counter(file_path, num_threads=4):
  
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    result_dict = {}
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread = WordCountThread(lines[start:end], result_dict, lock)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Word Occurrences Summary:")
    for word, count in sorted(result_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")


if __name__ == "__main__":

    with open("sample_text.txt", "w", encoding="utf-8") as f:
        f.write("Hello world\n" * 100)
        f.write("Python is fun\n" * 50)
        f.write("Threading is useful in Python\n" * 30)

    threaded_file_word_counter("sample_text.txt", num_threads=4)
