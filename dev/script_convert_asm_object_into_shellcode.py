import argparse
import subprocess
import platform
import pathlib

ACCEPTED_SYSTEM = ["Linux"]
ACCEPTED_ARCHITECTURE = ["64bit"]
ACCEPTED_FILE_EXTENSION = ["asm", "s"]


def main(argv=None):
    if platform.system() not in "".join(ACCEPTED_SYSTEM) or platform.architecture()[
        0
    ] not in "".join(ACCEPTED_ARCHITECTURE):
        print(
            "This script need to be run with a "
            + "/".join(ACCEPTED_SYSTEM)
            + " in a "
            + "/".join(ACCEPTED_ARCHITECTURE)
            + " architecture to work properly."
        )
        exit()

    parser = argparse.ArgumentParser()
    parser.add_argument("asm_file_name")
    args = parser.parse_args(argv)
    file_name = args.asm_file_name
    file_extension = pathlib.Path(file_name).suffix
    file_base_name = file_name[: -len(file_extension)]
    # Removing the dot for file_extension.
    file_extension = file_extension[1:]
    if file_extension not in ACCEPTED_FILE_EXTENSION:
        print("Only " + "/".join(ACCEPTED_FILE_EXTENSION) + " files extensions are accepted.")
        exit()
    output = subprocess.getoutput("nasm -f elf64 " + file_name)
    if len(output) > 0:
        print("An error occured with nasm: ", output)
        exit()
    output = subprocess.getoutput("objdump -d " + file_base_name + ".o")
    print(output)


if __name__ == "__main__":
    main()
