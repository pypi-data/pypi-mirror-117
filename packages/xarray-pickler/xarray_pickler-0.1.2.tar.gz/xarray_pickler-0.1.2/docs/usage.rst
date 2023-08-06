=====
Usage
=====

To use xarray-pickler in a project::

    import xarray_pickler


To use the ``open_dset`` function

.. code-block:: python

    from xarray_pickler import open_dset

    dpath = "/badc/cmip6/data/CMIP6/CMIP/IPSL/IPSL-CM6A-LR/historical/r1i1p1f1/Amon/rlds/gr/v20180803"

    # specify extra kwargs to use with xarray.open_mfdataset()
    kwargs = {'parallel': True}

    ds = open_dset(dpath, **kwargs)
    return ds


In ``etc/config.ini`` there are settings that can be configured.


Any section of the configuration file can be overwritten by creating a new INI file with the desired sections and values and then setting the environment variable ``PICKLE_CONFIG`` as the file path to the new INI file.
e.g. ``PICKLE_CONFIG="path/to/config.ini"``


The configuration settings used are listed and explained below. Explanations will be provided as comments in the code blocks if needed.
Examples are provided so these settings will not necesarily match up with what is used.

Specifying types
################

It is possible to specify the type of the entries in the configuration file, for example if you want a value to be a list when the file is parsed.

This is managed through a ``[config_data_types]`` section at the top of the INI file which has the following options::

    [config_data_types]
    # use only in xarray-pickler
    lists = pickle_dirs
    dicts =
    ints = dir_grouping_level
    floats =
    boolean = use_cftime remove_archive_dir_in_path
    # use the below if using the xarray-pickler config settings in other packages
    extra_lists =
    extra_dicts =
    extra_ints =
    extra_floats =
    extra_booleans =

Simply adding the name of the value you want to format after ``=`` will render the correct format. e.g. ``boolean = use_cftime remove_archive_dir_in_path`` will set  both ``use_cftime`` and ``remove_archive_dir_in_path`` as booleans.

Settings
########
The settings that can be configured are::

    # the default settings that will be used everytime an xarray.Dataset object is opened.
    [open_mfdataset_kwargs]
    use_cftime = True
    combine = by_coords

    [paths]
    # how many directory levels to join together to create the name of the pickle file - this reduces the length of the file path
    dir_grouping_level = 4
    # the path to the pickle file stores, to be listed in the order they should be checked for existing pickles.
    pickle_dirs = /badc/cmip6/metadata/xarray-pickles /gws/nopw/j04/cp4cds1_vol1/metadata/xarray-pickles
    # the directory to write new pickle files to
    writeable_pickle_dir = /gws/nopw/j04/cp4cds1_vol1/metadata/xarray-pickles
    # directories where the archive data is stored
    archive_dir = /badc/cmip6/data/
    # whether to remove the archive dir from the full pickle file path
    remove_archive_dir_in_path = True
