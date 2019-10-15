import subprocess
import os

org_apk_path = input("Enter original APK path: ")
if os.path.exists("decompiled"):
    print(os.system("RMDIR /Q/S decompiled "))

def signer():
    name = recompile()
    #jdk_version = input("Enter your java jdk verion (java --version)")
    subprocess.call('"C:\\Program Files\\Java\\jdk1.8.0_221\\bin\\jarsigner.exe" -keystore Gray_D.keystore -storepass 123456 '+name+' gray')
    #print("APK SIGNED!!"+name)
    subprocess.call("zipalign.exe -c 4 "+name)
    print("Apk Aligned!!")

def recompile():
    name = input("Enter name for youR new apk\n")
    print("Creating an Brand new apk for YOu..")
    subprocess.call("java -jar apk.jar b decompiled -o "+name,stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=subprocess.PIPE, stderr=subprocess.PIPE is used to hide output of command
    return name

def search():
    print("Hey Tie uP YouR belts Application is decompling...")
    subprocess.call("java -jar apk.jar d  -s "+org_apk_path+" -o decompiled",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Application is decompiled!")
    print("\n Doing the MaGIC!!!")
    f = open("decompiled/AndroidManifest.xml")
    f_content = f.read()
    if ('android:debuggable="true"' in f_content):
        print("NOOOOO!!!  Application is already debuggable")
        exit()
    f_content=f_content.replace('<application', '<application android:debuggable="true"')
    f = open("decompiled/AndroidManifest.xml", "w")
    f.writelines(f_content)
    print("Magic Completed@@@")
    #print(f)

def main():
    search()
    signer()
    #modifier()
    #recompile()

main()



#'C:\Users\Naman\Desktop\DEMO\debug\InsecureBankv2.apk'
#"C:\Program Files\Java\jdk1.8.0_221\bin\jarsigner.exe" -keystore Gray_D.keystore -storepass 123456 tl.apk gray
