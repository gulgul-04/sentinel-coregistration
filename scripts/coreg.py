import rioxarray
from rasterio.enums import Resampling
import os
from tqdm import tqdm

def pixel_matching(master_path: str, slave_path: str, output_path: str):
    """ master path: file pathy to reference image
        slave path: file path to image being shifted and resampled to match the master
        output path: file path to save the aligned image
    """

    with tqdm(total=4, desc="Starting coregistration", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:

        #step 1: load master
        pbar.set_description("Loading Optical Master...")
        master_da = rioxarray.open_rasterio(master_path)
        pbar.update(1)

        #step 2: load slave
        pbar.set_description("Loading Radar Slave...")
        slave_da = rioxarray.open_rasterio(slave_path)
        pbar.update(1)

        #step 3: perform coregistration alignment
        pbar.set_description("Aligning Pixels (Nearest Neighbor Resampling)...")
        aligned_da = slave_da.rio.reproject_match(master_da, resampling=Resampling.nearest)
        pbar.update(1)

        #step 4: save output
        pbar.set_description("Saving Output...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        aligned_da.rio.to_raster(output_path)
        pbar.update(1)

        #clean up memory
        master_da.close()
        slave_da.close()
        aligned_da.close() 

        pbar.set_description("Coregistration Complete!")
    return output_path