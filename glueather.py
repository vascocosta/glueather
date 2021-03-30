#!/usr/bin/env python3

# Copyright (C) 2021 Vasco Costa (gluon) <vascomacosta at gmail dot com>
#
# This file is part of glueather.
#
# glueather is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# glueather is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

import json
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from ui_mainwindow import Ui_MainWindow

from weathermanager import WeatherManager, WeatherError

CONF_PATH    = 'conf.json'
ICON_PATH    = 'icons/glueather.ico'
WINDOW_TITLE = 'glueather'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.zoomIn(2)
        self.ui.lineEdit.returnPressed.connect(self.fetch_weather)
        self.ui.pushButton.clicked.connect(self.fetch_weather)
        self.conf = {'api_key': '0', 'location': 'London', 'units': 'C'}
        self.load_conf()
        self.fetch_weather()

    def load_conf(self):
        try:
            with open(CONF_PATH, 'r') as f:
                self.conf = json.load(f)
            self.ui.lineEdit.setText(self.conf['location'])
            if self.conf['units'].lower() in ('f', 'fahrenheit'):
                self.ui.radioButton_2.setChecked(True)
        except Exception:
            QMessageBox.critical(self, "Error", "Problem reading configuration file.")

    def save_conf(self):
        api_key = self.conf['api_key']
        location = self.ui.lineEdit.text()
        if self.ui.radioButton.isChecked():
            units = 'C'
        else:
            units = 'F'
        conf = {'api_key': api_key, 'location': location, 'units': units}
        try:
            with open(CONF_PATH, 'w') as f:
                json.dump(conf, f, ensure_ascii=False, indent=4)
        except Exception:
            QMessageBox.critical(self, "Error", "Problem writing configuration file.")

    def closeEvent(self, event):
        self.save_conf()
        event.accept()

    def fetch_weather(self):
        output = ""
        location = self.ui.lineEdit.text()
        if self.ui.radioButton_2.isChecked():
            units = 'f'
        else:
            units = 'c'
        wm = WeatherManager(self.conf['api_key'], units)
        if self.ui.checkBox.isChecked():
            try:
                current_weather = wm.current(location)
                output += f"<h1>Current weather at - {current_weather['location']}</h1>" + \
                          f"<hr>" + \
                          f"<table border='1' width='100%' cellpadding='10'>" + \
                          f"<tr><td><b>Conditions</b></td><td>{current_weather['description']}</td></tr>" + \
                          f"<tr><td><b>Temperature</b></td><td>{current_weather['temperature']}</td></tr>" + \
                          f"<tr><td><b>Humidity</b></td><td>{current_weather['humidity']}</td></tr>" + \
                          f"<tr><td><b>Pressure</b></td><td>{current_weather['pressure']}</td></tr>" + \
                          f"<tr><td><b>Wind</b></td><td>{current_weather['wind']}</td></tr>" + \
                          f"</table>"
                self.ui.textEdit.setHtml(output)
            except WeatherError as e:
                QMessageBox.warning(self, "Error", e.message)
                return
        if self.ui.checkBox_2.isChecked():
            try:
                three_h_forecast = wm.hourly(location)
                output += f"<h1>Hourly forecast for - {three_h_forecast[0]['location']}</h1>" + \
                          f"<hr>" + \
                          f"<table border='1' cellpadding='10' width='100%'>" + \
                          f"<tr><td><b>Time</b></td><td><b>Conditions</b></td><td><b>Temperature</b></td><td><b>Humidity</b></td><td><b>Pressure</b></td><td><b>Wind</b></td></tr>"
                for i, forecast in enumerate(three_h_forecast, start=1):
                    output += f"<tr><td>{3*i} hours</td>" + \
                              f"<td>{forecast['description']}</td>" + \
                              f"<td>{forecast['temperature']}</td>" + \
                              f"<td>{forecast['humidity']}</td>" + \
                              f"<td>{forecast['pressure']}</td>" + \
                              f"<td>{forecast['wind']}</td></tr>"
                output += f"</table>"
                self.ui.textEdit.setHtml(output)
            except WeatherError as e:
                QMessageBox.warning(self, "Error", e.message)
                return
        if self.ui.checkBox_3.isChecked():
            try:
                daily_forecast = wm.daily(location)
                output += f"<h1>Daily forecast for - {daily_forecast[0]['location']}</h1>" + \
                          f"<hr>" + \
                          f"<table border='1' cellpadding='10' width='100%'>" + \
                          f"<tr><td><b>Day</b></td><td><b>Conditions</b></td><td><b>Temperature</b></td><td><b>Humidity</b></td><td><b>Pressure</b><td><b>Wind</b></td></tr>"
                for i, forecast in enumerate(daily_forecast, start=1):
                    output += f"<tr><td>{forecast['day']}</td>" + \
                              f"<td>{forecast['description']}</td>" + \
                              f"<td>{forecast['temperature']}</td>" + \
                              f"<td>{forecast['humidity']}</td>" + \
                              f"<td>{forecast['pressure']}</td>" + \
                              f"<td>{forecast['wind']}</td></tr>"
                self.ui.textEdit.setHtml(output)
            except WeatherError as e:
                QMessageBox.warning(self, "Error", e.message)
                return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(WINDOW_TITLE)
    window.setWindowIcon(QIcon(ICON_PATH))
    window.show()
    sys.exit(app.exec())
