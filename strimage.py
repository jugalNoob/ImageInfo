import streamlit as st
import PIL.Image
import PIL.ExifTags

def main():
    st.title("EXIF Metadata Viewer")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        exif = image._getexif()

        if exif is not None:
            exif_data = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in exif.items()
                if k in PIL.ExifTags.TAGS
            }

            date_time_original = exif_data.get('DateTimeOriginal')
            date_time_digitized = exif_data.get('DateTimeDigitized')
            model = exif_data.get('Model')
            maker = exif_data.get("Make")
            software = exif_data.get("Software")
            gps = exif_data.get("GPSInfo")

            st.write("Original Date and Time:-:", date_time_original)
            st.write("Digitized Date and Time:-:", date_time_digitized)
            st.write("Model:-:", model)
            st.write("Maker:-:", maker)
            st.write("Software:-:", software)
            st.write("GPSInfo:-:", gps)

        else:
            st.warning("No EXIF metadata available for this image.")

if __name__ == "__main__":
    main()
