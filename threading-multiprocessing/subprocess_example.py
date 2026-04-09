import subprocess

def main() -> None:

    # Passing the entire shell command as a single string:
    # This requires the shell=True flag
    output = subprocess.run("ls -la", shell=True)
    print(output.stdout)
    # DRAWBACK: only use this if you are creating the shell command yourself,
    # and not relying on user input. This can result in injection attacks.
    # Currently stdout is None.
    # In order to capture the subprocess stdout and stderr into the 'output' variable
    # need to use the pamameter capture_output=True

    # The safer way to use subprocress is to pass in a list of strings
    # which get compiled into a shell command.

    output2 = subprocess.run(['ls', '-la'], capture_output=True)
    print(output2.stdout.decode())
    # capture_output captures the subprocess' output in bytes, which needs to be decoded
    # if the output is a string.
    # If the expected output is a string, then the text=True parameter can be used.
    # Then decoding is not necessary.

    output3 = subprocess.run(['ls', 'l'], capture_output=True, text=True)
    print(output3.stdout)

    # Subprocess outputs can also be captured directly to files, which can be useful for logging.
    with open("stdout-to-file.txt", 'w') as f:
        subprocess.run(['echo', 'hello world'], stdout=f, text=True)


    # Passing in the stdout from one subprocess to another, like using a pipe in the shell:
    # Need to use the input flag to pass the stdout of one process as the input of another

    p1 = subprocess.run(['cat', 'stdout-to-file.txt'], capture_output=True, text=True)
    p2 = subprocess.run(['grep', '-n', 'world'], capture_output=True, text=True, input=p1.stdout)
    print(p2.stdout)

    return

if __name__ == "__main__":
    main()