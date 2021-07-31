import argparse
import subprocess
import platform
import pathlib
import re

ACCEPTED_SYSTEM = ["Linux"]
ACCEPTED_ARCHITECTURE = ["64bit"]
ACCEPTED_FILE_EXTENSION = ["asm", "s"]


def error(error_message: str = None):
    print(error_message)
    exit()


def main(argv=None):
    if platform.system() not in "".join(ACCEPTED_SYSTEM) or platform.architecture()[
        0
    ] not in "".join(ACCEPTED_ARCHITECTURE):
        error(
            error_message="This script need to be run with a "
            + "/".join(ACCEPTED_SYSTEM)
            + " in a "
            + "/".join(ACCEPTED_ARCHITECTURE)
            + " architecture to work properly."
        )

    parser = argparse.ArgumentParser()
    parser.add_argument("asm_file_name")
    args = parser.parse_args(argv)
    file_name = args.asm_file_name
    file_extension = pathlib.Path(file_name).suffix
    file_base_name = file_name[: -len(file_extension)]
    # Removing the dot for file_extension.
    file_extension = file_extension[1:]
    if file_extension not in ACCEPTED_FILE_EXTENSION:
        error(
            error_message="Only "
            + "/".join(ACCEPTED_FILE_EXTENSION)
            + " files extensions are accepted."
        )
    output = subprocess.getoutput("nasm -f elf64 " + file_name)
    if len(output) > 0:
        error(error_message="An error occured with nasm: " + output)
    output = subprocess.getoutput("objdump -d " + file_base_name + ".o")
    print(output)
    output = output.split("\n")
    shell_code = []
    pattern_match_code_line = r"[\da-f]+:"
    pattern_hexa_code = r"^[a-f\d]+"
    for line in output:
        if re.search(pattern_match_code_line, line):
            # Remove left part before ':' char
            line = line.split(":")[1]
            line = line.replace(" ", "")
            line = line.replace("\t", "")
            match = re.match(pattern_hexa_code, line)
            if match is None:
                error(error_message="Error during line matching.")
            line = match.group(0)
            shell_code.append(line)
    print("\n".join(shell_code))


if __name__ == "__main__":
    main()
