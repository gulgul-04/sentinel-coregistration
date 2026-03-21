import geopandas as gpd
import os
import rioxarray

def shapefile_to_boundary_geojson(
    shp_path: str,
    output_geojson: str,
    target_epsg: int = 4326):
    
    # Load the shapefile
    gdf = gpd.read_file(shp_path)

    # Check CRS
    if gdf.crs is None:
        raise ValueError("CRS is not defined in the shapefile.")

    # Reproject if needed
    if gdf.crs.to_epsg() != target_epsg:
        gdf = gdf.to_crs(epsg=target_epsg)

    # Convert polygons to boundaries (LineString / MultiLineString)
    gdf["geometry"] = gdf.geometry.boundary

    # Keep only line geometries
    gdf = gdf[gdf.geometry.geom_type.isin(["LineString", "MultiLineString"])]

    # Save as GeoJSON
    gdf.to_file(output_geojson, driver="GeoJSON")

    print(f"GeoJSON saved to {output_geojson}")
    print("Geometry types:", gdf.geometry.geom_type.unique())

    return gdf 


#function to clip large raster down to Area Of Interest and handle CRS reprojection if needed
def clip_raster_to_aoi(raw_raster_path: str, aoi_file_path: str, output_path: str):

    print(f"\n--- Clipping Raster ---")
    print(f"Loading the raw image: {raw_raster_path}")
    raw_raster = rioxarray.open_rasterio(raw_raster_path)

    print(f"Loading the AOI: {aoi_file_path}")
    aoi_gdf = gpd.read_file(aoi_file_path)

    #check to see if AOI and Image use same co-ordinate reference system (CRS)
    if aoi_gdf.crs != raw_raster.rio.crs:
        print("Reprojecting AOI to match raster CRS...")
        aoi_gdf = aoi_gdf.to_crs(raw_raster.rio.crs)

    print("Executing clipping operation...")
    #clip image and drop empty space outside the AOI
    clipped_raster = raw_raster.rio.clip(aoi_gdf.geometry, aoi_gdf.crs, drop=True)

    os.amkedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"Saving clipped image to: {output_path}")
    clipped_raster.rio.to_raster(output_path)

    #clean up memory
    raw_raster.close()
    clipped_raster.close()

    return output_path