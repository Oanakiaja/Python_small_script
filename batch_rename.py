# 做SRTP时对图像的分类使用的，到时候想复用的话改代码就行
import os,shutil

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print('no'+ srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print ('move ', srcfile,' to ',dstfile)

def rename(num, foldpath,path):
        print(foldpath)
        filelist=os.listdir(foldpath)#该文件夹下所有的文件（包括文件夹）
        for files in filelist:#遍历所有文件
            print(files)
            Olddir=os.path.join(foldpath,files)#原来的文件路径                
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                continue
            filename = os.path.splitext(files)[0]
            filetype = os.path.splitext(files)[-1]
            filepath = os.path.join(foldpath, filename+filetype)
            if filename == 'brain' and filetype == '.nii':
              #  Newdir=os.path.join(foldpath,str(num)+'.nii')#新的文件路径
                destdir = os.path.join(path,'brain'+'/'+str(num)+'.nii')
                mycopyfile(filepath, destdir)
                print(destdir)
            elif filename == 'truth' and filetype == '.nii':
               # Newdir=os.path.join(foldpath,str(num)+ '.nii')#新的文件路径
              #  os.rename(Olddir, Newdir)
                destdir = os.path.join(path,'truth'+'/'+str(num)+'.nii')
                mycopyfile(filepath,destdir)
                print(destdir)
path = os.getcwd()
for i in range(1,19):
    if i <10 :
        stri = 'IBSR_0'+str(i)
        print(stri)
    else:
        stri = 'IBSR_'+str(i)
        print(stri)
    foldpath = os.path.join(path,stri)  #文件路径
    rename(i-1,foldpath,path)
