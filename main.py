# Bitcoin Protocol: Proof of Work

import string
import random
import hashlib
import time

example_challenge = '9j122sdf4i9028uedioiu353ee'


def generation(challenge=example_challenge, size=25):
    # make a random string of size 26
    answer = ''.join(random.choice(string.ascii_lowercase +
                                   string.ascii_uppercase +
                                   string.digits) for x in range(size))
    attempt = challenge + answer
    return attempt, answer


def testAttempt():
    found = False
    start = time.time()
    attemptCount = 0

    # start mining
    while not found:
        # create a new hash
        attempt, answer = generation()
        shaHash = hashlib.sha256(str(attempt).encode('utf-8'))
        solution = shaHash.hexdigest()

        # mining difficulty is changed by altering the number of starting zero bits
        if solution.startswith('000'):
            print('Attempt successful!')
            print('================================================================')
            print('Attempt: ' + str(attemptCount))
            timeTook = time.time() - start
            print(solution)
            print('Answer: ' + answer)
            print('Time took: ' + str(timeTook))
            print('================================================================')
            found = True
        else:
            print('Not successful')
            print('================================================================')
            print('Attempt: ' + str(attemptCount))
            timeTook = time.time() - start
            print(solution)
            print('Time:' + str(timeTook))
            attemptCount += 1
            print('================================================================')

    return answer


testAttempt()
