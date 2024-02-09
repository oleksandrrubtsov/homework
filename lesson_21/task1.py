import time

class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()

        total_time = end_time - self.start_time

        print(f"Час початку виконання: {self.start_time}")
        print(f"Час завершення виконання: {end_time}")
        print(f"Загальний час виконання: {total_time} секунди")


with TimerContextManager():
    for _ in range(100):
        pass

        
