
num = 5
user = 100

def algo(target_num, user_num):
    if target_num > user_num/2:
        print("Greater Please..")
        algo(target_num,((user_num/2)))
    elif target_num < user_num/2:
        print("Smaller Please..")
        algo()

# I was making this and stuck here where i am checking weather if the both halfs are greater or smaller and cant figure out what next