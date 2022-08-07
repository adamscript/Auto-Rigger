<h1 align="center">
  Awan's Auto Rigging Toolkit for Autodesk Maya
</h1>
<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/69242299/183228839-b4356401-ebe6-4091-8059-513e7d92829c.png" alt="autorigger_rigresults_screenshot" width="300" />
</p>
<br>

## Introduction

With this Auto Rigging tool you can build a 3D character rig without building it yourself from scratch. All you have to do is place a few markers, and then the script will do the rest. **This tool will save you hours if not days of rigging work**.

## Getting Started
### Installation

1. Clone/download the zip file
2. Extract it (you can do it wherever you want)

Now you have two options:  

3. Run `install.bat` (for windows, this file will do the steps below automatically)

or

3. Create a new `.mod` file, you can name it whatever you want (e.g. awtorigger.mod)
4. Inside that file, type in `+ AwtoRigger 1.0 [your awtorigger full directory]`

e.g.

    + AwtoRigger 1.0 C:\Users\awwwan\Awan-Auto-Rigger

5. Move the `.mod` file into one of these directories :

**Default for Windows**
```
<user’s directory>/My Documents/Maya/<version>/modules

<user’s directory>/My Documents/Maya/modules

C:/Program Files/Common Files/Autodesk Shared/Modules/Maya/<version>

C:/Program Files/Common Files/Autodesk Shared/Modules/Maya

<maya_directory>/modules/
```

**Default for Mac OS X, Linux**
```
$MAYA_APP_DIR/Maya/<version>/modules

$MAYA_APP_DIR/Maya/modules

/usr/autodesk/modules/Maya/<version>

/usr/autodesk/modules/Maya
```

More about this [here](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2020/ENU/Maya-EnvVar/files/GUID-228CCA33-4AFE-4380-8C3D-18D23F7EAC72-htm.html) and [here](https://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=__files_GUID_CB76E356_753B_4837_8C5B_3296C14872CA_htm)  

## Usage

1. **Launch Maya** (or restart Maya if you already have it opened). 
2. If everything was set up correctly, you should see the menu for `Awto Rigger` on the menu bar.

    ![autorigger_menubar_screenshot](https://user-images.githubusercontent.com/69242299/183229169-44e8b5b9-d19e-4ce0-95ec-add8001e248e.png)

3. **Create guides**, and adjust the markers based on the shape of your character model. You can rotate and scale them when needed, but you must not delete any marker individually.
4. **Awto Rig!** Sit back and relax while the script is building the rig for you.

## Support
If you are having issues or found a bug, feel free to [open an issue](https://github.com/adamscript/Auto-Rigger/issues). Also if you have questions about the project, feel free to reach out at: <adam@adamscript.com>.

## Features
### Toolkit
The main interface for this tool. It covers main functionalities such as guide marker creation and automatic rig generation. It includes options for IK Control, Reverse Foot Control, and custom Picker GUI creation. It also includes some tools needed for curves editing, which can be used to fit the generated controller shapes on the character model better.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69242299/183229012-c50692e3-8f74-4ec6-9436-b7e7e8350502.png" alt="autorigger_toolkit_screenshot" />
</p>

### Picker GUI
Optional GUI for controller selection. Locations of the buttons will be adjusted dynamically with the shape of the 3D model of the character on the rig.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69242299/183229016-7a32fdc0-a975-4730-b97c-96ff5eb6dc30.png" alt="autorigger_picker_screenshot" />
</p>

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/69242299/183294091-6879443f-c2c4-41ab-a9a7-6712d541fb60.png" alt="autorigger_pickerresults_screenshot" />
</p>

## Reflection
For my college final project, I created an Auto Rigging tool for Autodesk Maya that can be used to speed up the rigging process for humanoid 3D character creation. I’m not really a fan of building a rig from scratch for every character that I made. So I wrote this tool to make the rigging process quicker by letting the script do the repetitive work. I used this tool to rig this character (I'm not best at animation yet but I tried 😂).

<p align="center">
  <img src="https://user-images.githubusercontent.com/69242299/183229338-b34c9975-1c10-4e14-9371-279bad78b995.gif" alt="autorigger_tabby_gif" />
</p>

Hopefully this tool can be useful for any 3D artist who needs it.

## Inspiration
This project is inspired by these awesome tools. Check them out!
- [mGear](http://www.mgear-framework.com/)
- [Advanced Skeleton](https://www.animationstudios.com.au/advanced-skeleton)
