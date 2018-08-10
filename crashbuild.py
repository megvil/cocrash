import re
import os
import time


def readfile(path, fileName, libfileName):
    print(path)
    file_object = open(path, 'r')
    txtnew = open('./output/' + fileName, "w")
    # txtnew = open('./output/' +'m_'+ fileNmae, "w")
    find_mark = 0
    for line in file_object:
        if find_mark == 1:
            for idx in range(len(line)):
                if line[idx] == '+':
                    name = line[idx + 1:len(line) - 1]
                    cmd = os.popen('./tool/arm-linux-androideabi-addr2line -C -f -e' + libfileName + name).read()
                    # print(cmd)
                    # print(name)
                    newline = line.replace(name, cmd)
                    # print(newline)
                    txtnew.write(newline)
                    find_mark = 0
                    break
            break
        else:
            txtnew.write(line)
        if re.match('Thread 0', line) != None:
            find_mark = 1

    localtime = time.asctime(time.localtime(time.time()))
    txtnew.write('file create time:' + localtime)
    txtnew.write('\npower by Andye ')
    txtnew.close()
    file_object.close()


rootDumpDir = './house'
rootLibDir = './libso'
liblist = os.listdir(rootLibDir)
for i in range(0, len(liblist)):
    path = os.path.join(rootLibDir, liblist[i])
    # for filename in path:
    if os.path.splitext(path)[1] == '.so':
        # readfile(path, fileNmae)
        libfileName = path
        # print(libfileName)

dumplist = os.listdir(rootDumpDir)
for i in range(0, len(dumplist)):
    dumppath = os.path.join(rootDumpDir, dumplist[i])
    fileNmae = os.path.basename(dumppath)
    if os.path.isfile(dumppath):
        # for filename in path:
        if os.path.splitext(dumppath)[1] == '.txt':
            fileName = dumppath
            # print(fileName)
            readfile(dumppath, fileNmae, libfileName)


