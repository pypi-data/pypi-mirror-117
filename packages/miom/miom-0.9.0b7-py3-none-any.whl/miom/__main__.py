import argparse
import miom
import os
from miom.tools import consistent_subnetwork


def convert_list_gems(input_files, output=None, consistent=False, solver="glpk"):
    for i, input_file in enumerate(input_files):
        input_file = input_file.strip()
        # Check if input_file is a valid file and it exists
        if not (miom.mio._is_url(input_file) or (os.path.isfile(input_file) and os.path.getsize(input_file) > 0)):
            print(f"Skipping {input_file} (not a valid URL or file)")
            continue
        filename = os.path.basename(input_file)
        extension = os.path.splitext(filename)[1]
        output_file = filename.replace(extension, '.miom')
        print(f"Loading {input_file}...")
        try:
            m = miom.mio.load_gem(input_file)
            print(f"Loaded network with {m.num_reactions} reactions (in-memory size: {m.object_size:.2f} MB)")
            if consistent:
                print(f"Calculating consistent subnetwork...")
                m,_ = consistent_subnetwork(m, solver=solver)
                print(f"Consistent subnetwork contains {m.num_reactions}")
            # Concatenate folder and output file
            # print(os.path.abspath(output))
            if output is not None:
                if isinstance(output, list) and len(output) == len(input_files):
                    output_file = output[i]
                    # Get absolute path of the folder of the file
                    abspath = os.path.dirname(os.path.abspath(output_file))
                    if not os.path.isdir(abspath):
                        # Try to create a folder
                        try:
                            print(f"Creating directory {abspath}...")
                            os.makedirs(abspath)
                        except OSError as e:
                            print(f"Cannot create {abspath} folder: {e}")
                elif os.path.isdir(output) or os.path.isdir(os.path.abspath(output)):
                    output_file = os.path.join(output, output_file)
                else:
                    raise ValueError("The provided output is not a folder or a list of destinations for each file")
            print(f"Exporting to {output_file}...")
            miom.mio.export_gem(m, output_file)
            # Calculate the MBs of the output_file and print it
            output_file_size = os.path.getsize(output_file)
            output_file_size = output_file_size / (1024 * 1024)
            print(f"File size: {output_file_size:.2f} MB")
            print("Done.")
        except Exception as e:
            print(f"Error while converting {input_file}: {e}")
            raise e
        

def convert_gem(args):
    print(f"MIOM v{miom.__version__}")
    input = args.input
    output = args.output
    if isinstance(input, str):
        if os.path.isfile(input) and input.endswith('.txt'):
            # Open file and get all the lines into a list
            print(f"Reading list of files from {input}...")
            with open(input, "r") as f:
                in_files, out_files = [], []
                input = f.readlines()
                for line in input:
                    if ";" in line:
                        in_path, out_path = line.split(";")
                        in_files.append(in_path.strip())
                        out_files.append(out_path.strip())
                input = in_files
                output = out_files
        elif os.path.isdir(os.path.abspath(input)):
            #in_folder = os.path.abspath(input)
            input = [os.path.join(input, f) for f in os.listdir(input)]
        else:
            input = [input]
            output = [output]
    convert_list_gems(input, output, consistent=args.consistent, solver=args.solver)


def get_args():
    parser = argparse.ArgumentParser(description=f"MIOM: Mixed Integer Optimization for Metabolism")
    parser.add_argument(
        "--version",
        action="version", 
        version=f"MIOM v{miom.__version__}"
    )
    subparsers = parser.add_subparsers(help="sub-command help")
    convert = subparsers.add_parser("convert", help="Convert a model to miom format")
    convert.add_argument(
        "--consistent",
        action="store_true",
        default=False
    )
    convert.add_argument(
        '--solver', 
        default="glpk", 
        type=str
    )
    convert.add_argument(
        "input",
        help="Input model file (if cobra is installed, any format supported by cobra is allowed)"
    )
    convert.add_argument(
        "output",
        help="Output GEM file in MIOM format"
    )
    convert.set_defaults(func=convert_gem)
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    # Check if 'func' is an attribute of args
    if hasattr(args, "func") and args.func:
        args.func(args)