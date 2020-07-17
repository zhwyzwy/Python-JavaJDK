from jpype import *
from PathJoin import path_join
import sys

jvmPath = getDefaultJVMPath()

jarPath = path_join("./fileClient/lib/")
filePath = path_join('./fileData/')

if not filePath:
    sys.exit()

startJVM(jvmPath, "-ea", "-Djava.class.path={}".format(";".join(jarPath)))

# 实例化java对象
PutClass = JClass("com.dcfs.esc.ftp.client.upload.FtpPut")
ConfigClass = JClass("com.dcfs.esc.ftp.client.FtpClientConfig")

config_filePath = "./fileClient/classes/FtpClientConfig.properties"
config_instance = ConfigClass.getInstance(config_filePath)


for file in filePath:
    put_instance = PutClass(file, '/%s' % file, 'python-javajdk', True, True, config_instance)

shutdownJVM()





