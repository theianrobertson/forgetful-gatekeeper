from random import SystemRandom

def get_pass(seeder='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()', 
    length=16):
	'''Gets a password given a seeder and length.'''
	return ''.join([SystemRandom().choice(seeder) for i in range(length)])

if __name__ == '__main__':
	for i in range(5):
	    print(get_pass())