import folium

# Variables
inty = 5
listy = [6, 7]
stringy = "Hi"

# Create a folium map
azores = folium.Map(location=(38, -27), zoom_start=6)

# Type checking
print(type(inty), type(listy), type(stringy), type(azores))
print(type(5), type([6, 5]), type("Hi"))
print(type(folium.Map(location=(38, -27), zoom_start=6)))

# Built-in constructors
print(int(5))
print(list([6, 7]))
print(str("Hi"))

# Simple operations
print(4 + 5)
print("hi".capitalize())

# Save map to HTML
map_obj = folium.Map(location=(38, -27), zoom_start=6)
map_obj.save("output.html")
print("Map has been saved to output.html")

