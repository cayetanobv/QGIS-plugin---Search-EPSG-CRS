# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Search EPSG CRS
                                 A QGIS plugin
 Search for a valid CRS on the basis of an EPSG code.
 This plugin uses epsg.io
                              -------------------
        begin                : 2014-05-05
        copyright            : (C) 2014 by Cayetano Benavent
        email                : cayetanobv@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load searchEpsgCrs class from file searchEpsgCrs
    from searchepsgcrs import SearchEpsgCrs
    return SearchEpsgCrs(iface)
