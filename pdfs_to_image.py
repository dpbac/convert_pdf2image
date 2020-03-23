# USAGE

# python pdfs_to_image.py -p "./data/pdf/" -i "./data/img/" -d 300 -f "pdfs_require_password"


from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError
import glob
import argparse
import time

TodaysDate = time.strftime("%Y-%m-%d")


def convert_pdf2image(pdf_path, image_path, dpi):
    """ 
    Converts a multi-page pdf file to image file given the path of the pdf file (pdf_path) and save images in image_path.
    
    Input:
        pdf_path: path to PDF file to be converted in image
        image_path: path to folder where resulting image will be saved
        dpi: chosen resolution
    """
    # convert pdf to image
    images = convert_from_path(pdf_path, dpi, jpegopt = 'optimize', fmt = 'jpge')
    # Extract name of pdf file to name image similarly
    image_name = pdf_path.split('\\')[-1].split('.')[-2]
    
    # save all images generated from pdf file
    for i, image in enumerate(images):
        fname = image_path + image_name+"_image_" + str(i) + ".jpeg"
        image.save(fname, "jpeg")
        
        
def convert_multiple_pdf(pdfs_folder, image_path, dpi, filename):
    """ 
    Convert multiple PDF files in a folder to images.
    
    Input:
        pdfs_folder: folder containing PDF files
        image_path: image_path: path to folder where resulting image will be saved
        dpi: chosen resolution
        filename: name of the .txt file that keep name of PDF files that required passwords and could not be converted
        
    """

    # starting counter of files converted
    count = 0
    #list to keep name of pdf files that require password
    password_pdf = []

    for pdf_path in glob.glob(pdfs_folder+'*.pdf'):
        try:
            convert_pdf2image(pdf_path, image_path, dpi)
            count += 1
        except PDFPageCountError:
            password_pdf.append(pdf_path.split('\\')[-1])
            pass    
    
        with open(pdfs_folder+filename+"_"+TodaysDate+".txt", "w") as output:
            output.write(str('\n'.join(password_pdf)))
        
    print(str(len(glob.glob(pdfs_folder+'*.pdf'))-count) + " PDF files with password.")
    print(str(count) + " files converted.")
        


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pdfs_folder", required=True, help="Folder where PDF files are located.")
    parser.add_argument("-i", "--image_path", required=True,help="Folder where to save image file obtained from pdf file.")
    parser.add_argument("-d", "--dpi",required=True,help="Resolution.")
    parser.add_argument("-f", "--filename",required=True,help="Name of the .txt file that keep name of PDF files that required passwords and could not be converted")
    
    args = parser.parse_args()
        
    pdfs_folder = args.pdfs_folder
    image_path = args.image_path
    dpi = args.dpi
    filename = args.filename
    
    convert_multiple_pdf(pdfs_folder, image_path, dpi, filename)
    
    

        
if __name__=='__main__':
    main()
        
        
        
        
        
        
