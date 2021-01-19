"""
Based on:

    https://gis.stackexchange.com/questions/88209/python-mapping-in-matplotlib-cartopy-color-one-country

    and

    https://github.com/SciTools/cartopy/issues/1303

"""
import matplotlib.pyplot as plt
import cartopy
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.PlateCarree())
#ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
#ax.add_feature(cartopy.feature.COASTLINE)
#ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
#ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
#ax.add_feature(cartopy.feature.RIVERS)
ax.set_extent([-150, 60, -25, 60])

shpfilename = shpreader.natural_earth(resolution='110m',
                                      category='cultural',
                                      name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
countries = reader.records()

countries_visited = [
    'ARG',
    'BEL',
    'CAN',
    'CHE',
    'CUB',
    'DEU',
    'DNK',
    'FRA',
    'GBR',
    'GTM',
    'HND',
    'IND',
    'ITA',
    'JPN',
    'KEN',
    'KHM',
    'LAO',
    'MEX',
    'NLD',
    'POL',
    'SWE',
    'THA',
    'USA',
    'ZMB',
]

key = 'ADM0_A3'

for country in countries:
    print(country.attributes['NAME_EN'])
    print(country.attributes[key])
    if country.attributes[key] in countries_visited:
        ax.add_geometries([country.geometry], ccrs.PlateCarree(),
                          facecolor=(0, 0, 1),
                          label=country.attributes[key])
    else:
        ax.add_geometries([country.geometry], ccrs.PlateCarree(),
                          facecolor=(0, 1, 0),
                          label=country.attributes[key])

plt.show()
