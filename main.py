import os
from scripts import  geo, coreg

def main():

    #define input paths 
    s2_raw_jp2 = 'data/Sen2/GRANULE/L2A_T43RGM_A041887_20250314T054014/IMG_DATA/R10m/T43RGM_20250314T052649_B04_10m.jp2'
    my_aoi = 'data/aoi/aoi.geojson'
    s1_vv_tif = 'data/Sen1/measurement/s1a-iw-grd-vv-20250315t005226-20250315t005251-058308-073539-001.tiff'

    #define output paths
    s2_clipped_tif = 'data/output/sen2_b4_clipped.tiff'
    s1_coreg_tif = 'data/output/sen1_vv_coreg.tiff'

    #coregistration pipeline
    try:
        #step1 - clip sentinel-2 image to AOI
        if os.path.exists(s2_clipped_tif):
            print(f"\n--- Skipping Clip ---")
            print(f"Found existing file: {s2_clipped_tif}")
        else:
            geo.clip_raster_to_aoi(
                raw_raster_path=s2_raw_jp2,
                aoi_file_path=my_aoi,
                output_path=s2_clipped_tif
            )

        #step2 - coregister sentinel-1 image to clipped sentinel-2 image
        coreg.pixel_matching(
            master_path=s2_clipped_tif,
            slave_path=s1_vv_tif,
            output_path=s1_coreg_tif
        )

        print("\nPipeline executed successfully! \n All preproccessing tasks completed and outputs saved.")

    except Exception as e:
        print(f"\nAn error occurred during pipeline execution: {e}")

if __name__ == "__main__": 
    main()