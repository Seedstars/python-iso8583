"""

(C) Copyright 2009 Igor V. Custodio

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *

import traceback

import os
os.system(['clear','cls'][os.name == 'nt'])

#Enable Debug Information
# It's print a lot of information ... So only use if you are developping the library!
p2 = ISO8583(debug=True)
p2.setMTI('0800')
p2.setBit(2,2)
p2.setBit(4,4)
p2.setBit(12,12)
p2.setBit(21,21)
p2.setBit(17,17)
p2.setBit(49,986)
p2.setBit(99,99)
print ('MTI = %s' %p2.getMTI()) 
print ('Bitmap = %s' %p2.getBitmap()) 
p2.showIsoBits();


iso = p2.getRawIso()
#Show debug information of the parsing function
print ('\n\n\n------------------------------------------\n')
print ('Parsing ... <%s> ' % iso)


i = ISO8583()
i.setIsoContent(iso)
#Show information ... to compare
print ('MTI = %s' %i.getMTI()) 
print ('Bitmap = %s' %i.getBitmap()) 
print ('Here we have bits')
i.showIsoBits()


print ('This is the bits and values (1)')
v1 = p2.getBitsAndValues()
print ('\n%s\n' %v1)

print ('This is the bits and values (2)')
v2 = i.getBitsAndValues()	
print ('\n%s\n' %v2)

print ('One way of printing the information ...!')
for v in v1:
	print ('Bit %s of type %s has value = %s' % (v['bit'],v['type'],v['value']))


print ('Another way...')
for v in range(0,len(v2)):
	print ('Bit %s of type %s has value = %s' % (v2[v]['bit'],v2[v]['type'],v2[v]['value']))
	
	
