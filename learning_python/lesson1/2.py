#!/usr/bin/env python
"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it
up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

$ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.

"""

ips = [
	"254.253.252.251",
	"10.11.12.13",
	"1.2.3.4",
	# input("Please enter an IP address (eg. 1.2.3.4):"),
]

for ip in ips:
	print("\n" + "#" * 64 + "\n")
	print(f"IP ADDRESS: {ip}")
	octets = ip.split('.')

	print("\nFIRST PRINT")
	print(
	f"""
    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      {octets[0]}             {octets[1]}             {octets[2]}            {octets[3]}
   {bin(int(octets[0]))}      {bin(int(octets[0]))}       {bin(int(octets[0]))}      {bin(int(octets[0]))}
     {hex(int(octets[0]))}           {hex(int(octets[1]))}           {hex(int(octets[2]))}           {hex(int(octets[3]))}
------------------------------------------------------------
	"""
	)

	print("\nSECOND PRINT")
	heads = [f"Octet{o}" for o in range(1, 5)]
	bins = [bin(int(o)) for o in octets]
	hexs = [hex(int(o)) for o in octets]
	print(heads)
	print(bins)
	print(hexs)


	print("\nTHIRD PRINT")
	from random import randint as random
	outputs = [
		["Headers"],
		heads,
		["Binary"],
		bins,
		["Hex"],
		hexs,
		["Random"],
		[str(random(0,1)) for x in range(0,4)]
	]
	for output in outputs:
		print(output)
