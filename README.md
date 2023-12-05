# Readymade-EDA
This repository created for documentation of code which is used in day to day performing of EDA. Generates EDA reports in report directory using diffrent EDA tools, makes EDA task easier and saves lot of time

# prerequisites
pip install dtale
pip install ydata_profiling
pip install autoviz

# import 
import sys
myLibDir=r"D:\Data_Science\ds\mylib"
sys.path.append(myLibDir)
from customlib import fileProcessing as fp, eda

# make instance and generate/view reports
reporter = eda.reporter(df)

reporter.dtale_report()

reporter.ydata_profiling()

reporter.autoviz_report()
