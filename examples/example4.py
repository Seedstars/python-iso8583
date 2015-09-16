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
	

'''
   00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15    0123456789012345
   -----------------------------------------------    ----------------
00 30 32 31 30 42 32 33 38 30 30 30 31 30 32 43 30    0210B238000102C0
01 38 30 30 34 30 30 30 30 30 30 30 30 30 30 30 30    8004000000000000
02 30 30 30 32 31 30 30 30 30 30 30 30 30 30 30 30    0002100000000000
03 30 30 31 37 30 30 30 31 30 38 31 34 34 36 35 34    0017000108144654
04 36 39 34 32 31 36 31 34 34 36 35 37 30 31 30 38    6942161446570108
05 31 31 30 30 33 30 31 30 30 30 30 30 30 4e 33 39    1100301000000N39
06 39 39 31 35 34 34 34 33 30 33 35 30 30 30 31 39    9915444303500019
07 39 39 31 35 34 34 39 38 36 30 32 30 20 56 61 6c    991544986020 Val
08 6f 72 20 6e 61 6f 20 70 65 72 6d 69 74 69 21 21    ue not allowed!!
09 30 30 39 30 30 30 30 39 35 34 39 32                009000095492

'''
#i2 = ISO8583(debug=True)
i2 = ISO8583()

iso2 = '0210B238000102C080040000000000000002100000000000001700010814465469421614465701081100301000000N399915444303500019991544986020 Value not allowed!!009000095492'
print ('\n\n\n------------------------------------------\n')
print ('This is the ISO <%s> parse it!' % iso2)

i2.setIsoContent(iso2)
print ('Bitmap = %s' %i2.getBitmap()) 
print ('MTI = %s' %i2.getMTI())

print ('Bits')
v3 = i2.getBitsAndValues()
for v in v3:
	print ('(1) Bit %s of type %s and value = %s' % (v['bit'],v['type'],v['value']))
	

# in this case, we need to redefine a bit because default bit 42 is A and in this especification is "N"
# the rest remain, so we use get's to copy original values :)
i2.redefineBit(42, '42', i2.getLargeBitName(42), 'N', i2.getBitLimit(42), i2.getBitValueType(42) )	
print ('\nBit 42 redefined...\n')
	
i3 = ISO8583(iso=iso2)
print ('Bitmap = %s' %i3.getBitmap()) 
print ('MTI = %s' %i3.getMTI())

print ('Bits inside')
v4 = i3.getBitsAndValues()
for v in v4:
	print ('(2) Bit %s of type %s and value = %s' % (v['bit'],v['type'],v['value']))	

	
