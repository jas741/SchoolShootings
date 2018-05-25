# SchoolShootings
Analysis of US School Shootings since Sandy Hook.

Data pulled from "school shooting, elementary/secondary" query at http://www.gunviolencearchive.org/query

This data includes placename but not latitude / longitude.

`GetCoordinates.py` gets latitude / longitude from placename data.

`basicfoliummap.py` uses `folium` to build a rudimentary map. clicking on an incident marker tells you how many victims (injured or killed).  You can view it here: https://jas741.github.io/SchoolShootings/

