# -*- coding: utf-8 -*-
"""functions to add surface water to a mf model using the ghb package."""

import logging
import os
import geopandas as gpd
import nlmod
import datetime as dt
import xarray as xr

from .. import mdims, util

logger = logging.getLogger(__name__)


def get_gdf_surface_water(model_ds):
    """read a shapefile with surface water as a geodataframe, cut by the extent
    of the model.

    Parameters
    ----------
    model_ds : xr.DataSet
        dataset containing relevant model information

    Returns
    -------
    gdf_opp_water : GeoDataframe
        surface water geodataframe.
    """
    # laad bestanden in
    fname = os.path.join(nlmod.NLMOD_DATADIR, 'opp_water.shp')
    gdf_swater = gpd.read_file(fname)
    gdf_swater = util.gdf_within_extent(gdf_swater, model_ds.extent)

    return gdf_swater


def get_sea_and_lakes(model_ds,
                      modelgrid,
                      da_name,
                      use_cache=False):
    """Get data arrays with area, cond en peil from the Northsea and big lakes
    in the Netherlands.

    Parameters
    ----------
    model_ds : xr.DataSet
        dataset containing relevant model grid information
    modelgrid : flopy grid
        model grid.
    da_name : str
        name of the polygon shapes, name is used to store data arrays in
        model_ds
    use_cache : bool, optional
        if True the cached ghb data is used. The default is False.

    Returns
    -------
    model_ds : xr.DataSet
        dataset with spatial model data including the ghb rasters
    """
    model_ds = util.get_cache_netcdf(use_cache, model_ds.cachedir, 'rws_oppwater.nc',
                                     surface_water_to_model_dataset,
                                     model_ds,
                                     modelgrid=modelgrid, da_name=da_name)

    return model_ds


def surface_water_to_model_dataset(model_ds, modelgrid, da_name):
    """create 3 data-arrays from the shapefile with surface water:

    - area: with the area of the shape in the cell
    - cond: with the conductance based on the area and bweerstand column in shapefile
    - peil: with the surface water lvl based on the peil column in the shapefile

    Parameters
    ----------
    model_ds : xr.DataSet
        xarray with model data
    modelgrid : flopy grid
        model grid.
    da_name : str
        name of the polygon shapes, name is used to store data arrays in
        model_ds

    Returns
    -------
    model_ds : xarray.Dataset
        dataset with modelgrid data. Has
    """
    gdf = get_gdf_surface_water(model_ds)

    area = xr.zeros_like(model_ds['top'])
    cond = xr.zeros_like(model_ds['top'])
    peil = xr.zeros_like(model_ds['top'])
    for _, row in gdf.iterrows():
        area_pol = mdims.polygon_to_area(modelgrid, row['geometry'],
                                         xr.ones_like(model_ds['top']),
                                         model_ds.gridtype)
        cond = xr.where(area_pol > area, area_pol / row['bweerstand'], cond)
        peil = xr.where(area_pol > area, row['peil'], peil)
        area = xr.where(area_pol > area, area_pol, area)

    model_ds_out = util.get_model_ds_empty(model_ds)
    model_ds_out[f'{da_name}_area'] = area
    model_ds_out[f'{da_name}_cond'] = cond
    model_ds_out[f'{da_name}_peil'] = peil

    for datavar in model_ds_out:
        model_ds_out[datavar].attrs['source'] = 'RWS'
        model_ds_out[datavar].attrs['date'] = dt.datetime.now().strftime('%Y%m%d')

    return model_ds_out
