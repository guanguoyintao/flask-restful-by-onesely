import random
def verification_code():
    VerificationCode = ""
    for i in range(4):
        j = random.randrange(0,4)
        if j == 1:
            a = random.randrange(0,10)
            VerificationCode = VerificationCode + str(a)
        elif j == 2:
            a = chr(random.randrange(65,90))
            VerificationCode = VerificationCode + a
        else:
            a = chr(random.randrange(97,122))
            VerificationCode = VerificationCode + a
    return VerificationCode
