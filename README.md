# Sentinel Coregistration

A Python-based workflow for downloading, visualizing, and coregistering Sentinel-1 (VV polarization) and Sentinel-2 optical data over a defined Area of Interest (AOI), with a focus on pixel-to-pixel alignment and multisensor geospatial analysis.

---

## Project Objectives

- Define a small Area of Interest (≈ 0.3 km²)
- Acquire Sentinel-1 (SAR, VV polarization) and Sentinel-2 (optical) data
- Visualize spatial and pixel-level misalignment between datasets
- Understand and apply image coregistration concepts
- Perform preprocessing using Python and open-source GIS tools

---

## Data Sources

- **Sentinel-1**: SAR GRD data (VV polarization)  
  Source: ASF DAAC / Copernicus Open Access Hub
- **Sentinel-2**: Optical imagery (Level-2A, Band 3 or Band 4)  
  Source: Copernicus Open Access Hub / Google Earth Engine

> Raw satellite data is not included in this repository due to size constraints.

---

## Project Structure

```text
sentinel-coregistration/
│
├── README.md
├── .gitignore
│
├── env/                # Python virtual environment (ignored)
├── data/               # Sentinel datasets (ignored)
│   ├── sentinel1/
│   └── sentinel2/
│
├── scripts/            # Python processing scripts
└── outputs/            # Generated results (ignored)# Sentinel Coregistration
