# -*- coding: utf-8 -*-
# Copyright (C) 2018 Matthias Luescher
#
# Authors:
#  Matthias Luescher
#
# This file is part of edi-boot-shim.
#
# edi-boot-shim is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# edi-boot-shim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with edi-boot-shim.  If not, see <http://www.gnu.org/licenses/>.

import edi_boot_shim


def test_command_line_interface_setup():
    parser = edi_boot_shim._setup_command_line_interface()
    assert 'edi-boot-shim' in parser.description
