import folium
import pandas

map = folium.Map(location=[43.78,-120.56],zoom_start=6,tiles = "Stamen Terrain")
fgv=folium.FeatureGroup(name="Volcanoes")
data=pandas.read_csv("Volcanoes.txt")

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

for lt,ln,el in zip(lat,lon,elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    if el<1000:
        fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=folium.Popup(iframe),fill_color="green",color="grey",fill_opacity=0.7))
    elif el>=1000 and el<3000:
        fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=folium.Popup(iframe),fill_color="orange",color="grey",fill_opacity=0.7))
    else:
        fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=folium.Popup(iframe),fill_color="red",color="grey",fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding="utf-8-sig").read(),
style_function=lambda x:{'fillColor':'green' if x["properties"]["POP2005"] < 10000000
else 'orange' if 10000000<= x["properties"]["POP2005"] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map2.html")
