from time import perf_counter
import sys
def fib(num:int):
    return 0 if num <= 0 else fib(num-1) + fib(num-2)
def main():
    target_number_index = sys.argv[1] if len(sys.argv[1:]) else 50
    start = perf_counter()
    print(fib(50))
    print(f"time taken: {perf_counter()-start:.4f} seconds")
if __name__ == "__main__":
    main()