import shlex
from test_functions import validate_passport

expected_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
exception_keys = ['cid']

def run_task(INPUT):

    with open(INPUT) as f:
        content = [line[0:-1] for line in f]

    content.append('') #appending a null ending to list to end the loop

    count_task1 = 0
    count_task2 = 0
    my_dict = {}

    for line in content:
        my_dict.update(dict(token.split(':') for token in shlex.split(line)))
    
        if not line: 
            missing_key = list(set(expected_keys)-set(list(my_dict.keys())))
            if not missing_key:
                count_task1 += 1
                if validate_passport(my_dict):
                    count_task2 += 1
                            
            else:
                pass
            my_dict = {}
    return count_task1, count_task2


def run_tests():

    cnt1, cnt2 = run_task('test.txt')
    if cnt1 == 2: print("Task 1 test passed")

    cnt1, cnt2 = run_task('passport_true.txt')
    if cnt2 == 4: print("Task 2 passport validity passed")

    cnt1, cnt2 = run_task('passport_false.txt')
    if cnt2 == 0: print("Task 2 passport invalidity passed")


if __name__ == "__main__":

    run_tests()
    INPUT = "input.txt"
#    INPUT = "passport_true.txt"
    task1, task2 = run_task(INPUT)

    print(f'Task 1 count:{task1}\nTask 2 count:{task2}')
