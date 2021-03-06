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

def main():
	while True:
		'''read the command line from stdin and split it.
		[0] is the command;
		[2] is the name of the file;
		[4] is the path to the locker.'''
		print('\n')
		print ('Format of Input: command -file "filename" -path "path_to_locker"')
		print ('(no space in "filename" and "path_to_locker")')
		print ('Input "exit" to stop the program')
		print('')
		command = sys.stdin.readline()
		command = cli(command)
		print('')

		'''Judge if the command is valid.'''
		if command == ['exit']:
			return None

		elif len(command) != 5:
			print('Incorrect input format!')
			continue

		elif command[0] == 'storea':
			try:
				insert.insertASCII(command[2],command[4])
				print(command[2] + ' is stored in ' + command[4] + ' successfully.')
			except:
				print('Incorrect file or path.')

		elif command[0] == 'storeb':
			try:
				insert.insertbinary(command[2],command[4])
				print(command[2] + ' is stored in ' + command[4] + ' successfully.')
			except:
				print('Incorrect file or path.')

		elif command[0] == 'delete':
			try:
				delete.delete(command[2],command[4])
				print(command[2] + ' is deleted successfully.')
			except:
				print('Incorrect file or path.')

		elif command[0] == 'retrieve':
			try:
				fileretrieve.retrieve(command[2],command[4])
				print(command[2] + ' is retrieved successfully.')
			except:
				print('Incorrect file or path.')

		else:
			print('Illegal command!(legal commands are: store; delete; retrieve.)')
	return None


if __name__ == '__main__':
	main()
