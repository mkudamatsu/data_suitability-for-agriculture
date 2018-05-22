print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)
print work_dir

if not os.path.isdir("../orig/"): # Create the output directory if it doesn't exist
    os.makedirs("../orig/")

if not os.path.isdir("../temp/"): # Create the temporary file directory if it doesn't exist
    os.makedirs("../temp/")

if not os.path.isdir("../docs/"): # Create the temporary file directory if it doesn't exist
    os.makedirs("../docs/")

### Define the main function ###
def main():
    try:
        # Setting input and output
        url = "https://nelson.wisc.edu/sage/data-and-models/atlas/data/suit.zip"
        downloaded_zip = "../temp/" + url[-8:]
        # Process
        # download_data(url, downloaded_zip)

        print "Extract all files" # Extracting only necessary files (the .extract() function) does not work. So we extract all and then delete those unnecessary.
        # Setting input and output
        input_zip = downloaded_zip
        outdir = "../orig/"
        # uncompress_zip(input_zip, outdir)

        # Move the Readme file to the /docs folder
        readme = "readme.pdf"
        if not os.path.isfile("../docs/"+readme): # Only for the first loop
            os.rename(outdir+readme, "../docs/"+readme)

        print "Deleting the zip file and the temporary file directory"
        for file in os.listdir("../temp/"):
            print file
            os.remove("../temp/"+file)        # os.rm(dowloaded_zip)
        os.rmdir("../temp/")

        print "All done."

    # Return any other type of error
    except:
        print "There is an error."

### Define the subfunctions ###
def download_data(url, output):
    print "...downloading and saving the file"
    import urllib
    urllib.urlretrieve(url, output)

def uncompress_zip(in_zip, outdir):
    print "...launching zipfile module" # See http://stackoverflow.com/questions/9431918/extracting-zip-file-contents-to-specific-directory-in-python-2-7
    import zipfile
    print "...reading the zip file"
    zip_ref = zipfile.ZipFile(in_zip, 'r')
    print "...extracting the zip file"
    zip_ref.extractall(outdir)
    print "...closing the zip file"
    zip_ref.close()
    print "...deleting the zip file"
    os.remove(in_zip)

### Execute the main function ###
if __name__ == "__main__":
    main()
