def is_prime(number):
    count = 0
    for i in range(2,number):
        if number %i == 0:
            count += 1
    if count != 0: return False

    else: return True
print(is_prime(22))