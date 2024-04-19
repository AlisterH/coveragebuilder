"""
/***************************************************************************
 CoverageBuilder
                                 A QGIS plugin
 Creation de synoptiques grille ou dynamique pour utiliser dans un atlas
                             -------------------
        begin                : 2012-02-22
        copyright            : (C) 2012 by Experts SIG / Biotope
        email                : dev-qgis@biotope.fr
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
from __future__ import absolute_import
# from PyQt4.QtCore import *

def name():
    return "Coverage Builder"
def description():
    return "Create rectangles to use as an input layer for atlas generation"
def version():
    return "version 0.5.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "3.0"

def classFactory(iface):
    # load CoverageBuilder class from file CoverageBuilder
    from .coveragebuilder import CoverageBuilder
    return CoverageBuilder(iface)
