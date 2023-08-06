# -*- coding: utf-8 -*-
# @Time    : 4/8/2021 4:50 PM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : Harmonic_time.py
# @Software: PyCharm

import py_dss_interface
# 0 - Snapshot,
# 1 - Daily,
# 7 - Harmonics,
# 8 - HarmonicT,  (sequential Harmonic Mode)


dss = py_dss_interface.DSSDLL()

dss_file = r"C:\Users\ppra005\Box\Documents_PC\OpenDSS_forum\BrunoCarmelito\TestCase\ST_TestCases.dss"

dss.text("compile [{}]".format(dss_file))

for i in range(24):
    dss.text("set mode= daily")
    dss.text("set number=1")
    dss.text('set stepsize=1h')
    dss.text(f"set hour={i}")
    hour = dss.solution_read_hour() #Evaluate hour
    dss.solution_solve()
    dss.text("set mode = harmonics")
    dss.solution_solve()
    print(f"Hour={hour + 1} Losses B={dss.circuit_losses()[0]}")





