ConvertXML is a script that reformats an IGV session that was originally created on a Windows system,
so that the session could also be opened on a macOS device. 

Positional arguments:
1. igvSession - Name of IGV session
2. convertedFile - Name for newly formatted file 

The script implements the ArgParser library and can be called through the command line, along with two
additional arguments. The first parameter requires the path and name to the igv session, which specifies
the igv session that needs to be reformatted. Then the second parameter is the name under which the 
reformatted session would be saved as.

Example of a command that would be used to run the script in a command line:
python ConvertXML.py Y:\data\igv_sessions\AndreySession.xml ConvertedFile