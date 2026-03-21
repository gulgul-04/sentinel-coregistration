import rioxarray
import matplotlib.pyplot as plt

def plot_alignment(optical_path: str, radar_path: str):
    print(f"\n--- Visualizing Alignment ---")
    print("Loading images..")

    #load the datasets
    optical = rioxarray.open_rasterio(optical_path)
    radar = rioxarray.open_rasterio(radar_path)

    #setting up side by side figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle("Coregistration verification: Sentinel-2 vs Sentinel-1", fontsize=16)

    print ("Plotting Sentinel-2 (Optical) Image...")

    optical[0].plot.imshow(
        ax=ax1, 
        cmap='Greys_r', 
        robust=True, 
        add_colorbar=False
    )
    ax1.set_title("Sentinel-2 (Optical Band 4)")
    ax1.set_axis_off() # Hides the latitude/longitude axes for a clean look

    print("Plotting Radar (Sentinel-1)...")
    radar[0].plot.imshow(
        ax=ax2, 
        cmap='Greys_r', 
        robust=True, 
        add_colorbar=False
    )
    ax2.set_title("Sentinel-1 (Radar VV - Coregistered)")
    ax2.set_axis_off()

    # Adjust layout so it fills the window perfectly
    plt.tight_layout()
    
    print("Success! Displaying plot. (Close the image window to end the script).")
    plt.show()

    # Clean up RAM
    optical.close()
    radar.close()