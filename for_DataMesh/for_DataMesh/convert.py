import numpy as np
import xarray as xr

# Load the .npy file
npy_file = "10perc_disps_sites_c_MDEz_uniform.npy"
data = np.load(npy_file)

# Create an xarray DataArray from the numpy array
data_array = xr.DataArray(data)

# Convert the DataArray to a Dataset (optional, but recommended for metadata)
dataset = data_array.to_dataset(name='data')

# Save the dataset to a NetCDF file
nc_file = '10perc_disps_sites_c_MDEz_uniform.nc'
dataset.to_netcdf(nc_file)

print(f"Converted {npy_file} to {nc_file}")
