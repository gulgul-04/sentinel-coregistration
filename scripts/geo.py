import geopandas as gpd


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