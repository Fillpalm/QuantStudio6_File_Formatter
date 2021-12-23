import pandas as pd

def convert_file(file):
    df=pd.read_excel(file)
    df=df[['Well Position','Scan 1']]
    df=df.dropna(how='all')
    df=df.loc[df['Well Position']!="H11"]
    df=df.loc[df['Well Position']!="H12"]



    df['Well']=df.index+1   #df['Well Position'].apply(get_number)
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

    df=df[["Well","Well Position","Sample Name","Target Name","Task","Reporter","Quencher"]]

    return df
