import shutil
import os
import re

viewFile = "/Users/wayne/AndroidStudioProjects/DelectableAndroid/Delectable/app/src/main/java/com/delectable/mobile/ui/tagpeople/widget/TagPeopleRow.java"
file = open(viewFile, 'r').read()
print file

if "R.layout" in file:
    print "true"
else:
    print "false"

matches = re.findall("R\.[._a-z0-9]*", file)

for x in matches:
    print x

tuple = ('anim', 'attr', 'bool', 'drawable', 'id', 'integer', 'layout',
         'menu', 'mipmap', 'plurals', 'raw', 'string', 'style', 'styleable')

print tuple




print matches