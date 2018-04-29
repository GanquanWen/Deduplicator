## Copyright 2018 Ganquan Wen wengq@bu.edu


import sys
import delete
import insert
import fileretrieve

def cli(cmd):
	'''The format of input should be store -file [file] -locker [locker_location]
	No space in the [file] and [locker_location] '''
	command = cmd.split()
	return command

	
def store(file, path):
	return None


def main():
	while True:
		'''read the command line from stdin and split it.
		[0] is the command;
		[2] is the name of the file;
		[4] is the path to the locker.'''
		print ('Format of Input: command -file "filename" -path "path_to_locker"')
		print ('(no space in "filename" and "path_to_locker")')
		command = sys.stdin.readline()
		command = cli(command)
		print (command)

		'''Judge if the command is valid.'''
		if command == ['exit']:
			return None
		elif len(command) != 5:
			print('Incorrect input format!')
			continue
		elif command[0] == 'store':
			store(command[2],command[4])
		elif command[0] == 'delete':
			delete.delete(command[2],command[4])
		elif command[0] == 'retrieve':
			fileretrieve.retrieve(command[2],command[4])
		elif command[0] == 'insert':
			pass
		else:
			print('Illegal command!(legal commands are: store; delete; retrieve.)')
	return None


if __name__ == '__main__':
	main()
