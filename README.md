# Convert_pdf2image

The code presented here convert multiple PDF files in images and is based on the Python module [pdf2image](https://pypi.org/project/pdf2image/).
It includes a mechanism to deal with PDF files that ask for pasword so all other PDF files are converted and the one that requires password are listed in a .txt file.

The code is presented in details and with examples in notebook [convert_pdf_to_image.ipynb](https://github.com/dpbac/pdf2image/blob/master/convert_pdf_to_image.ipynb).

The same code is presented in a script, [pdfs_to_image.py](https://github.com/dpbac/pdf2image/blob/master/pdfs_to_image.py).

To use the script use the command line in the folder where is and type:

python pdfs_to_image.py [-h] -p PDFS_FOLDER -i IMAGE_PATH -d DPI

**Example:**

`python pdfs_to_image.py -p "./data/pdf/" -i "./data/img/" -d 300 -f "pdfs_require_password"`

PDF files used here were downloaded from:

https://www.bu.edu/geneva/files/2010/08/Easy_recipes.pdf

https://www.formerchef.com/wp-content/uploads/2010/07/Ratatouille.pdf

https://www.cdc.gov/coronavirus/2019-ncov/downloads/2019-ncov-factsheet.pdf

## Install requirements
* Install requirements using `pip install -r requirements.txt`.
  * Make sure you use Python 3.
  * You may want to use a virtual environment for this.



