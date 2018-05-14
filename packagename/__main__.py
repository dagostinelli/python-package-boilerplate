import sys

def main(args=None):
	"""The main routine."""
	if args is None:
		args = sys.argv[1:]

	print("This is the main routine.")
	print("It should do something interesting.")
	
	print( "This is the name of the script: ", sys.argv[0])
	print( "Number of arguments: ", len(sys.argv))
	print( "The arguments are: " , str(sys.argv))	

	# Do argument parsing here with argparse

if __name__ == "__main__":
	main()
