# Bitcoin Protocol: Proof of Work

import string
import random
import hashlib

example_challenge = '9j122sdf4i9028uedioiu353ee'


def generation(challenge=example_challenge, size=25):
    # make a random string of size 26
    answer = ''.join(random.choice(string.ascii_lowercase +
                                   string.ascii_uppercase +
                                   string.digits) for x in range(size))
    attempt = challenge + answer
    return attempt, answer


def testAttempt():
    attempt, answer = generation()

    # shaHash.update(attempt)
    # solution = shaHash.hexdigest()
    shaHash = hashlib.sha256(str(attempt).encode('utf-8'))
    solution = shaHash.hexdigest()

    if solution.startswith('000'):
        print("Mine successful!")
        print(solution)

for x in range(0,10000):
    testAttempt()

testAttempt()
