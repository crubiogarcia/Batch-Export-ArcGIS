# -*- coding: utf-8 -*-

import arcpy
import os

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Batch Export Toolbox"
        self.alias = "batch_export_toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [ExportPAGXTool,ExportPDFTool, ExportMPKXTool]


class ExportPAGXTool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Export as PAGX"
        self.description = "Batch export all Layouts in project as .PAGX"

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = []
        
        # Define the folder location parameter
        folder_param = arcpy.Parameter(
            displayName="Folder location for exported files",
            name="folder_location",
            datatype="DEFolder",  # Specify that the input is a folder
            parameterType="Required",  # Set to Required
            direction="Input"  # The parameter is an Input
        )

        # Add the parameter to the list
        params.append(folder_param)
            
        
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        #Get input
        folderpath = parameters[0].valueAsText
        #Get project layouts
        project = arcpy.mp.ArcGISProject('CURRENT')
        layouts = project.listLayouts()
        
        #LAYOUT EXPORT
        for lyt in layouts:
            try:
                # Export each layout to .PAGX format
                lyt.exportToPAGX(os.path.join(folderpath, f"{lyt.name}.pagx"))
                messages.addMessage(f"Layout exported '{lyt.name}'")
                
            except Exception as e:
                # Add an error message if the export fails
                messages.addErrorMessage(f"Failed to export layout '{lyt.name}': {e}")

        # Add a success message after all layouts are processed
        messages.addMessage("Export completed successfully.")
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


class ExportPDFTool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Export as PDF"
        self.description = "Batch export all Layouts in project as PDF"

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = []
        
        # Define the folder location parameter
        folder_param = arcpy.Parameter(
            displayName="Folder location for exported files",
            name="folder_location",
            datatype="DEFolder",  # Specify that the input is a folder
            parameterType="Required",  # Set to Required
            direction="Input"  # The parameter is an Input
        )

        # Add the parameter to the list
        params.append(folder_param)
            
        
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        #Get input
        folderpath = parameters[0].valueAsText
        #Get project layouts
        project = arcpy.mp.ArcGISProject('CURRENT')
        layouts = project.listLayouts()
        
        #LAYOUT EXPORT
        for lyt in layouts:
            try:
                # Export each layout to .PAGX format
                output_path = os.path.join(folderpath, f"{lyt.name}.pdf")
                # Export the layout to PDF with rasterization
                lyt.exportToPDF(output_path,
                    resolution=250,  # Set resolution
                    image_quality='NORMAL',  # Set image quality
                    image_compression='ADAPTIVE',  # Set compression method
                    embed_fonts=True,  # Embed fonts for better quality
                    layers_attributes='NONE',  # Avoid including layers and attributes
                    georef_info=True,  # Include georeference information
                    jpeg_compression_quality=70)  # Set JPEG compression quality
                
                messages.addMessage(f"Layout exported '{lyt.name}'")
                
            except Exception as e:
                # Add an error message if the export fails
                messages.addErrorMessage(f"Failed to export layout '{lyt.name}': {e}")

        # Add a success message after all layouts are processed
        messages.addMessage("Export completed successfully.")
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


class ExportMPKXTool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Export as MPKX"
        self.description = "Batch export all maps in project as MPKX"

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = []
        
        # Define the folder location parameter
        folder_param = arcpy.Parameter(
            displayName="Folder location for exported files",
            name="folder_location",
            datatype="DEFolder",  # Specify that the input is a folder
            parameterType="Required",  # Set to Required
            direction="Input"  # The parameter is an Input
        )

        # Add the parameter to the list
        params.append(folder_param)
            
        
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        #Get input
        fpath = parameters[0].valueAsText
        #Get project layouts
        project = arcpy.mp.ArcGISProject('CURRENT')
        maps = project.listMaps()
        
        #LAYOUT EXPORT
        for map_obj in maps:
            try:
                # Export each layout to .PAGX format
                output_mpkx = os.path.join(fpath, f"{map_obj.name}.mpkx")
                
                #Export the map as map package (.mpkx)
                arcpy.PackageMap_management(map_obj, output_mpkx, "PRESERVE", "CONVERT_ARCSDE", "#", "ALL")
                
                messages.addMessage(f"Map exported '{map_obj.name}'")
                
            except Exception as e:
                # Add an error message if the export fails
                messages.addErrorMessage(f"Failed to export map '{map_obj.name}': {e}")

        # Add a success message after all layouts are processed
        messages.addMessage("Export completed successfully.")
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return