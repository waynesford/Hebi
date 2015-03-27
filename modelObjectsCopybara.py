import shutil
import os

'''
A script that syncs model objects and endpoint model objects to a lightweight development project for faster build times.
'''
def copyDir(source, target):

    print "Copying directory:"
    print source
    print os.listdir(source)

    #must remove directory first if already exists or else it will error our
    if(os.path.exists(target)):
        shutil.rmtree(target)
    shutil.copytree(source, target)

androidhome = os.path.expanduser('~') + "/AndroidStudioProjects"
#print os.getcwd()
#print androidhome

modelsSource = androidhome + "/DelectableAndroid/Delectable/app/src/main/java/com/delectable/mobile/api/models"
modelsTarget = androidhome + "/MeuApp/app/src/main/java/com/delectable/mobile/api/models"

endpointModelsSource = androidhome + "/DelectableAndroid/Delectable/app/src/main/java/com/delectable/mobile/api/endpointmodels"
endpointModelsTarget = androidhome + "/MeuApp/app/src/main/java/com/delectable/mobile/api/endpointmodels"


copyDir(modelsSource, modelsTarget)
copyDir(endpointModelsSource, endpointModelsTarget)


