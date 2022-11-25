import streamlit as st
import weasyprint


import subprocess

try:
    # sudo apt-get update
    # sudo apt-get install wkhtmltopdf
    subprocess.call(["wkhtmltopdf", "--version"])
    wkhtmltopdf_installed = True
    print("wkhtmltopdf installed")
except:
    wkhtmltopdf_installed = False
    print("wkhtmltopdf not installed")


if not wkhtmltopdf_installed:

    # install wkhtmltopdf
    subprocess.call([ "apt-get", "-y", "update"])
    subprocess.call([ "apt-get", "install", "-y", "wkhtmltopdf"])


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
        PDFbyte = weasyprint.HTML(url).write_pdf()
        st.success("Done")

        st.download_button(
            label="download",
            data=PDFbyte,
            file_name=name + ".pdf",
            mime="application/pdf",
        )


if __name__ == "__main__":
    main()
