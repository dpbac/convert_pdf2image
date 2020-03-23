# pdf2image

The code presented here convert multiple PDF files in images and is based on the Python module [pdf2image](https://pypi.org/project/pdf2image/).
It includes a mechanism to deal with PDF files that ask for pasword so all other PDF files are converted and the one that requires password are listed in a .txt file.

The code is presented in details and with examples in notebook [convert_pdf_to_image.ipynb](https://github.com/dpbac/pdf2image/blob/master/convert_pdf_to_image.ipynb).

The same code is presented in a script, [pdfs_to_image.py](https://github.com/dpbac/pdf2image/blob/master/pdfs_to_image.py).

To use the script use the command line in the folder where is and type:

python pdfs_to_image.py -p _"path to folder where PDF files are"_ -i _"path to folder where to save generated images"_ -d resolution in dpi -f _"name of the file that will keep the name of PDF files that were not converted because required password"_ 

Example:

`python pdfs_to_image.py -p "./data/pdf/" -i "./data/img/" -d 300 -f "pdfs_require_password"`
