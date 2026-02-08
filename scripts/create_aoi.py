import geopandas as gpd
from shapely.geometry import box
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = Path("data")
AOI_DIR = DATA_DIR / "aoi"

def create_aoi(min_lon, min_lat, max_lon, max_lat, output_path):
    # Create a bounding box geometry
    aoi_geom = box(min_lon, min_lat, max_lon, max_lat)

    # Create a GeoDataFrame
    aoi_gdf = gpd.GeoDataFrame(
        {"name": ["AOI_0.3km2"]},
        geometry=[aoi_geom],
        crs="EPSG:4326"
    )

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save shapefile
    aoi_gdf.to_file(output_path)

    print(f"AOI saved to {output_path}")


if __name__ == "__main__":
    # Final locked AOI (~0.3 km²)
    create_aoi(
        min_lon=77.492900,
        min_lat=28.450900,
        max_lon=77.498600,
        max_lat=28.455800,
        output_path=AOI_DIR / "aoi.shp"
    )

