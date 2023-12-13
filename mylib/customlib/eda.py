#################################
import os
import pandas as pd
from . import environments as env
import webbrowser

##### Dtale #####
import dtale
import dtale.global_state as global_state
global_state.set_app_settings(dict(enable_custom_filters=True))
global_state.set_chart_settings({'scatter_points': 25000, '3d_points': 40000})

#### pandas profiling ####
from ydata_profiling import ProfileReport
#### autoviz ####
from autoviz import AutoViz_Class
# %matplotlib inline

########### import end ###################
dirs = env.hosters()
reportDir = dirs.getReportDir()

# hst = hst.
# reportDir = hst.getReportDir()
######################################
class reporter:
    def __init__(self, data):
        self.data = data # input as dataframe
        self.reportDir = reportDir

    def dtale_report(self):
        d = dtale.show(self.data)
        d.open_browser()

    def ydata_profiling(self):
        reportFile = os.path.join(self.reportDir,"ydata_report.html")

        profile = ProfileReport(self.data, title="Profiling Report")
#         profile.to_notebook_iframe()
#         profile.to_widgets()
        profile.to_file(reportFile)

        try:
           webbrowser.open('file://' + reportFile, new=2)
        except FileNotFoundError:
            print("The file does not exist.")

    def autoviz_report(self):
        AV = AutoViz_Class()
        dft = AV.AutoViz('',dfte=self.data, save_plot_dir=self.reportDir, verbose=2)


