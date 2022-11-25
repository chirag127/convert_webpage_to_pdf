import streamlit as st
import pdfkit


import subprocess

try:
    # sudo apt-get update
    # sudo apt-get install wkhtmltopdf
    subprocess.call(['wkhtmltopdf', '--version'])
    wkhtmltopdf_installed = True
    print("wkhtmltopdf installed")
except:
    wkhtmltopdf_installed = False
    print("wkhtmltopdf not installed")

    # install wkhtmltopdf
    subprocess.call(['sudo', 'apt-get', 'update'])
    subprocess.call(['sudo', 'apt-get', 'install', 'wkhtmltopdf'])



# this is an python app to convert the webpages to pdf

# this is the main function
def main():
    st.title("Webpage to PDF Converter")
    st.text("This app converts the webpage to pdf")
    st.text("Enter the url of the webpage")
    url = st.text_input("Enter the url")
    st.text("Enter the name of the pdf file")
    name = st.text_input("Enter the name")
    if st.button("Convert"):
        st.text("Converting...")
        pdfkit.from_url(url, name+".pdf")
        st.success("Done")

        with open(name+".pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="download", data=PDFbyte, file_name=name+".pdf", mime="application/pdf")

if __name__ == "__main__":
    main()
