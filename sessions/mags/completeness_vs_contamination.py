#!/usr/bin/python3
import matplotlib.pyplot as plt
import argparse
import sys

# Argument parser setup
parser = argparse.ArgumentParser(description="Plot completeness vs contamination")
parser.add_argument("-i", "--input", dest="input", required=True, help="Input table: genome,completeness,contamination")
parser.add_argument("-o", "--output", dest="output", help="Output plot file (optional)")
parser.add_argument("--scatter-dots-size", dest="scatter_dots_size", help="argument for dots size in plt.scatter(s= )",
                    default=5, type=float)
parser.add_argument("--scatter-dpi", dest="scatter_dpi", help="argument for dots size in plt.savefig(dpi= )",
                    default=300, type=int)

args = parser.parse_args()

comp, cont = [], []
try:
    with open(args.input, 'r') as file_in:
        for line in file_in:
            if 'completeness' in line:
                continue
            try:
                line = line.strip().split(',')
                comp.append(float(line[1]))
                cont.append(float(line[2]))
            except ValueError:
                print(f"Error parsing line: {line}", file=sys.stderr)
except FileNotFoundError:
    print(f"File not found: {args.input}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
    sys.exit(1)

# Plotting
fig = plt.figure(figsize=(6, 6))
plt.scatter(comp, cont, s=args.scatter_dots_size)
plt.xlabel("Completeness")
plt.ylabel("Contamination")
plt.title("Completeness vs Contamination")

# Save the plot if an output file is provided, otherwise show the plot
if args.output:
    plt.savefig(args.output, dpi=args.scatter_dpi)
    print(f"Plot saved to {args.output}")
else:
    plt.show()
