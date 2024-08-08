import time
start_time = time.time()

target_num = 4500000


for i in range(1,1000000000000):
    if i == target_num:
        print(f"The number was {i}")
        break
    else:
        print(f"Current {i}")
        i += 1

print("--- %s seconds ---" % (time.time() - start_time))