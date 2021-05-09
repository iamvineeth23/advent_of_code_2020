import re

def check_byr(data):
    
    if len(data) == 4:
    
        try:
            num = int(data)
    
            if 1920 <= num <= 2002:
                return True

        except:
            return False
    
    return False



def check_iyr(data):

    if len(data) == 4:
    
        try:
            num = int(data)
    
            if 2010 <= num <= 2020:
                return True

        except:
            return False
    
    return False
    

def check_eyr(data):
    if len(data) == 4:

        try:
            num = int(data)
            if num >=2020 and num <= 2030:
                return True

        except:
            return False

    return False


def check_hgt(data):

    try:
        num = int(data[:-2])
        unit = data[-2:]

        
        if unit == 'cm':
            
            if num >= 150 and num <= 193:

                return True
            else:
                return False

        elif unit == 'in':
            
            if  num >= 59 and num <= 76:
                return True
            else:
                return False
        else:
            return False

    except:
        return False


def check_hcl(data):

    if len(data) != 7 and data[0] != '#':
        return False

    nonltr = re.compile('[a-f0-9]').search

    res = True
    for ltr in data[-6:]:
        
        res = res and bool(nonltr(ltr))
        
    if res:       
        return True

    else:
        return False


def check_ecl(data):

    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if data in ecl_list:
        return True
    else:
        return False


def check_pid(data):

    if len(data) == 9:
        try:
            num = int(data)
            return True
        except:
            return False

    return False


def validate_passport(passport):

    if (check_byr(passport['byr'])):
        if ( check_hgt(passport['hgt'])):
            if (check_hcl(passport['hcl'])):
                if (check_ecl(passport['ecl'])):
                    if (check_pid(passport['pid'])):
                        if (check_eyr(passport['eyr'])):
                            if (check_iyr(passport['iyr'])):
                                return True
    return False



