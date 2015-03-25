import shutil
import os


#shutil.copytree()
home = os.path.expanduser('~')
androidhome = home + "/AndroidStudioProjects"
delectableHome = androidhome + "/DelectableAndroid"
meuAppHome = androidhome + "/MeuApp"


modelsDir = delectableHome + "/Delectable/app/src/main/java/com/delectable/mobile/api/models"
targetModelsDir = androidhome + "/MeuApp/app/src/main/java/com/delectable/mobile/api/models"

print os.listdir(modelsDir)

#print os.getcwd()
#print androidhome

#must remove directory first if already exists or else it will error our
if(os.path.exists(targetModelsDir)):
    shutil.rmtree(targetModelsDir)
    print "tree removed"
shutil.copytree(modelsDir, targetModelsDir)


