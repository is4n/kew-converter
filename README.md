Application for converting "KEW" Flash interactive lessons to a format more suitable for modern PCs. 

Depends: 
- Python3 with PIP (to install PDFminer.six)
- SWFTools (downloaded and compiled by setup.sh)

setup: 
- clone repo into a folder of your choice
- `cd` into the folder
- run `./setup.sh` (if it doesn't run: `chmod +x setup.sh`) NOTE: This may take a minute or three.

Usage:
`kew_converter <KEW_url> <output>`
- <output> should be in the form of `valid_path/output_folder`, `output_folder` will be created automatically.
