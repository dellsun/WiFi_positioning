John Cavalieri

To use the locator, simply execute:
sudo ./Locator.sh
where root is required for the iw command to scan wireless channels.
Additionally iw version 3.14 is required, I have included a binary in
the Scripts folder that will probably work on most Unix systems; else it
can be easily installed or upgraded. Earlier versions of iw have different
output and thus will not be parsed properly. Gawk must also be installed,
but this comes on most Unix-like systems.  

Right now it just gives a location but I am looking into displacement vectors so 
that a person moving with their phone switching AP's will have a particular vector and
that will aide in determining future location i.e. if the WiFi signature currently indicates
room 400 but the person is moving past room 400 then there ought to be a way to handle that
