John Cavalieri

To use the locator, simply execute:
sudo ./Locator.sh
where root is required for the iw command to scan wireless channels.
Additionally iw version 3.14 is required, I have included a binary in
the Scripts folder that will probably work on most Unix systems; else it
can be easily installed or upgraded. Earlier versions of iw have different
output and thus will not be parsed properly. Gawk must also be installed,
but this comes on most Unix-like systems.  
