#update time : 20200819   直接从迈普的分析结果进行分析，不需要人为再去生成excel。
#update time : 20200820   修改生成的图片名称。  
#update time : 20201215   更新sanger结果生成后，储存的路径。
#update time : 20210111   生成W231_NY200729655811_张黄安 类似的文件夹，将分析结果放到对应的目录里。

import os
import sys
import glob
import time
import shutil
import zipfile
import pandas as pd
from Sanger import bio_function
from pathlib import Path
try:
    import xlrd
except Exception as import_error:
    os.system('pip install xlrd')
    import xlrd
try:
    import pandas
except Exception as import_error:
    os.system('pip install pandas')
    import pandas as pd
try:
    import pymysql
except Exception as import_error:
    os.system('pip install pymysql')
    import pymysql


defaultPath = "/share_data/wujm/project/Django/Project/uploadSanger"
allResultPath = "/share_data/wujm/project/Django/Project/uploadSanger/sangerResult/"  #该目录下存放样本名

class Mysql:
    def __init__(self, sql_user='NA', sql_pswd='NA'):
        self.user = 'wujm' if sql_user == 'NA' else sql_user
        self.pswd = 'wjM123456++' if sql_pswd == 'NA' else sql_pswd

    def connect(self, sql_db='clinepilepsy_pipeline'):
        try:
            sql_con = pymysql.connect(host='192.168.99.7', user=self.user, passwd=self.pswd, db=sql_db)
        except Exception as connect_error:
            print('连接数据库-%s错误！' % sql_db)
            print(connect_error)
            sys.exit()
        return sql_con

    # 创建游标
    def cursor(self, sql_con):
        sql_cur = sql_con.cursor()
        return sql_cur

    # 获取
    def run_cmd(self, sql_cur, sql_cmd):
        try:
            sql_cur.execute(sql_cmd)
        except Exception as run_error:
            print('运行sql命令问题:\n%s' % sql_cmd)
            print(run_error)
            sys.exit()

def searchMySQL():
    #判断Sanger_sangerzipfiles表中的analysisStatus状态是否为1，如果为1，表示未分析，需要进行run(FILE)分析； 如果是0 ，表示已分析，pass。
    my_obj = Mysql()
    my_con = my_obj.connect()
    my_cur = my_obj.cursor(my_con)
    no_ana_cmd = "select id, fileName from Sanger_sangerzipfiles where analysisStatus = 1"
    my_obj.run_cmd(my_cur, no_ana_cmd)
    info = my_cur.fetchall()
    if len(info) == 0:
        pass
    else:
        for index in range(len(info)):
            no_ana_id = info[index][0]
            no_ana_filename = info[index][1]
            run(no_ana_id, no_ana_filename)
            #运行完成之后，更新analysisStatus为0
            update_cmd = "update Sanger_sangerzipfiles set analysisStatus = 0 where id={};".format(no_ana_id)
            my_obj.run_cmd(my_cur, update_cmd)
            my_con.commit()
    my_con.close() 


def get_dict():
  sampleDict = {}# 从200例之后开始
  sql_con = pymysql.connect(host='192.168.99.7', user='wujm', passwd='wjM123456++', db='clinepilepsy_pipeline')
  sql_cur = sql_con.cursor()
  cmd = "select type_id, user_name, sample_name, kinsfolk_sample from PM_pm;"
  sql_cur.execute(cmd)
  infos = sql_cur.fetchall() 
  ##先判断有没有亲属送样
  for each in infos[100:]:
    if each[-1] == None or each[-1] == "Empty":
      sampleDict[each[2]] = each[0]+'_'+each[1]+'_'+each[2]
    else:
      sampleDict[each[2]] = each[0]+'_'+each[1]+'_'+each[2]
      for jias in each[-1].split(','):
        jias = jias.strip().split(':')
        sampleDict[jias[1]] = each[0]+'_'+each[1]+'_'+each[2]
  
  return sampleDict

