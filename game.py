import folium
import img

m = folium.Map(location=[45.5236, -122.6750])
loc = img.find_img()
marker = (loc["lat"], loc["lon"])

folium.Marker(marker, popup="WP").add_to(m)

menu_html = f"""
<div style="display: flex; height: 100vh;">
    <div style="flex-basis: 50%; height: 100%;">
        <iframe src='{loc["url"]}' width='100%' height='100%'></iframe>
    </div>
    <div style="flex-basis: 50%; height: 100%;">
        {m._repr_html_()}
    </div>
</div>
"""
with open("index.html", "w") as f:
    f.write(menu_html)
