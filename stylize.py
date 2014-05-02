'''
Created on 2014/04/15

A simple script that converts Android XML view tag properties into a style tag. 
Replace the text inside the viewprops variable with the view tag that you want to stylize. Will print out to console.

@author: Wayne
'''

import re

viewprops = '''

    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="?attr/BMBgPrimaryColor"
    android:orientation="vertical"
    android:paddingLeft="15dp"
    android:paddingRight="15dp" >

        '''
        
styleName = 'pinLayout'


def stylize(rawProperties, styleName):

    #printing the opening tag of the style
    openTag = '<style name="{0}">'.format(styleName)
    print openTag
    
    holder = []
    
    #grabbing the text line by line
    propsSplit = rawProperties.split('\n')
    
    for line in propsSplit:
        
        #weens out opening view tags
        if '=' not in line:
            continue
        
        propertyLineSplit = line.rsplit('=')
        
        # grab name, strip out whitespaces
        propertyName = propertyLineSplit[0].strip()
        
        #don't put xmlns into style
        if "xmlns:android" in propertyName:
            continue
        
        #don't put ids into style
        if "android:id" in propertyName:
            holder.append(line);
            continue
        
        #don't put text into style
        if re.compile('^android:text$').match(propertyName):
            holder.append(line);
            continue
        
        #grabbing the propertyLineSplit name and making the opening tag for the item
        itemOpenTag = '\t<item name="{0}">'.format(propertyName)
        
        #grab value on right side of original string, find the value between the quotes
        propertyValue = propertyLineSplit[1]
        propertyValue = re.findall('"(.*?)"', propertyValue)[0]

        item = itemOpenTag + propertyValue + '</item>'
        print item
    
    #print closing tag
    print '</style>'
    print ''
    
    
    print 'style="@style/{0}"'.format(styleName)
    #print the id and text that we weened out, if they exist
    for item in holder:
        print item.strip()
    print '/>'

    

stylize(viewprops, styleName)



