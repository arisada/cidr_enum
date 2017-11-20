#!/usr/bin/env python3

"""
cidr_enum.py is a very simple tool to help enumerate IP ranges when being used with other tools
"""

import argparse
import netaddr

def enum_ranges(ranges, do_sort):
	cidrs=[]
	for r in ranges:
		try:
			cidrs.append(netaddr.IPNetwork(r))
		except Exception as e:
			print("Error:", e)
			return
	if(do_sort):
		cidrs = sorted(cidrs)
	#print(cidrs)
	for cidr in cidrs:
		for ip in cidr:
			print(ip)

def main():
	parser = argparse.ArgumentParser(description='Enumarate CIDR ranges')
	parser.add_argument('ranges', metavar='range', type=str, nargs='*',
                   help='List of CIDR ranges to enumerate')
	parser.add_argument('-f', '--files', metavar='file', type=str, nargs='*',
					help='List of files to retrieve CIDR ranges to enumerate')
	parser.add_argument('-s', '--sort', action='store_true', help='Sort CIDR ranges')
	args = parser.parse_args()
	if args.files:
		files = list(args.files)
	else:
		files = []
	ranges = list(args.ranges)
	if not (files or ranges):
		print ("Please give a list or ranges or input files")
		parser.print_help()
		return
	for f in files:
		with open(f, "r") as fd:
			for l in fd.readlines():
				ranges.append(l.strip())

	enum_ranges(ranges, do_sort=args.sort)

if __name__ == '__main__':
	main()
