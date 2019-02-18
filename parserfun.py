import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--filename", help = "This is a file to open cuz")
parser.add_argument("--port", help = "It's a port dude")
parser.add_argument("num1", type=int)
parser.add_argument("num2", type=int)
args = parser.parse_args()
sum = args.num1 + args.num2

print(sum)
print(args.port)
