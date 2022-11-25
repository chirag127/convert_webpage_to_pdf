import streamlit as st
import weasyprint


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
