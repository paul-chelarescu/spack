##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RShape(RPackage):
    """Functions for plotting graphical shapes such as ellipses, circles,
       cylinders, arrows, ..."""

    homepage = "https://cran.r-project.org/package=shape"
    url      = "https://cran.r-project.org/src/contrib/shape_1.4.3.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/shape"

    version('1.4.3', '2a807bf95e7decc71478f805221852da')
    version('1.4.2', '75557c43a385b9cc0c4dff361af6e06c')
