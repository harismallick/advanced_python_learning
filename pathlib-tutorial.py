from pathlib import Path

my_dir = Path("50_advanced_concepts")
my_file = Path("metaclasses.py")

new_file1 = my_dir / "new_file.txt" # Special pathlib syntax
new_file2 = my_dir.joinpath("new_file.txt") # Old school method
# These files don't have to exist to create a dynamic path like this in the source code

print(my_dir)
print(my_file)
print(new_file1)
print(new_file2)

## How to check if a path exists:

print(my_dir.exists())
print(new_file1.exists())

# Best way to get absolute path of a file or directory:

print(my_file.resolve())

# Go to home directory and start navigation from there:

documents = Path.home() / "Documents"

# loop through all contents of a Path object:
# for p in documents.iterdir():
#     print(p)

# use glob to refine the search:

for p in documents.glob("*sol*"): # Finds all folders and files with 'sol' in it
    print(p)

# use rglob to recursively check the subdirectories as well.

# If the Path object is a file, it can be opened:

# with my_file.open() as f:
#     print(f.read())

# Making directories

# p = Path("new_dir")
# p.mkdir()   # makes the new dir in root

# p = Path("parent/child_dir")
# p.mkdir(parents=True)   # This will make the parent and the child_dir
# # This ONLY works if the parent directory doesn't yet exist.

# p = Path("new_file.txt")
# p.touch() # Creates an empty new_file.txt in root dir

