# CharCodeViewer
Document version 0.1
Date 2019-01-16
Author(s): Erik Grundström

CharCodeViewer is a small and simple utility tool to display the numeric ASCII codes of characters.
The Numbers are displayed in decimal, hexadecimal and binary formats.

The tool features three ways to use it:
  * A simple to use GUI
  * Interactive command line interface
  * Command line utility that accepts arguments
  
  
  
  
How to use
CharCodeViewer must currently, in it's alpha stage, be used directly with python. As mentioned before there are three ways
to run the application. Details follow below.

GUI
The GUI is run using the following command from the source code directory:
  $ python GUI.py 
  The GUI also accepts command line arguments that will be interpreted as the initial characters displayed
  
Interactive command line interface
The Interactive version of the CLI is the way the tool is run when you don't supply arguments:
  $ python CLI.py
 
Command Line utility
To run the tool as a command line utility you must run supply the characters you want as command line arguments. Please note that
whitespace characters do not work with the command line tool since they are interpreted as separators in the command propmt itself.
Furthermore you must supply all characters unseparated, otherwise only the first argument is used, the rest are currently ignored.
Run the command line with the following command from the source directory:
  $ python CLI.py xyz
where xyz are the command line arguments



  
Requirements
The tool is built on python 3.7.1 on windows 10 and is officially supported only on this platform. No external libraries
and/or frameworks are used and it should therefore run on other platforms as well.




Terms of use
See the LICENSE.txt document found where you found this readme or on https://github.com/grunmurstraumr/CharCodeViewer for full
terms.
The short version: Standard MIT-license terms apply.
