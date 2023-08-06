# robot-screenshot-player
A robot listener for capturing screenshot before and after execution of each keyword in robot automation framework.Once the complete execution is done it will create a html file which will displayed all  screenshot for corresponding robot script.


## Features
- Capture screenshot before and after execution of each keyword
- Generate html file which will show all the screenshots 
<!-- 
## Requirements
| Software | version | -->

 
# Project Depencecy
| Library                        | Description                                  |
| ------------------------------ | -------------------------------------------- |
| request                        | Used for  handling http request and response |
| robotframework                 | robot framework                              |
| shutil                         |                                              |
| robotframework-seleniumlibrary | used for web application automation          |
| os                             |                                              |
| selenium                       |                                              |



# References and docs
[SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
[appiumlibrary](https://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html)



## _Setup Guide_
# To install library
pip install robot-screenshot-player
# How to run with robot
robot  --listener ScreenShotPlayer;${path where to store entire report} .......


