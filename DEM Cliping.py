import arcpy
from arcpy import env
env.workspace = r'F:\Sanskruti Mam\All Village Shapefiles\shp'
fclist = arcpy.ListFeatureClasses()
  
for fc in fclist:
    outName = str(fc)+'dem'
    clip = arcpy.sa.ExtractByMask("cdne43u.tif",fc)
    outs = clip.save(r'F:\Sanskruti Mam\All Village Shapefiles\allDEMs\{0}'.format(outName)+'.img')
    

