import threading
import random
import time




def delayed_function():
    print("Початок виконання функції...")
    time.sleep(1)  
    print("Функція завершила виконання!")

def main():
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=delayed_function)
        thread.start()  
        threads.append(thread)
    
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()







