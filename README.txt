John Cavalieri

To use the locator, simply execute:
sudo ./Locator.sh
where root is required for the iw command to scan wireless channels.
Additionally iw version 3.14 is required, I have included a binary in
the Scripts folder that will probably work on most Unix systems; else it
can be easily installed or upgraded. Earlier versions of iw have different
output and thus will not be parsed properly. Gawk must also be installed,
but this comes on most Unix-like systems.  

The predictions will be accurate for all rooms of the fourth floor except
room 401; there was a class during my scanning and I was unable to get in there.
Occasionally a warning message about disregarding unseen APs will be printed,
safe to ignore but the more warnings you get the less likely it is that you
are on the fourth floor of Olsen Hall
