import queues as qs
import time

def main():

    bq = qs.BoundedQueue(50_000)
    for i in range(50_000):
        bq.enqueue(i)

    cq = qs.CircularQueue(50_000)
    for i in range(50_000):
        cq.enqueue(i)

    start_bq = time.time()
    for _ in range(50_000):
        bq.dequeue()
    end_bq = time.time()
    timeInterval_bq = end_bq - start_bq
    print(f"For Bounded Queue, the total runtime of dequeueing 50,000 items is {timeInterval_bq:6.4} seconds.")

    start_cq = time.time()
    for _ in range(50_000):
        cq.dequeue()
    end_cq = time.time()
    timeInterval_cq = end_cq - start_cq
    print(f"For Circular Queue, the total runtime of dequeueing 50,000 items is {timeInterval_cq:6.4} seconds.")


if __name__ == '__main__':
    # main()
    cq = qs.CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(11)
    a = cq.dequeue()
    print(a)
    # print(cq)
