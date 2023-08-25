import streamlit as st
import geocoder
import folium

def main():
    st.title("Location Mapper")

    ip_address = st.text_input("Enter IP Address:")
    if ip_address:
        g = geocoder.ip(ip_address)
        my_address = g.latlng

        st.write("Latitude and Longitude:", my_address)

        my_map = folium.Map(location=my_address, zoom_start=12)
        folium.CircleMarker(location=my_address, radius=50, popup="Location").add_to(my_map)
        folium.Marker(my_address, popup="Marker").add_to(my_map)

        folium_static(my_map)

if __name__ == "__main__":
    main()



# import geocoder 
# import folium
# g=geocoder.ip("49.36.193.35")
# myAddress=g.latlng
# print(myAddress)
# my_map=folium.Map(location=myAddress , zoom_start=12)
# folium.CircleMarker(location=myAddress , radius=50 , popup="jammu").add_to(my_map)
# folium.Marker(myAddress , popup="Jugal sharma").add_to(my_map)
# my_map.save("my_map.html")


# import requests 

# import pprint


# ip="2405:201:5505:e12c:e441:11d5:ec05:bc19"
# url=f"https://ipapi.co/{ip}/json/"

# r=requests.get(url)

# pprint.pprint(r.json())