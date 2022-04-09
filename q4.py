# Q: 4 - Convert list to list of dictionaries from those given lists.
# Sample: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [
#     {'color_name': 'Black', 'color_code': '#000000'},
#     {'color_name': 'Red', 'color_code': '#FF0000'},
#     {'color_name': 'Maroon', 'color_code': '#800000'},
#     {'color_name': 'Yellow', 'color_code': '#FFFF00'}
#     ] 


color_name = ["Black", "Red", "Maroon", "Yellow"]

color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
vs = []
for i, j in zip(color_name, color_code):
    v = {'color_name': i,'color_code': j}
    vs.append(v)
print(vs)