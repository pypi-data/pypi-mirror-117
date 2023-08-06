# -*- coding: utf-8 -*-
# @Time    : 3/3/2021 12:03 PM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : bus_dis.py
# @Software: PyCharm

# First import the Package
import py_dss_interface
import pathlib
import os
# Creates an OpenDSS object
dss = py_dss_interface.DSSDLL(r"C:\Program Files\OpenDSS")

# Select the DSS model
dss_file = r"C:\Program Files\OpenDSS\IEEETestCases\4Bus-YY-Bal\4Bus-YY-Bal.DSS"
# dss_file = r"C:\Users\ppra005\Box\DOPF_Report\OpenDSSModels\420-3PVs\420_12kv\Master.DSS"
dss.text("compile [{}]".format(dss_file))

# Assuming we have just one Vsource element (Circuit element is a Vsource in OpenDSS)
dss.vsources_first()
circuit_bus1 = dss.dssproperties_read_value(str(dss.cktelement_all_property_names().index("bus1") + 1))

connected_element_found = False

dss.lines_first()
for _ in range(dss.lines_count()):
    if dss.lines_read_bus1().split(".")[0].lower() == circuit_bus1.lower():
        connected_element_found = True
        line = f"line.{dss.lines_read_name()}"
        terminal = 1
        break
    elif dss.lines_read_bus2().split(".")[0].lower() == circuit_bus1.lower():
        connected_element_found = True
        line = f"line.{dss.lines_read_name()}"
        terminal = 2
        break
    dss.lines_next()

if not connected_element_found:
    pass
    # look at other elements, transformer or maybe reactors.

dss.text(f"new energymeter.Meter element={line} terminal={terminal}")

dss.solution_solve()

print(dss.circuit_all_bus_names())
print(dss.circuit_all_bus_distances())
