import arcpy
import pythonaddins

class Tool1(object):
    """Implementation for 1. Create-Random-Points-in-Selcted Polygon_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "Circle" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.

    def onRectangle(self, rectangle_geometry):
        if arcpy.Exists(r'in_memory\ran_points'):
            arcpy.Delete_management(r'in_memory\ran_points')
        arcpy.CreateRandomPoint_management(r'in_memory','ran_points','',rectangle_geometry,60)
        pythonaddins.MessageBox('60 Random Points are Created','Message : On Circle Event',0)
                        
