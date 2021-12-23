import numpy as np
import string
import pandas as pd
alphabet=string.ascii_uppercase


def plate1(well):
    #get new well letter
    for num,x in enumerate(alphabet):
        if well[0].upper()==x:
            letter=alphabet[num*2]
    #get new well number
    number=int(well[1:])*2-1
    newWell=str(letter)+str(number)
    return newWell

def plate2(well):
    #get new well letter
    for num,x in enumerate(alphabet):
        if well[0].upper()==x:
            letter=alphabet[num*2]
    #get new well number
    number=int(well[1:])*2
    newWell=str(letter)+str(number)
    return newWell

def plate3(well):
    #get new well letter
    for num,x in enumerate(alphabet):
        if well[0].upper()==x:
            letter=alphabet[num*2+1]
    #get new well number
    number=int(well[1:])*2-1
    newWell=str(letter)+str(number)
    return newWell
    
def plate4(well):
    #get new well letter
    for num,x in enumerate(alphabet):
        if well[0].upper()==x:
            letter=alphabet[num*2+1]
    #get new well number
    number=int(well[1:])*2
    newWell=str(letter)+str(number)
    return newWell

def get_number(newWell):
    #get overall well position as number 1-384
    for num,x in enumerate(alphabet):
        if newWell[0]==x:
            n384=(num)*24+int(newWell[1:])
    return int(n384)
            
def convert_file(plate_num,file):
    df=pd.read_excel(file)
    df=df[['Well Position','Scan 1']]
    df=df.dropna(how='all')

   

    if plate_num==1:
        df['Well Position']=df['Well Position'].apply(plate1)
    elif plate_num==2:
        df['Well Position']=df['Well Position'].apply(plate2)
    elif plate_num==3:
        df['Well Position']=df['Well Position'].apply(plate3)
    elif plate_num==4:
        df['Well Position']=df['Well Position'].apply(plate4)
        
    df['Well']=df['Well Position'].apply(get_number)
    df=df[['Well',"Well Position","Scan 1"]]
    df=df.rename(columns={"Scan 1":"Sample Name"})
    df1=df.copy()
    df2=df.copy()
    df3=df.copy()
    df1['Target Name']='IC'
    df2['Target Name']='RNaseP'
    df3['Target Name']='SARS'

    df1['Reporter']="TAMRA"
    df2['Reporter']="CY5"
    df3['Reporter']="FAM"

    df=pd.concat([df1,df2,df3])

    df['Task']="UNKNOWN"
    df['Quencher']="none"

    df.loc[df['Sample Name']==0, "Target Name"]=""
    df.loc[df['Sample Name']=="0", "Target Name"]=""

    df=df.loc[df['Well Position']!="O24"]
    df=df.loc[df['Well Position']!="P23"]
    df=df.loc[df['Well Position']!="P24"]
    df=df.loc[df['Well Position']!="O23"]

    df=df[["Well","Well Position","Sample Name","Target Name","Task","Reporter","Quencher"]]
    return df
