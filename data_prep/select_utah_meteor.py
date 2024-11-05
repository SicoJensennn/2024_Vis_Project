from glob import glob
import xarray as xr

files = glob("../../../haskins-group1/data/ExtData/GEOS_0.25x0.3125_NA/GEOS_FP/2017/0*")
files.sort()

all_months = []
for month in files[:3]:
    days = glob(month + "/*A1*")
    print(days)
    month = xr.concat([xr.open_dataset(day).sel(lat = slice(37,42), lon = slice(-114,-109)) for day in days], dim = 'time')
    all_months.append(month)

utah = xr.concat(all_months, dim = 'time')


# PRECSNO (snow fall), PRECTOT (total precipitation) T2M (2m-air temperature)
utah_meteo = utah[['PRECSNO', 'PRECTOT', 'T2M']]
utah_meteo.to_netcdf("utah_meteo_GEOS.nc")