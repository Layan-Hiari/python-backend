import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"\nRunning '{func.__name__}'...")

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' took {duration:.4f} seconds.")

        
        with open("execution_log.txt", "a") as log_file:
            log_file.write(f"{func.__name__} ran in {duration:.4f} seconds\n")

        return result
    return wrapper


@log_execution_time
def download_simulation():
    print("Simulating download...")
    time.sleep(3)
    print("Download complete.")

@log_execution_time
def calculation_simulation():
    print("Simulating calculation...")
    time.sleep(1.5)
    print("Calculation complete.")


if __name__ == "__main__":
    download_simulation()
    calculation_simulation()
