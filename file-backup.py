
from distutils.dir_util import copy_tree
import shutil
import time
import schedule

def createBackup():
    fromDir = "D:/katalog do skopiowania"
    toDir = "F:/dest"
    copy_tree(fromDir, toDir)
    print("Kopiowanie zakończone")

    actualTime = time.localtime(time.time())
    fileName = str(actualTime[0]) + "." + str(actualTime[1])+ "." + str(actualTime[2])+ " " + str(actualTime[3])+ "." + str(actualTime[4])
    archPath = shutil.make_archive(fileName, 'zip', toDir)
    shutil.move(archPath,toDir)
    print("Archiwum utworzone")


schedule.every().day.at('01:00').do(createBackup)

while 1:
    schedule.run_pending()
    time.sleep(1)