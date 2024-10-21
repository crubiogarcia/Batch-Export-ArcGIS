# Batch Export ArcGIS Python Toolbox

This toolbox contains three custom ArcGIS tools for batch exporting layouts and maps from an ArcGIS project. The tools allow you to export layouts as `.PAGX` or `.PDF` files, and maps as `.MPKX` packages. These tools are designed to simplify the process of exporting multiple layouts and maps from an ArcGIS project in one step.

## Tools

### 1. Export as PAGX Tool
This tool batch exports all layouts in the current ArcGIS project as `.PAGX` files, which can be used to share or reuse layout configurations.

#### Parameters
- **Folder location for exported files** (Required): Specifies the folder where the exported `.PAGX` files will be saved.

### 2. Export as PDF Tool
This tool batch exports all layouts in the current ArcGIS project as `.PDF` files. You can customize the export settings like resolution, image quality, and compression.

#### Parameters
- **Folder location for exported files** (Required): Specifies the folder where the exported `.PDF` files will be saved.

### 3. Export as MPKX Tool
This tool batch exports all maps in the current ArcGIS project as `.MPKX` (Map Package) files, allowing you to package maps for sharing or reuse.

#### Parameters
- **Folder location for exported files** (Required): Specifies the folder where the exported `.MPKX` files will be saved.

## Installation

1. Clone or download this repository.
2. Place the `.pyt` file into your ArcGIS project's `Toolboxes` folder.

## Usage

1. Open ArcGIS Pro and load your project.
2. Navigate to the **Catalog** pane and locate the toolbox.
3. Double-click the desired tool to open its interface.
4. Specify the folder location for the exported files.
5. Click **Run** to execute the tool.

## Requirements

- ArcGIS Pro


## License

This project is licensed under the MIT License.
