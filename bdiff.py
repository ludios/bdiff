import sys

def main():
	fname1, fname2 = sys.argv[1], sys.argv[2]
	f1 = open(fname1, "rb")
	f2 = open(fname2, "rb")
	while True:
		a = f1.read(32)
		b = f2.read(32)
		if a != b:
			print "MISMATCH before byte %d:" % (f1.tell(),)
			print a.encode("hex")
			print b.encode("hex")

		if not a or not b:
			break


main()
