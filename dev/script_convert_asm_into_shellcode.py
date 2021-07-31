import argparse
import subprocess


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("asm_file_name")
    args = parser.parse_args(argv)
    file_name = args.asm_file_name
    output = subprocess.getoutput("nasm -f elf64 " + file_name)
    # output = subprocess.getoutput("objdump -d " + file_name)
    print(output)


if __name__ == "__main__":
    main()
