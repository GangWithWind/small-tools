import sys
import glob
import hashlib
import os
import commands

out = 'a.out'
ini_file = 'pMakefile'
compiler = 'g++'
c11 = '-std=c++11'
opt = '-g -Wall'


def updata_ini(src, out):
    ini = open(ini_file,'w')
    ini.write(out + '\n')
    for onefile in src :
        ini.write(onefile + ';' + '0\n')
    ini.close()

def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
        
def compile_one(name,aim):
    command = compiler+' '+opt+' '+c11+' -c '+name+' -o '+aim
    (status, output) = commands.getstatusoutput(command)
    print '============compile '+name+'=============='
    print command
    print output
    return status

def link_one(name,aim):
    command = compiler+' '+opt+' '+c11+' '+name+' -o '+aim
    (status, output) = commands.getstatusoutput(command)
    print '============Link=============='
    print command
    if(output != ''):
        print output
    return status

def pcompile():
    ini = open(ini_file,'r')
    output = ini.readline()
    lines = ini.readlines()
    ini.close()
    newini = []
    newini.append(output)
    allname = []
    
    for line in lines:
        line = line.rstrip()
        [name,hashv] = line.split(';')
        this_md5 = CalcMD5(name)
        ofile = name.split('.')
        ofile = ofile[0:-1]
        ofile.append('o')
        ofile = '.'.join(ofile)
        allname.append(ofile)
        if( this_md5 == hashv and os.path.isfile(ofile)):
            print 'skip: '+ofile
            newini.append(line)
        else:
            if( compile_one(name,ofile) == 0):
                newini.append(name+';'+this_md5+'\n')
            else:
                newini.append(name+';'+hashv+'\n')
    link_one(' '.join(allname),output.rstrip())
    
    ini = open(ini_file,'w')
    for line in newini:
        ini.write(line.rstrip()+'\n')
    ini.close()

def add_new(names):
    ini = open(ini_file,'w+')
    for name in names:
        ini.write(name+'\n')
    ini.close()
            

def clean():
    ini = open(ini_file,'r')
    output = ini.readline()
    lines = ini.readlines()
    ini.close()
    ini = open(ini_file,'w')
    ini.write(output)
    for line in lines:
        [name,hashv] = line.split(';')
        ofile = name.split('.')
        ofile = ofile[0:-1]
        ofile.append('o')
        ofile = '.'.join(ofile)
        print 'delete '+ofile+'...'
        (status, output) = commands.getstatusoutput('rm -f '+ofile)
        ini.write(name+';'+'0'+'\n')
    ini.close()
    

if(len(sys.argv) > 1):
    cmd2 = sys.argv[1]
    if(cmd2 == 'clean'):
        clean()
    elif(cmd2 == 'add'):
        src = sys.argv[2:]
        add_new(src)
        pcompile()
    elif(len(sys.argv) == 2):
        src = sys.argv[1]
        updata_ini(src, out)
        pcompile()
    else:
        src = sys.argv[1:-1]
        out = sys.argv[-1]
        updata_ini(src, out)
        pcompile()
else:
    pcompile()