def run(ID, FILE):
    '''
    输入为一个压缩文件，以zip结尾
    输出结果更新到Sanger_sangersamples数据库。
    数据库格式：id, sampleName chrom pos  genoType abiUrl abiJpgUrl created_time update_time
    '''
    print("开始分析---")
    sampleDict = get_dict()
    fileAbosultePath = defaultPath + '/' + FILE
    os.chdir(defaultPath)   #切换上传文件所在目录里面
    timePath = time.strftime("%Y%m%d%H", time.localtime())
    if not os.path.exists(timePath):
        os.mkdir(timePath);#生成日期目录，
    else:
        pass
    os.chdir(timePath) 
    newPath = defaultPath +'/'+timePath
    
    if FILE.endswith('.zip'):   #如果是压缩文件，先复制文件，在newPath解压缩，newPath即为ab1存放目录以及新生层的文件的存放目录
        shutil.copyfile(fileAbosultePath,FILE)
        os.system("unzip -o -q %s" % FILE)

    else: 
        #其他则认为是非压缩文件，直接移动Excel和ab1文件至newPath
        shutil.move(fileAbosultePath,FILE)

    resultList = []
    for eachFile in Path(newPath).iterdir():
        if eachFile.is_file():
            if eachFile.suffix == '.xlsx' or eachFile.suffix == '.xls':
                xls_data = xlrd.open_workbook(eachFile)
                sheetName = xls_data.sheet_names() #暂考虑只有一张Sheet1
                data = pd.read_excel(eachFile,sheet_name = sheetName[0],index_col = None,na_values= ['9999'])
                #data['sampleId'] = data['姓名']
                #data['chrom'] = data['检测位点'].str.split(":",0).str[0]
                #data['pos'] = data['检测位点'].str.split(":",0).str[1]
                #data['pos'].replace('[A-Z]|>','',regex=True,inplace=True)
                #data['geneType'] = data['突变类型']
                #data['ab1Name'] = data['峰图文件']
                data['sampleId'] = data['样本名']
                data['chrom'] = data['检测区域'].str.split(":",0).str[0]
                data['pos'] = data['检测区域'].str.split(":",0).str[1]
                data['pos'].replace('[A-Z]|>','',regex=True,inplace=True)
                data['geneType'] = data['突变类型']
                data['ab1Name'] = data['峰图文件']
                data['gene'] = data['检测位点']
                data['fangx'] = data['测序方向']
                sampleInfos = data[["sampleId","chrom","pos","geneType","ab1Name","gene","fangx"]]
                for index, row in sampleInfos.iterrows():
                    #print("\t".join(str(i) for i in row))
                    sampleId = row['sampleId']
                    chromId = row['chrom'].replace("chr","")
                    posId = row['pos']
                    if row['fangx'] == "正向":
                        fangx = "F"
                    else:
                        fangx = "R"
                    #rsNumber = row['SNP'].upper()
                    upStart = int(posId) - 30
                    upEnd = int(posId) - 1
                    downStart = int(posId) + 1
                    downEnd = int(posId) + 30
                    #获取snp位点前后30bp碱基序列
                    upSeq = bio_function.extract_fa(str(chromId),str(upStart),str(upEnd)).upper()
                    downSeq = bio_function.extract_fa(str(chromId),str(downStart),str(downEnd)).upper()
                    sampleAb1 = row['ab1Name']
                    #运行程序
                    #将ab1文件名前缀作为图片的name
                    #rawName = os.path.splitext(sampleAb1)[0].split("-")
                    pngName = sampleId + '_' + row['gene'] + '_' + fangx + '.png'
                    #定位sample_id 对应的ab1文件
                    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
                    print(sampleAb1)
                    print(pngName)
                    print(upSeq)
                    print(downSeq)
                    print(sampleDict[sampleId])
                    print("----------------------------------")
                    os.system("Rscript /share_data/wujm/Config/script/clinepilepsy/plot_by_sangerseqR-copy.R %s %s %s %s" % (sampleAb1,pngName,upSeq,downSeq))

                    #程序运行结束之后，将sampleId相关的文件全放到同一个sampleId目录下
                    sampleIdPath = allResultPath + sampleDict[sampleId]
                    if not os.path.exists(sampleIdPath):
                        os.mkdir(sampleIdPath);#生成日期目录，
                    else:
                        pass
                    #模糊匹配
                    localSampleList = glob.glob('*%s*[ab1,png]' % sampleId)
                    for i in localSampleList:
                        os.system("cp %s %s" % (i, sampleIdPath))

                    ab1AboPath = allResultPath+sampleDict[sampleId]+'/'+sampleAb1
                    newPngAboPath = allResultPath+sampleDict[sampleId]+'/'+pngName
                    resultList.append(str(sampleId)+','+chromId+','+str(posId)+','+row['geneType']+','+ab1AboPath+','+newPngAboPath)
                    

                    

            else:
                pass
    #进行数据库更新
    updateSangersamples(resultList)



def updateSangersamples(List):
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    my_obj = Mysql()
    my_con = my_obj.connect()
    my_cur = my_obj.cursor(my_con)
    no_ana_cmd = "select sampleName, chrom, pos, genoType from Sanger_sangersamples;"
    my_obj.run_cmd(my_cur, no_ana_cmd)
    allSampleNames = my_cur.fetchall()
    for each in List:
        sampleName, chrom, pos, GT, ab1File, ab1Png = each.split(',')
        #判断sampleName，chrom, pos，GT是否存在，如果存在，更新
        if (sampleName, chrom, int(pos), GT) in allSampleNames:
            #update
            update_cmd = "update Sanger_sangersamples set abiFileUrl='{abiFile}', abiPngUrl='{abiPng}', update_time='{updateTime}'  where sampleName='{name}' and chrom='{chr}' and pos={pos} and genoType='{gt}';".format(abiFile=ab1File,abiPng=ab1Png,updateTime=nowTime, name=sampleName, chr=chrom, pos=pos, gt=GT)
            my_obj.run_cmd(my_cur, update_cmd)
            my_con.commit()
        else:
            #insert
            insert_cmd = "insert into Sanger_sangersamples (sampleName, chrom, pos, genoType, abiFileUrl, abiPngUrl, created_time, update_time) values ('{sample}','{chr}',{pos},'{gt}','{abiFile}','{abiPng}','{createTime}','{updateTime}');".format(sample=sampleName,chr=chrom,pos=pos,gt=GT,abiFile=ab1File,abiPng=ab1Png,createTime=nowTime, updateTime=nowTime)
            my_obj.run_cmd(my_cur, insert_cmd)
            my_con.commit()
    my_con.close()
