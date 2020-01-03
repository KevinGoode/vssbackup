Use Eclipse with PyDev as IDE. Can run and debug tests from here.

On Centos 7:

1.) Download and install eclipse : http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/neon/1a/eclipse-java-neon-1a-linux-gtk-x86_64.tar.gz  

2.) Create icon for eclipse on desktop, by first creating a desktop link for Terminal and then copying this and changing icon to eclipse and target to eclipse:  

a.) Open the file browser (the "home" folder shortcut is on the desktop by default)  

b.) Click the "Computer" link on the left navigation panel and go to "/usr/shared/applications". This should now display all the applications icons/shortcuts in the browser window. c.)  "Right-click Icon->Context Menu->Copy To". This will bring up another browser window titled "Select Destination".  

c.) Select (left-click) the "Desktop" folder in the left navigation panel, and the click the "Select" button in the bottom right.  

3.) Install and setup pydev in eclipse. a.) From Help/Eclipse market place, search for pydev and then install  

4.) Install pep8  

a.) http://rpm.pbone.net/index.php3/stat/4/idpl/35509084/dir/centos_7/com/python-pep8-1.5.7-2.el7.noarch.rpm.html  

b.) rpm -Uvh python-pep8-1.5.7-2.el7.noarch.rpm  

5.) Install pylint: sudo yum install pylint.noarch  

6.) Install PyQt4: sudo yum install python2-pyside  
