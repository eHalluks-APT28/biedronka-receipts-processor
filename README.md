# BIEDRONKA RECEIPTS PROCESSOR

### Short description: After cloning the project, <span style="color:pink"> remove the following block of code.

## <span style="color:lightgreen">ToDo

```python
################################################################
# Remove below block after cloned
################################################################

directories = [
    "input",
    "output/collection",
    "output/combined_png",
    "output/extracted_png",
    "output/json",
    "output/target",
    "output/txt",
    "receipts/done",
    "receipts/downloaded"
]

for directory in directories:
    gitkeep_path = os.path.join(directory, ".gitkeep")
    if os.path.isfile(gitkeep_path):
        os.remove(gitkeep_path)

################################################################
# end of block of code to remove
################################################################
```
### <span style="font-style: italic">*main.py
