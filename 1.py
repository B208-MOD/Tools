import os
import shutil
import zipfile
import re
import xml.etree.ElementTree as ET
import sys
from xml.dom import minidom
import getopt
import pyzstd
from colorama import init, Fore, Style
import hashlib
import struct
import time
from halo import Halo
from rich.console import Console
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn



from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from colorama import init, Fore, Style
import time
import sys

# Khởi tạo colorama
init(autoreset=True)
console = Console()

# Định nghĩa banner mới
banner = f"""
╔════════════════════════════════════════════════════════════════╗
║       {Style.BRIGHT}{Fore.GREEN}██╗    ██╗██╗  ██╗ █████╗ ██████╗  █████╗ ███╗   ██╗   {Style.RESET_ALL}  ║
║       {Style.BRIGHT}{Fore.YELLOW}██║    ██║██║  ██║██╔══██╗██╔══██╗██╔══██╗████╗  ██║   {Style.RESET_ALL}  ║
║       {Style.BRIGHT}{Fore.RED}██║ █╗ ██║███████║███████║██║  ██║███████║██╔██╗ ██║   {Style.RESET_ALL}  ║
║       {Style.BRIGHT}{Fore.MAGENTA}██║███╗██║██╔══██║██╔══██║██║  ██║██╔══██║██║╚██╗██║  {Style.RESET_ALL}   ║
║       {Style.BRIGHT}{Fore.BLUE}╚═╝╚══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═╝   {Style.RESET_ALL}     ║
╠════════════════════════════════════════════════════════════════╣
║            {Style.BRIGHT}{Fore.YELLOW}TOOL MOD SKIN AOV - B208MOD                    {Style.RESET_ALL}     ║
║            {Style.BRIGHT}{Fore.GREEN}DỰ ÁN PHÁT TRIỂN BỞI LQB AND B208                {Style.RESET_ALL}   ║
╠════════════════════════════════════════════════════════════════╣
║ {Style.BRIGHT}{Fore.CYAN}👉 Liên hệ hỗ trợ qua Zalo:                          {Style.RESET_ALL}          ║
║ {Style.BRIGHT}{Fore.RED}👉 Zalo: 0389655646                                          {Style.RESET_ALL}  ║
╚════════════════════════════════════════════════════════════════╝
"""


for line in banner.splitlines():
    sys.stdout.write(line + "\n")
    sys.stdout.flush()
    time.sleep(0.005)
console.print("ĐỢI XÍU ĐANG LẤY DỮ LIỆU...", style="bold green")




with open('FILES_CODE/ZSTD_DICT.xml', 'rb') as f:
    ZSTD_DICT = f.read()

ZSTD_LEVEL = 17


version = '1.56.1'


copy_tasks = [
    ('EX/Databin', f'FILES_MOD/files/Resources/{version}/Databin/Client'),
    ('EX/AGES/commonresource', f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/commonresource'),
    ('EX/AGES/KeySpell', f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/KeySpell'),
    ('EX/AGES/mowen', f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/mowen'),
    ('EX/AGES/PassiveResource', f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/PassiveResource'),
    ('EX/AGES/Ultrafire', f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/Ultrafire')
]


HeroSkin = f"FILES_MOD/files/Resources/{version}/Databin/Client/Actor/heroSkin.bytes"
HeroSkinShop = f"FILES_MOD/files/Resources/{version}/Databin/Client/Shop/HeroSkinShop.bytes"
OganSkin = f"FILES_MOD/files/Resources/{version}/Databin/Client/Actor/organSkin.bytes"
Sound_Files = f"FILES_MOD/files/Resources/{version}/Databin/Client/Sound"
ktr_Sound = f"FILES_MOD/files/Resources/{version}/Databin/Client/Sound/BattleBank.bytes"
file_mod_Modtion = f"FILES_MOD/files/Resources/{version}/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes"
file_mod_skill1 = f"FILES_MOD/files/Resources/{version}/Databin/Client/Skill/liteBulletCfg.bytes"
file_mod_skill2 = f"FILES_MOD/files/Resources/{version}/Databin/Client/Skill/skillmark.bytes"
file_mod_Character = f"FILES_MOD/files/Resources/{version}/Databin/Client/Character/ResCharacterComponent.bytes"
source_path = 'EX/INFO/Prefab_Hero'
file_map = 'EX/kb.txt'
Back = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/commonresource/Back.xml'
hasteE1 = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/commonresource/HasteE1.xml'
HasteE1_leave = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/commonresource/HasteE1_leave.xml'
Dance = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/commonresource/Dance.xml'
Blu15010 = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/PassiveResource/BlueBuff.xml'
Blu15013 = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/PassiveResource/BlueBuff_CD.xml'
Red15010 = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/PassiveResource/RedBuff_Slow.xml'
junglemark_path = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD/PassiveResource/junglemark.xml'
HeadID = f"FILES_MOD/files/Resources/{version}/Databin/Client/Global/HeadID.bytes"
HeadImage = f"FILES_MOD/files/Resources/{version}/Databin/Client/Global/HeadImage.bytes"
Huanhua = f"FILES_MOD/files/Resources/{version}/Databin/Client/Huanhua/ResSkinExclusiveBattleEffectCfg.bytes"
RSBBC = f"FILES_MOD/files/Resources/{version}/Databin/Client/Huanhua/ResKillBillboardCfg.bytes"



os.makedirs(f"FILES_MOD/files/Resources/{version}/AssetRefs/Hero/", exist_ok=True)


with Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.description]{task.description}"), refresh_per_second=10) as progress:
    total_tasks = len(copy_tasks)
    task = progress.add_task("Đang sao chép tệp...", total=total_tasks)

    for src, dst in copy_tasks:
        shutil.copytree(src, dst, dirs_exist_ok=True)
        progress.update(task, advance=1)  # Cập nhật tiến độ


console.print(f" Dữ Liệu Đã Sẵn Sàng Vui Lòng Nhập Lựa Chọn Để MOD !")
#========================================ICON=================================


def modheroskin(ID_SKIN, HeroSkin):
    Files = HeroSkin
    skinId = ''
    heroId = ''
    skinNumber = ''
    icon = ''
    code_skin_mod = ''
    with open(HeroSkin, 'r',  encoding="utf-8") as file:
        ALL_CODE_GOC = file.read()
        STAR_END = re.compile(r'<Track skinId=".*?</Track>', re.DOTALL)
        DOAN_CODE = STAR_END.findall(ALL_CODE_GOC)
    for code in DOAN_CODE:
        if code_skin_mod != '':
            continue
        if f'<Track skinId="{ID_SKIN}' in code:
            if ID_SKIN == '16707':
                code = code.replace('301677', '301677_2').replace('16707.jpg', '16707_2.jpg').replace('BG_Commons_01/BG_Commons_01_Platform', 'BG_wukongjuexing2/BG_wukongjuexing2_Platform')
            if ID_SKIN == '13311':
                code = code.replace('3013311', '3013311_2').replace('13311.jpg', '13311_2.jpg').replace('BG_Commons_01/BG_Commons_01_Platform', 'BG_direnjie_13312_T3/BG_yinyingzhishou_01_platform').replace('3013311_2head', '3013311head_2')
            
            code_skin_mod = code
            A = code.split('\n')
            B = A[0].split()
            skinId = B[1]
            heroId = B[2]
            skinNumber = B[3]
            icon = B[4]
            
    if code_skin_mod != '':
        for code in DOAN_CODE:
            if f'<Track skinId="{ID_SKIN[:3]}' in code:
                skin_phu = code
                C = skin_phu.split('\n')
                D = C[0].split()
                
                skin_phu_1 = code_skin_mod.replace(skinId,D[1]).replace(heroId,D[2]).replace(skinNumber,D[3])
                if (D[1])[11:-1] == '00':
                    skinNumber_MD = D[3]
                if skinNumber in code:
                    skin_phu_1 = skin_phu_1.replace(skinNumber, skinNumber_MD)
                if (D[1])[11:-1] == '00':
                    skin_phu_1 = skin_phu_1.replace(icon, D[4]).replace(skinNumber_MD, skinNumber)


                    

                    if ID_SKIN == '15412':
                        skin_phu_1 = skin_phu_1.replace('3015412_B43_1', '3015412')
                        

                with open(HeroSkin, 'r',  encoding="utf-8") as file:
                    ALL_CODE_GOC = file.read().replace(skin_phu, skin_phu_1)
                with open(HeroSkin, 'w') as f:
                    f.write(ALL_CODE_GOC)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.GREEN + "Đã Mod HeroSkin.bytes !", Style.BRIGHT + Fore.CYAN + ' Done!')
    else:
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.GREEN + "Chưa Mod HeroSkin.bytes !", Style.BRIGHT + Fore.RED + ' Skin Not Found!')
    dieukienmod = code_skin_mod.encode()
    return dieukienmod
def modheroskinshop(ID_SKIN, HeroSkinShop):
    SkinId = ''
    HeroId = ''
    SkinNumber = ''
    codeskinmod = ''
    with open (HeroSkinShop, 'r') as f:
        allcode = f.read()
        ds_code = allcode.split('<Track')
    for code in ds_code:
        if codeskinmod != '':
            continue
        if f'SkinId="{ID_SKIN}"' in code:
            if ID_SKIN == '16707':
                code = code.replace('Awake_Label_1.png', 'Awake_Label_5.png')
            if ID_SKIN == '13311':
                code = code.replace('13311.png', 'Awake_Label_5.png')
            codeskinmod = code
            A = code.split('\n')
            SkinId = A[1]
            HeroId = A[2]
            SkinNumber =A[3]
    if codeskinmod != '':
        for code in ds_code:
            if f'SkinId="{ID_SKIN[:3]}' in code:
                code_skin_phu = code
                B = code.split('\n')
                code_skin_phu1 = codeskinmod.replace( SkinId,B[1]).replace( HeroId,B[2]).replace(SkinNumber,B[3])
                with open (HeroSkinShop, 'r') as f:
                    code1 = f.read().replace(code_skin_phu, code_skin_phu1)
                with open (HeroSkinShop, 'w') as f:
                    f.write(code1)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + "Đã Mod HeroSkinShop.bytes !", Style.BRIGHT + Fore.CYAN + ' Done!')
    else:
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + "Chưa Mod HeroSkinShop.bytes !", Style.BRIGHT + Fore.RED + ' Skin Not Found!')
    return


def habua15010(Blu15010, Red15010):

    DS_FILES = [Blu15010, Red15010]
    for files in DS_FILES:
        with open (files, 'rb') as f:
            code = f.read().replace(b"CheckSkinIdVirtualTick", b"CheckHeroIdTick").replace(b'"skinId" value="15009"', b'"heroId" value="150"')
        with open (files, 'wb') as f:
            f.write(code)

def sound_databin(ID_MOD_SKIN_NEW, Sound_Files):
    skin_id_input = ID_MOD_SKIN_NEW
    sound_directory = Sound_Files
    sound_files = os.listdir(sound_directory)

    all_skin_ids = []
    for i in range(21):
        if i < 10:
            i = "0" + str(i)
        all_skin_ids.append(b"\x00" + int(skin_id_input[0:3] + str(i)).to_bytes(4, byteorder="little"))

    initial_skin_id = all_skin_ids[0]
    selected_skin_id = all_skin_ids[int(skin_id_input[3:])]

    all_skin_ids.remove(selected_skin_id)
    all_skin_ids.remove(initial_skin_id)

    for file in sound_files:
        with open(os.path.join(sound_directory, file), "rb") as sound_file:
            sound_data = sound_file.read()

        if skin_id_input == "13311":
            if file == 'BattleBank.bytes':
                sound_data = sound_data.replace(b'\x9dO\x14', b'\xff3\x00').replace(b'\x9eO\x14', b'\xff3\x00').replace(b'\x9fO\x14', b'\xff3\x00').replace(b'\xa0O\x14', b'\xff3\x00')
            if file == 'ChatSound.bytes':
                sound_data = sound_data.replace(b'\x9fO\x14', b'\xff3\x00')
            if file == 'HeroSound.bytes':
                sound_data = sound_data.replace(b'\x9fO\x14', b'\xff3\x00').replace(b'\xa0O\x14', b'\xff3\x00')
            if file == 'LobbyBank.bytes':
                sound_data = sound_data.replace(b'\xa0O\x14', b'\xff3\x00')
            if file == 'LobbySound.bytes':
                sound_data = sound_data.replace(b'\xa0O\x14', b'\xff3\x00')

        if skin_id_input == "16707":
            if file == 'BattleBank.bytes':
                sound_data = sound_data.replace(b'/~\x19', b'CA\x00').replace(b'0~\x19', b'CA\x00').replace(b'1~\x19', b'CA\x00')
            if file == 'ChatSound.bytes':
                sound_data = sound_data.replace(b'0~\x19', b'CA\x00')
            if file == 'HeroSound.bytes':
                sound_data = sound_data.replace(b'0~\x19', b'CA\x00').replace(b'1~\x19', b'CA\x00')
            if file == 'LobbyBank.bytes':
                sound_data = sound_data.replace(b'0~\x19', b'CA\x00')
            if file == 'LobbySound.bytes':
                sound_data = sound_data.replace(b'0~\x19', b'CA\x00')

        if file != "CoupleSound.bytes":
            for skin_id in all_skin_ids:
                skin_id += b"\x00" * 8
                sound_data = sound_data.replace(skin_id, b"\x0000" + b"\x00" * 10)
        else:
            for skin_id in all_skin_ids:
                skin_id += b"\x02\x00\x00\x00\x01"
                sound_data = sound_data.replace(skin_id, b"\x0000\x00\x00\x02\x00\x00\x00\x01")

        if sound_data.find(selected_skin_id) != -1:
            if file != "CoupleSound.bytes":
                sound_data = sound_data.replace(initial_skin_id + b"\x00" * 8, b"\x0000" + b"\x00" * 10)
                sound_data = sound_data.replace(selected_skin_id + b"\x00" * 8, initial_skin_id + b"\x00" * 8)
            else:
                sound_data = sound_data.replace(initial_skin_id + b"\x02\x00\x00\x00\x01", b"\x0000\x00\x00\x02\x00\x00\x00\x01")
                sound_data = sound_data.replace(selected_skin_id + b"\x02\x00\x00\x00\01", initial_skin_id + b"\x02\x00\x00\x00\x01")

        with open(os.path.join(sound_directory, file), "wb") as sound_file:
            sound_file.write(sound_data)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.BLUE + file, Style.BRIGHT + Fore.GREEN + ' Done!')
    return

def montion(ID_MOD_SKIN_NEW, file_mod_Modtion):
    ID=ID_MOD_SKIN_NEW
    AllID=[]
    for i in range(21):
        if i<10: AllID.append(ID[0:3]+"0"+str(i))
        else: AllID.append(ID[0:3]+str(i))
    All_S=[]
    for i in AllID:
        i=hex(int(i))[2:]
        All_S.append(bytes.fromhex(f"{i[2:4]}{i[0:2]}0000"))
    with open(file_mod_Modtion,"rb") as f:
        begin=f.read(140)
        All_Code=[]
        while True:
            SL=f.read(2)
            if SL==b"": 
                f.close()
                break
            SL0=SL[0]+SL[1]*256+2
            Code=SL+f.read(SL0)
            if All_S[AllID.index(ID)] in Code: All_Code.append(Code)
            elif All_S[0] in Code: All_Code.append(Code)
    CodeDB=[]
    CodeMD=[]
    CodeMD2=[]
    for code in All_Code:
        if code[0:2] in b"6\x00S\x00": CodeDB.append(code)
        else:
            CodeMD.append(code)
            CodeMD2.append(code)
    aw=0
    if len(CodeDB)>1:
        print(Style.BRIGHT + Fore.BLUE +f'==========> [Input Motion {len(CodeDB)}] <==========')
        aw = 1#int(input(Style.BRIGHT + Fore.CYAN + '[•]'+Style.BRIGHT + Fore.GREEN + 'INPUT: ' + Style.BRIGHT + Fore.BLUE))

        aw= aw-1
    if len(CodeDB)>0:
        CodeR=CodeDB[aw]
        idmod=CodeR[21:25]
        for code in CodeMD:
            vtf=CodeMD.index(code)
            for id in All_S:
                vt=code.find(id)
                if vt!=-1:
                    codet=code[vt+4:vt+8]
                    code=code.replace(codet,idmod,1)
                else: break
            CodeMD[vtf]=code
    else:
        for code in CodeMD:
            vtr=CodeMD.index(code)
            vt=code.find(All_S[AllID.index(ID)])
            idmod=code[vt+4:vt+8]
            for id in All_S:
                vt=code.find(id)
                if vt!=-1:
                    codet=code[vt+4:vt+8]
                    code=code.replace(codet,idmod,1)
                else: break
            CodeMD[vtr]=code
    with open(file_mod_Modtion,"rb") as f:
        y=f.read()
        f.close()
    for i in range(len(CodeMD)): y=y.replace(CodeMD2[i],CodeMD[i],1)
    if len(CodeMD)+len(CodeDB)==0:
        for id in All_S: y=y.replace(id,b"00\x00\x00",1)
    with open(file_mod_Modtion,"wb") as f: f.write(y)
    return


def liteBulletCfg(ID_SKIN, file_mod_skill1):
    if ID_SKIN == '13311':
        with open(file_mod_skill1, 'rb') as f:
            code = f.read().replace(b'prefab_skill_effects/hero_skill_effects/133_direnjie/', b'prefab_skill_effects/component_effects/13311/13311_5/')
        with open(file_mod_skill1, 'wb') as f:
            f.write(code)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.MAGENTA + file_mod_skill1, Style.BRIGHT + Fore.GREEN + ' Done!')
    else:
        with open(file_mod_skill1, "rb") as f:
            dl = f.read()
        with open(file_mod_skill1, "rb") as f:
            Header = f.read(140)
            F = [Header]
            for i in range(int.from_bytes(Header[12:16], "little")):
                _ = f.read(4)
                Code = _ + f.read(int.from_bytes(_, "little"))
                kb = Code[9:13]
                C1, C2 = 13+int.from_bytes(kb, "little") + \
                    41, 13+int.from_bytes(kb, "little")+45
                kb = Code[C1:C2]
                X = Code[C2:C2+int.from_bytes(kb, "little")][:-1].decode()
                if f"hero_skill_effects/{str(ID_SKIN)[:3]}" in X:
                    X = (X[:X.find("/", 41)]+"/"+str(ID_SKIN) +
                            X[X.find("/", 41):]).encode()+b"\x00"
                    Code = Code[4:C2-4]+(len(X).to_bytes(4, 'little')) + \
                        X+Code[C2+int.from_bytes(kb, "little"):]
                    Code = len(Code).to_bytes(4, "little")+Code
                F.append(Code)
        dln = b"".join(F)
        if dln == dl:
            print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.MAGENTA + "liteBulletCfg.bytes Chưa Được Mod !", Style.BRIGHT + Fore.RED + ' ID Not Found!')
            return 
        with open(file_mod_skill1, "wb") as f:
            f.write(dln)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.MAGENTA + "liteBulletCfg.bytes Đã Được Mod !", Style.BRIGHT + Fore.GREEN + ' Done!')

    return


def skillmark(ID_SKIN, file_mod_skill2):
    with open(file_mod_skill2, "rb") as f:
        dl = f.read()
    with open(file_mod_skill2, "rb") as f:
        Header = f.read(140)
        F = [Header]
        pos = 140
        for i in range(int.from_bytes(Header[12:16], "little")):
            _ = f.read(4)
            pos0 = f.tell() - 4
            Code = f.read(int.from_bytes(_, "little"))
            pos += int.from_bytes(_, "little") + 4
            f.seek(-(int.from_bytes(_, "little")) + 8, 1)
            f.read(int.from_bytes(f.read(4), 'little'))
            f.read(int.from_bytes(f.read(4), 'little'))
            f.read(int.from_bytes(f.read(4), 'little'))
            f.read(42)
            constant = 0
            while True:
                pos1 = f.tell() - pos0 + constant
                _ = f.read(4)
                X = f.read(int.from_bytes(_, 'little'))[:-1].decode()
                if f"hero_skill_effects/{str(ID_SKIN)[:3]}" in X:
                    X = (X[:X.find("/", 41)] + "/" + str(ID_SKIN) +
                            X[X.find("/", 41):]).encode() + b"\x00"
                    constant += len(str(ID_SKIN))+1
                    Code = Code[:pos1-4] + len(X).to_bytes(
                        4, 'little') + X + Code[pos1 + int.from_bytes(_, "little"):]
                else:
                    Code = len(Code).to_bytes(4, "little") + Code
                    break
            f.seek(pos - f.tell(), 1)
            F.append(Code)
        dln = b"".join(F)
        if dln == dl:
            print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.MAGENTA + "Skillmark.bytes Chưa Được Mod !", Style.BRIGHT + Fore.RED + ' ID Not Found!')
            return 
        with open(file_mod_skill2, "wb") as f:
            f.write(dln)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.MAGENTA + "Skillmark.bytes Đã Được Mod !", Style.BRIGHT + Fore.GREEN + ' Done!')

        return
        

def modhieuung(ID_SKIN,destination_path,NAME_HERO, modsoundages):
    DS_FILES_MOD_CHECK = []
    DS_FILES_MOD_SOUND = []
    DS_FILES_MOD_EFFECT = []

    ID_SKIN = ID_SKIN.encode()
    BY_FILES = b'CreditB208MOD'
    CODE_ID = b'<int name="skinId" value="'
    CODE_SOUND = b'        <String name="eventName" value="'

    if ID_SKIN.decode()[3] == '0':
        IDSOUND1 = ID_SKIN.decode()[4]
    else:
        IDSOUND1 = ID_SKIN.decode()[-2:]
    IDSOUND = b"_Skin" + IDSOUND1.encode()
    THU_MUC_SKILL =destination_path+'/'+NAME_HERO+'/Skill'
    FILES_XML = [file for file in os.listdir(THU_MUC_SKILL) if file.endswith('.xml')]
    if ID_SKIN == b'13210':
        with open ('FILES_CODE/13210/Dance.xml', 'rb') as f:
            fixdance13210 = f.read()
        with open (Dance, 'rb') as f:
            mod_dance_13210 = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', fixdance13210)
        with open(Dance,'wb') as f:
            f.write(mod_dance_13210)
    for filesxml in FILES_XML:
        filesxml1 = filesxml
        filesxml = THU_MUC_SKILL+'/'+ filesxml
        try:
            with open (filesxml, 'rb') as f:
                ALL_CODE_GOC = f.read()
                ALL_DOAN_CODE = ALL_CODE_GOC.split(b'    <Track trackName="')
        except UnicodeDecodeError as e:
            continue

            

        #------------------------------HIEU_UNG------------------------------#
        if ID_SKIN not in [b'13311', b'16707']:
            with open(filesxml, 'rb') as file:
                text = file.read()
            if b'prefab_skill_effects/hero_skill_effects/' in text.lower():
                if filesxml not in DS_FILES_MOD_EFFECT:
                    DS_FILES_MOD_EFFECT.append(filesxml1)

            text = re.sub(re.escape(b"prefab_skill_effects/hero_skill_effects/" + NAME_HERO.encode() + b'/'), b"prefab_skill_effects/hero_skill_effects/" + NAME_HERO.encode() + b'/' + ID_SKIN + b'/', text, flags=re.IGNORECASE)
            text = re.sub(re.escape(b'/'+ID_SKIN+b'/'+ID_SKIN+b'/'), b'/'+ID_SKIN+b'/', text, flags=re.IGNORECASE)
            text = re.sub(re.escape(b'<bool name="bAllowEmptyEffect" value="true" refParamName="" useRefParam="false" />'), b'<bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false" />', text, flags=re.IGNORECASE)
            with open(filesxml, 'wb') as file:
                file.write(text)

        if ID_SKIN[:3] == b'524' and filesxml1 == 'A1E9.xml':
            with open(filesxml, 'rb') as f:
                content = f.read()
            content = content.replace(b'prefab_skill_effects/hero_skill_effects/524_Capheny/' + ID_SKIN + b'/Atk1_FireRange', b'prefab_skill_effects/hero_skill_effects/524_Capheny/Atk1_FireRange')
            with open(filesxml, 'wb') as f:
                f.write(content)
        elif ID_SKIN == b'15015' and filesxml1 == 'U1.xml':
            cdto63 = b'<Condition id="63" guid="e89a739d-ad18-433f-83c7-ed477652dd8f" status="true" />'
            cdto28 = b'<Condition id="28" guid="c0b9dcbe-c83f-4a57-b203-70a202308416" status="true" />'
            cdto66 = b'<Condition id="66" guid="bf4a4330-412d-4b5e-9a2f-723ba76bdffb" status="true" />'
            cdio39 = b'<Condition id="39" guid="6e38b810-2c03-4c25-9331-fd09a03cb2e2" status="true" />'
            with open(filesxml, 'rb') as f:
                content = f.read().replace(cdto63, cdto28).replace(cdto66, cdio39)
            with open(filesxml, 'wb') as f:
                f.write(content)
        elif ID_SKIN == b'15412' and filesxml1 == 'P12E2.xml':
            with open(filesxml, 'rb') as f:
                rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/15413_HuaMuLan_Red', b'prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15413_HuaMuLan_Red')
            with open(filesxml, 'wb') as f:
                f.write(rpl)
        elif ID_SKIN == b'13015' and filesxml1 == 'A4.xml':
            with open(filesxml, 'rb') as f:
                rpl = f.read().replace(b'guid="0f548d1f-5ab9-4497-b629-5b022c25701d" enabled="true"', b'guid="0f548d1f-5ab9-4497-b629-5b022c25701d" enabled="false"')
            with open(filesxml, 'wb') as f:
                f.write(rpl)
        elif ID_SKIN == '17106':
            if filesxml1 == 'P1E5.xml':
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/171_zhangfei/17106/1719_zhangfei', b'prefab_skill_effects/hero_skill_effects/171_zhangfei/1719_zhangfei')                            
                with open(filesxml, 'wb') as f:
                    f.write(rpl)
        elif ID_SKIN == b'14111' and filesxml1 == 'S1.xml':
            DS_14111 =[]
            with open('FILES_CODE/14111.xml', 'rb') as f:
                code_fix = f.read()
            with open(filesxml, 'rb') as f:
                code_fix2 = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', code_fix)
            with open(filesxml, 'wb') as f:
                f.write(code_fix2)
            with open(filesxml, 'rb') as f:
                code_fix2 = f.readlines()
            for trackcd in code_fix2:
                if b'<Track trackName="' in trackcd:
                    DS_14111.append(trackcd)
            for i in range (len(DS_14111)):
                if b'"CheckHeroIdTick" guid="CreditB208MOD_1"' in DS_14111[i]:
                    condition1 = str(i).encode()
                if b'"CheckSkillCombineConditionTick" guid="CreditB208MOD_2"' in DS_14111[i]:
                    condition2 = str(i).encode()
                if b'"CheckSkillCombineConditionTick" guid="CreditB208MOD_3"' in DS_14111[i]:
                    condition3 = str(i).encode()
            with open(filesxml, 'rb') as f:
                code_fix2 = f.read().replace(b'condition1', condition1).replace(b'condition2', condition2).replace(b'condition3', condition3).replace(b'        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />',b'         <bool name="bEqual" value="true" refParamName="" useRefParam="false" />').replace(b'<int name="skinId" value="14111"', b'<int name="skinId" value="99999"')
            with open(filesxml, 'wb') as f:
                f.write(code_fix2)

        elif ID_SKIN in [b'11107', b'15704', b'10603'] and filesxml1 != 'Death.xml':
            with open(filesxml, 'rb') as file:
                text = file.read()
            text = re.sub(re.escape(b'<String name="clipName" value="'), b'<String name="clipName" value="' + ID_SKIN + b'/', text, flags=re.IGNORECASE)
            with open(filesxml, 'wb') as file:
                file.write(text)
        elif ID_SKIN[:3] == b'537' and filesxml1 == 'S12.xml':
            with open(filesxml, 'rb') as f:
                content = f.read()
            content = content.replace(b'prefab_skill_effects/hero_skill_effects/537_Trip/' + ID_SKIN + b'/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/' + ID_SKIN + b'/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/' + ID_SKIN + b'/Trip_attack_spell01_1_S', b'prefab_skill_effects/hero_skill_effects/537_Trip/' + ID_SKIN + b'/Trip_attack_spell01_1_S')
            with open(filesxml, 'wb') as f:
                f.write(content)
        elif ID_SKIN[:3] ==b'520':
            if filesxml1 == 'P9E2.xml':
                with open(filesxml, 'rb') as f:
                        rpl = f.read().replace(b'<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/520_Veres/'+ID_SKIN+b'/520_Veres_zishen_bron" refParamName="" useRefParam="false" />', b'<String name="resourceName" value="" refParamName="520_Veres_zishen_bron" useRefParam="true" />').replace(b'\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', b'\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="CreditB208MOD" eventType="GetHolidayResourcePathTick" guid="d62b83a3-6e49-384b-ebec-48067784d8ce" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="GetHolidayResourcePathTick" time="0.000" isDuration="false" guid="3a0e9d16-d49b-4e9f-d207-8232c09e8532">\r\n        <String name="holidayResourcePathPrefix" value="prefab_skill_effects/hero_skill_effects/520_Veres/'+ID_SKIN+b'/520_Veres_zishen_bron" refParamName="" useRefParam="false" />\r\n        <String name="outPathParamName" value="520_Veres_zishen_bron" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                        f.close()
                with open(filesxml, 'wb') as f:
                        f.write(rpl)
                if ID_SKIN == b'52011':
                    with open (Dance, 'rb') as f:
                        xich_520 = b'\r\n        <int name="skinId" value="52011" refParamName="" useRefParam="false" />'
                        Bequa_False = b'\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />'
                        mod_dance_52011 = f.read().replace(xich_520,xich_520+ Bequa_False)
                    with open(Dance,'wb') as f:
                        f.write(mod_dance_52011)
        elif ID_SKIN[:3] == b'544':
            if filesxml1 == 'U1E0.xml':
                with open(filesxml, 'rb') as f:
                    content = f.read()
                content = content.replace(b'Bone_Whisk03', b'Bone_Weapon01')
                with open(filesxml, 'wb') as f:
                    f.write(content)
            elif filesxml1 == 'A4B1.xml':
                with open(filesxml, 'rb') as f:
                    content = f.read()
                content = content.replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/' + ID_SKIN + b'/Painter_Atk4_blue', b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_blue')
                content = content.replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/' + ID_SKIN + b'/Painter_Atk4_red', b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_red')
                with open(filesxml, 'wb') as f:
                    f.write(content)
        elif ID_SKIN == b'13011':
            if filesxml1 in ['S2.xml', 'S21.xml', 'S22.xml']:
              with open(filesxml, 'rb') as f:
                  content = f.read()        
              content = content.replace(b'<int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />', b'<int name="skinId" value="99999" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />')
              content = content.replace(b'guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="true"', b'guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="false"')
              content = content.replace(b'130_GongBenWuZang/13011/GongBenWuZang_attack01_spell01_2', b'130_GongBenWuZang/13011/GongBenWuZang_attack01_spell01_1')
              content = content.replace(b'guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="true"', b'guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="false"')
              content = content.replace(b'130_GongBenWuZang/13011/GongBenWuZang_attack01_spell01_3', b'130_GongBenWuZang/13011/GongBenWuZang_attack01_spell01_2')
              with open(filesxml, 'wb') as f:
                  f.write(content)
            if filesxml1 == 'S2B1.xml':
              with open(filesxml, 'rb') as f:
                  content = f.read()
              content = content.replace(b'<TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />', b'<TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n         <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />')
              content = content.replace(b'<TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />', b'<TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />')
              content = content.replace(b'<Event eventName="SpawnObjectDuration" time="0.000" length="2.000" isDuration="true" guid="fc04504a-0865-4d5d-a5e4-e7067150bf42">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />', b'<Event eventName="SpawnObjectDuration" time="0.000" length="2.000" isDuration="true" guid="fc04504a-0865-4d5d-a5e4-e7067150bf42">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />')
              with open(filesxml, 'wb') as f:
                  f.write(content)
        elif ID_SKIN == b'11119':
            if filesxml1 =='A1B1.xml':
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false" />', b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11119/sunshangxiang_fly_01b" refParamName="" useRefParam="false" />\r\n        <Vector3i name="translation" x="0" y="750" z="0" refParamName="" useRefParam="false" />')
                with open(filesxml,'wb') as f:
                    f.write(rpl)
            if filesxml1 == 'A2B1.xml':
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false" />',b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11119/sunshangxiang_fly_01b" refParamName="" useRefParam="false" />\r\n        <Vector3i name="translation" x="0" y="700" z="0" refParamName="" useRefParam="false" />')
                with open(filesxml,'wb') as f:
                    f.write(rpl)
        elif ID_SKIN == b'10611':
            if filesxml1 == 'U1B1.xml':
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'<Condition id="10" guid="2e5f463f-105d-4143-b786-e59ea8b34fa2" status="true" />', b'\r\n    <!-- '+b'CreditB208MOD' +b' -->')
                    f.close()
                with open(filesxml, 'wb') as f:
                    f.write(rpl)
        elif ID_SKIN[:3] == b'131':
            if ID_SKIN in [b'13111', b'13112', b'13116']:
                if filesxml1 =='P1E5.xml':
                    with open(filesxml, 'rb') as f: rpl = f.read().replace(b'guid="5b2bf7a5-7a1b-424c-b3cc-077c4b9376b6" enabled="true"',b'guid="5b2bf7a5-7a1b-424c-b3cc-077c4b9376b6" enabled="false"')
                    with open(filesxml,'wb') as f: f.write(rpl)
        elif ID_SKIN == '11113':
            if filesxml1 =='S1E2.xml':
                with open(filesxml, 'rb') as f: rpl = f.read().replace(b'\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', b'\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="MaterialSwitchDuration0" eventType="MaterialSwitchDuration" guid="a901e786-648c-4a30-a6ec-6eaae0af6581" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n    \t<Condition id="13" guid="ca3dd627-8d6d-4661-b08f-c2fe67130b12" status="false" />\r\n      <Event eventName="MaterialSwitchDuration" time="0.000" length="0.600" isDuration="true" guid="36cf59fc-65d7-40d0-8abc-619b8dde6338">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11113/T3_Sunshuangxiang_skill_01_buff_03" refParamName="" useRefParam="false" />\r\n        <String name="node" value="11114_SunShangXiang_Mid" refParamName="" useRefParam="false" />\r\n        <bool name="bAddMaterial" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(filesxml,'wb') as f: f.write(rpl)
            if filesxml1 =='U1B1.xml':
                with open(filesxml, 'rb') as f: rpl = f.read().repalce(b'<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/111_SunShangXiang/11113/sunshuangxiang_skill_03_hurt" refParamName="" useRefParam="false" />', b'<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/111_SunShangXiang/11113/sunshuangxiang_skill_03_hurt" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.5" z="0.000" refParamName="" useRefParam="false" />')
                with open(filesxml,'wb') as f: f.write(rpl)
        elif ID_SKIN[:3] == b'141':
            if ID_SKIN in [b'14102', b'14103', b'14104', b'14105', b'14106', b'14107', b'14108', b'14109', b'14110', b'14114', b'14115', b'14117', b'14111']:
               if filesxml1 =='S1B2.xml':
                   with open(filesxml, 'rb') as f: rpl = f.read().replace(b'guid="685ff200-95ad-4b43-8471-83a9572b039b" enabled="true"',b'guid="685ff200-95ad-4b43-8471-83a9572b039b" enabled="false"')
                   with open(filesxml,'wb') as f: f.write(rpl)
        elif ID_SKIN == b'13609':
            if filesxml1 =='U1B1.xml':
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03" refParamName="" useRefParam="false" />', b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_1" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_2" refParamName="" useRefParam="false" />').replace(b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_e" refParamName="" useRefParam="false" />', b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_e" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_1_e" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_2_e" refParamName="" useRefParam="false" />')
                with open(filesxml,'wb') as f:
                    f.write(rpl)
        elif ID_SKIN == b'13210':
            if filesxml1 =='S1B0.xml':
                with open ('FILES_CODE/13210/S1B0.xml', 'rb') as f:
                    codefix = f.read()
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', codefix)
                with open(filesxml,'wb') as f:
                    f.write(rpl)
            if filesxml1 =='S11B0.xml':
                with open ('FILES_CODE/13210/S11B0.xml', 'rb') as f:
                    codefix = f.read()
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', codefix)
                with open(filesxml,'wb') as f:
                    f.write(rpl)
            if filesxml1 =='S12B0.xml':
                with open ('FILES_CODE/13210/S12B0.xml', 'rb') as f:
                    codefix = f.read()
                with open(filesxml, 'rb') as f:
                    rpl = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', codefix)
                with open(filesxml,'wb') as f:
                    f.write(rpl)
            if filesxml1 =='S1B2.xml':
                with open ('FILES_CODE/13210/S1B2.xml', 'rb') as f:
                    codefix = f.read()
                with open(filesxml,'wb') as f:
                    f.write(codefix)
            if filesxml1 =='13210_Back.xml':
                with open ('FILES_CODE/13210/13210_Back.xml', 'rb') as f:
                    codefix = f.read()
                with open(filesxml,'wb') as f:
                    f.write(codefix)
                
        elif ID_SKIN[:3] == b'510' and filesxml1 == 'U1M1.xml':
            with open(filesxml, 'rb') as f:
                content = f.read()
            content = content.replace(b'<Action tag="" length="5.000" loop="false">', b'<Action tag="" length="5.000" loop="false">\n    <Track trackName="B208MOD" eventType="GetHolidayResourcePathTick" guid="c0624999-948e-ff69-a6a7-37395abd5fe1" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Event eventName="GetHolidayResourcePathTick" time="0.000" isDuration="false" guid="0c1c6622-95d9-809d-4cd2-fab25aa68b98">\n        <String name="holidayResourcePathPrefix" value="prefab_skill_effects/hero_skill_effects/510_Liliana/'+ID_SKIN+b'/5101_Fox" refParamName="" useRefParam="false" />\n        <String name="outPathParamName" value="5101_Fox" refParamName="" useRefParam="false" />\n        <String name="outSoundEventParamName" value="" refParamName="" useRefParam="false" />\n      </Event>\n    </Track>\n')
            content = content.replace(b'        <String name="prefabName" value="prefab_skill_effects/hero_skill_effects/510_Liliana/'+ID_SKIN+b'/5101_Fox" refParamName="" useRefParam="false" />', b'        <String name="prefabName" value="" refParamName="5101_Fox" useRefParam="true" />')
            with open(filesxml, 'wb') as f:
                f.write(content)

                
        elif ID_SKIN[:3] == b'111' and filesxml1 == b'S1.xml':
            with open(filesxml, 'rb') as f:
                content = f.read()
            content = content.replace(b'prefab_skill_effects/hero_skill_effects/T3_Sunshuangxiang_skill_01_attack_01', b'prefab_skill_effects/hero_skill_effects/111_sunshangxiang/'+ID_SKIN+b'/T3_Sunshuangxiang_skill_01_attack_01')
            with open(filesxml, 'wb') as f:
                f.write(content)
                
        elif ID_SKIN == b'59702' and filesxml1 in ['U1.xml', 'U11.xml']:
            with open(filesxml, 'rb') as f:
                content = f.read()
            content = content.replace(b'prefab_skill_effects/hero_skill_effects/KuangTie_attack_spell03_1', b'prefab_skill_effects/hero_skill_effects/597_kuangtie/'+ID_SKIN+b'/KuangTie_attack_spell03_1')
            content = content.replace(b'prefab_skill_effects/hero_skill_effects/KuangTie_attack02_spell03_1', b'prefab_skill_effects/hero_skill_effects/597_kuangtie/'+ID_SKIN+b'/KuangTie_attack02_spell03_1')            
            with open(filesxml, 'wb') as f:
                f.write(content)
                    
        elif ID_SKIN == b'13311':
            with open(filesxml, 'rb') as f:
                content = f.read()
            content = content.replace(b'prefab_skill_effects/hero_skill_effects/133_direnjie/', b'prefab_skill_effects/component_effects/13311/13311_5/')
            content = content.replace(b'"Play_DiRenJie_Attack_1"', b'"Play_DiRenJie_Attack_1_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Voice_Short"', b'"Play_DiRenJie_Voice_Short_Skin11_AW3"')
            content = content.replace(b'"Play_DiRenJie_Attack_Hit_1"', b'"Play_DiRenJie_Attack_Hit_1_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Skill_A"', b'"Play_DiRenJie_Skill_A_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Voice_Anger"', b'"Play_DiRenJie_Voice_Anger_Skin11_AW3"')
            content = content.replace(b'"Play_DiRenJie_Skill_A_Hit"', b'"Play_DiRenJie_Skill_A_Hit_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Attack_Hit_2"', b'"Play_DiRenJie_Attack_Hit_2_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Skill_B"', b'"Play_DiRenJie_Skill_B_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Skill_B_Hit"', b'"Play_DiRenJie_Skill_B_Hit_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Card_Red"', b'"Play_DiRenJie_Card_Red_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Card_Blue"', b'"Play_DiRenJie_Card_Blue_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Card_Yellow"', b'"Play_DiRenJie_Card_Yellow_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Voice_Dead"', b'"Play_DiRenJie_Voice_Dead_Skin11_AW3"')
            content = content.replace(b'"Play_DiRenJie_Voice_Skill_B"', b'"Play_DiRenJie_Voice_Skill_B_Skin11_AW3"')
            content = content.replace(b'"Play_DiRenJie_Skill_C"', b'"Play_DiRenJie_Skill_C_Skin11_AW2"')
            content = content.replace(b'"Play_DiRenJie_Voice_Skill_C"', b'"Play_DiRenJie_Voice_Skill_C_Skin11_AW3"')
            content = content.replace(b'"Play_DiRenJie_Skill_C_Hit"', b'"Play_DiRenJie_Skill_C_Hit_Skin11_AW2"')
            with open(filesxml, 'wb') as f:
                f.write(content)

        elif ID_SKIN == b'16707':
            with open(filesxml, 'rb') as f:
                content = f.read()
            content = content.replace(b'prefab_skill_effects/hero_skill_effects/167_wukong/', b'prefab_skill_effects/component_effects/16707/16707_5/')
            content = content.replace(b'"Play_Back_WuKong"', b'"Play_Back_WuKong_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Attack_1"', b'"Play_WuKong_Attack_1_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_VO_Short"', b'"Play_WuKong_VO_Short_Skin7_AW4"')
            content = content.replace(b'"Play_WuKong_Attack_Hit_1"', b'"Play_WuKong_Attack_Hit_1_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Attack_2"', b'"Play_WuKong_Attack_2_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_VO_Anger"', b'"Play_WuKong_VO_Anger_Skin7_AW4"')
            content = content.replace(b'"Play_WuKong_Skill_Passive_Hit1"', b'"Play_WuKong_Skill_Passive_Hit1_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_Passive_Hit2"', b'"Play_WuKong_Skill_Passive_Hit2_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_Passive_Hit3"', b'"Play_WuKong_Skill_Passive_Hit3_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_B_2"', b'"Play_WuKong_Skill_B_2_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_B_Hit"', b'"Play_WuKong_Skill_B_Hit_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_VO_Dead"', b'"Play_WuKong_VO_Dead_Skin7_AW4"')
            content = content.replace(b'"Play_WuKong_Skill_A_2"', b'"Play_WuKong_Skill_A_2_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_A_Hit"', b'"Play_WuKong_Skill_A_Hit_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_A_1"', b'"Play_WuKong_Skill_A_1_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_VO_Skill_A"', b'"Play_WuKong_VO_Skill_A_Skin7_AW4"')
            content = content.replace(b'"Play_WuKong_Skill_A_Run"', b'"Play_WuKong_Skill_A_Run_Skin7_AW3"')
            content = content.replace(b'"Stop_WuKong_Skill_A_Run"', b'"Stop_WuKong_Skill_A_Run_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_B_1"', b'"Play_WuKong_Skill_B_1_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_VO_Skill_B"', b'"Play_WuKong_VO_Skill_B_Skin7_AW4"')
            content = content.replace(b'"Play_WuKong_Skill_C"', b'"Play_WuKong_Skill_C_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_VO_Skill_C"', b'"Play_WuKong_VO_Skill_C_Skin7_AW4"')
            content = content.replace(b'"Play_WuKong_Skill_C_01"', b'"Play_WuKong_Skill_C_01_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_C_02"', b'"Play_WuKong_Skill_C_02_Skin7_AW3"')
            content = content.replace(b'"Play_WuKong_Skill_C_Hit"', b'"Play_WuKong_Skill_C_Hit_Skin7_AW3"')

            with open(filesxml, 'wb') as f:
                f.write(content)
            if filesxml1 == 'U1B0.xml':
                DS_16707 =[]
                with open('FILES_CODE/16707.xml', 'rb') as f:
                    code_fix = f.read()
                with open(filesxml, 'rb') as f:
                    code_fix2 = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', code_fix)
                with open(filesxml, 'wb') as f:
                    f.write(code_fix2)
                with open(filesxml, 'rb') as f:
                    code_fix2 = f.readlines()
                for trackcd in code_fix2:
                    if b'stopAfterLastEvent="true">' in trackcd:
                        DS_16707.append(trackcd)
                for i in range (len(DS_16707)):
                    if b'<Track eventType="CheckSkillCombineConditionTick"' in DS_16707[i]:
                        condition1 = str(i).encode()
                with open(filesxml, 'rb') as f:
                    code_fix2 = f.read().replace(b'condition1', condition1)
                with open(filesxml, 'wb') as f:
                    f.write(code_fix2)

        
        #------------------------------SOUND---------------------------------#
        if modsoundages == 'y':
            if ID_SKIN not in [b'13311', b'16707']:
                with open(filesxml, 'rb') as file:
                    text = file.readlines()
                for sound in text:
                    if b'<String name="eventName" value="' in sound:
                        with open(filesxml, 'rb') as file1:
                            text1 = file1.read()
                            sound1 = sound.replace(b'" refParamName' , IDSOUND+b'" refParamName').replace(IDSOUND*2, IDSOUND)
                            text1 = text1.replace(sound, sound1)
                        with open(filesxml, 'wb') as file1:
                            file1.write(text1)
                        if filesxml not in DS_FILES_MOD_SOUND:
                            DS_FILES_MOD_SOUND.append(filesxml)

            #------------------------------CHECK_SKIN------------------------------#


        if ID_SKIN == b'14111' and filesxml1 == 'S1.xml':
            continue
        if ID_SKIN == b'16707' and filesxml1 == 'U1B0.xml':
            continue
        if ID_SKIN == b'15015' and filesxml1 == 'U1.xml':
            continue
        if ID_SKIN == b'10620' and filesxml1 == 'P1.xml':
            continue
        if ID_SKIN == b'11119' and filesxml1 in ['A1B1.xml', 'A2B1.xml', 'A1b2.xml', 'A2b2.xml']:
            continue
        if ID_SKIN == b'10611' and filesxml1 != 'U1E1.xml':
            continue
        if ID_SKIN == b'13609' and filesxml1 != 'S1B1.xml':
            continue
        if ID_SKIN == b'13011' and filesxml1 in ['S2.xml', 'S21.xml', 'S22.xml']:
            continue
            

        with open(filesxml, 'rb') as file1:
            text1 = file1.read()
        LGT = b'\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
        LGF = b'\r\n        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />'
        IDS = b'\r\n        <int name="skinId" value="'+ID_SKIN+b'" refParamName="" useRefParam="false" />'
        SKM = b'\r\n        <int name="skinId" value="99999" refParamName="" useRefParam="false" />'
        EQF = b'\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />'
        EQT = b'\r\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />'
        UNV = b'\r\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />'
        UNF = b'\r\n        <bool name="useNegateValue" value="false" refParamName="" useRefParam="false" />'
        bol = b'\r\n        <bool name="'
        check_vt = b'CheckSkinIdVirtualTick'
        check_sk = b'CheckSkinIdTick'
        SKR = b'<Array name="skinIdArray"'
        #SOAL = b'<SkinOrAvatarList id="'+ID_SKIN+b'" />'
        #SOAF = b'<HeroOrAvatarList id="'+ID_SKIN[:3]+b'" />'
        
        
       
            
        
        if IDS in text1:
            DS_FILES_MOD_CHECK.append(filesxml1)
            for DOAN_CODE in ALL_DOAN_CODE:
                if ID_SKIN == b'13210':
                    if filesxml1 == 'S1B0.xml':
                        if b'guid="5f05ee52-f084-4334-b710-8d9ca42e5eec" enabled="true"' in DOAN_CODE:
                            DOAN_CODE_MOD = DOAN_CODE.replace(IDS, SKM)
                            with open(filesxml, 'rb') as f:
                                code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                            with open(filesxml, 'wb') as f:
                                f.write(code_vt)
                            continue
                    if filesxml1 == 'S11B0.xml':
                        if b'guid="7d02fc49-3e77-44ba-838a-c601631ba8a2" enabled="true"' in DOAN_CODE:
                            DOAN_CODE_MOD = DOAN_CODE.replace(IDS, SKM)
                            with open(filesxml, 'rb') as f:
                                code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                            with open(filesxml, 'wb') as f:
                                f.write(code_vt)
                            continue
                    if filesxml1 == 'S12B0.xml':
                        if b'guid="aac205d6-202e-47d0-b2ff-62e077253759" enabled="true"' in DOAN_CODE:
                            DOAN_CODE_MOD = DOAN_CODE.replace(IDS, SKM)
                            with open(filesxml, 'rb') as f:
                                code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                            with open(filesxml, 'wb') as f:
                                f.write(code_vt)
                            continue
                if check_sk in DOAN_CODE and IDS in DOAN_CODE:
                    if bol not in DOAN_CODE:
                        DOAN_CODE_MOD = DOAN_CODE.replace(IDS, IDS+EQF).replace(IDS, SKM)
                        with open(filesxml, 'rb') as f:
                            code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                        with open(filesxml, 'wb') as f:
                            f.write(code_vt)
                    if EQF in DOAN_CODE:
                        DOAN_CODE_MOD = DOAN_CODE.replace(EQF, b'').replace(IDS, SKM)
                        with open(filesxml, 'rb') as f:
                            code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                        with open(filesxml, 'wb') as f:
                            f.write(code_vt)
                    if EQF not in DOAN_CODE:
                        if EQT in DOAN_CODE:
                            DOAN_CODE_MOD = DOAN_CODE.replace(EQT, EQF).replace(IDS, SKM)
                            with open(filesxml, 'rb') as f:
                                code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                            with open(filesxml, 'wb') as f:
                                f.write(code_vt)
                        if EQF not in DOAN_CODE:
                            DOAN_CODE_MOD = DOAN_CODE.replace(IDS, IDS+EQF).replace(IDS, SKM)
                            with open(filesxml, 'rb') as f:
                                code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                            with open(filesxml, 'wb') as f:
                                f.write(code_vt)
                if check_vt in DOAN_CODE and IDS in DOAN_CODE:
                    if UNV in DOAN_CODE:
                        DOAN_CODE_MOD = DOAN_CODE.replace(UNV, b'').replace(IDS, SKM)
                        with open(filesxml, 'rb') as f:
                            code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                        with open(filesxml, 'wb') as f:
                            f.write(code_vt)
                    if UNV not in DOAN_CODE:
                        if UNF in DOAN_CODE:
                            DOAN_CODE_MOD = DOAN_CODE.replace(UNF, UNV).replace(IDS, SKM)
                            with open(filesxml, 'rb') as f:
                                code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                            with open(filesxml, 'wb') as f:
                                f.write(code_vt)
                        if UNV not in DOAN_CODE:
                            DOAN_CODE_MOD = DOAN_CODE.replace(IDS, IDS+UNV).replace(IDS, SKM)
                            with open(filesxml, 'rb') as f:
                                code_vt = f.read().replace(DOAN_CODE, DOAN_CODE_MOD)
                            with open(filesxml, 'wb') as f:
                                f.write(code_vt)
                #if SOAL in DOAN_CODE:    
                   #with open(filesxml, 'rb') as f:
                       #code_vt = f.read().replace(SOAL, SOAF)
                   #with open(filesxml, 'wb') as f:
                       #f.write(code_vt)
                       #print(Style.BRIGHT + Fore.CYAN + "[•]", Style.BRIGHT + Fore.YELLOW + "Check SkinAvatar", Style.BRIGHT + Fore.GREEN + "Done !")
                    
                #else:
                    #print(Style.BRIGHT + Fore.CYAN + "[•]", Style.BRIGHT + Fore.YELLOW + "Check SkinAvatar", Style.BRIGHT + Fore.RED + "No ID !")
                    
                    
                   
    if len(DS_FILES_MOD_CHECK) != 0:
        print(Style.BRIGHT + Fore.GREEN+'┌'+'─'*23, Style.BRIGHT + Fore.CYAN+'CHECK_SKIN',Style.BRIGHT + Fore.GREEN+'─'*23+'┐')
        print(Style.BRIGHT + Fore.GREEN + '│'+' '*58+'│')
        for chek in DS_FILES_MOD_CHECK:
            chek = '[ ' +chek+' ]'
            chek = chek.center(58)
            chek = Style.BRIGHT + Fore.GREEN +'│' + Style.BRIGHT + Fore.YELLOW + chek+  Style.BRIGHT + Fore.GREEN + '│'
            print(chek)
        print(Style.BRIGHT + Fore.GREEN + '│'+' '*58+'│')
        print(Style.BRIGHT + Fore.GREEN + '└'+'─'*58+'┘')
    print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.BLUE + str(len(DS_FILES_MOD_SOUND)), Style.BRIGHT + Fore.WHITE + '/', Style.BRIGHT + Fore.BLUE + str(len(FILES_XML)), Style.BRIGHT + Fore.GREEN + 'Sound Files!')
    print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.MAGENTA + str(len(DS_FILES_MOD_EFFECT)), Style.BRIGHT + Fore.WHITE + '/', Style.BRIGHT + Fore.MAGENTA + str(len(FILES_XML)), Style.BRIGHT + Fore.GREEN + 'Effect Files!')



    return
def replace_skin_avatar_list(destination_path, NAME_HERO, ID_SKIN):
    THU_MUC_SKILL = os.path.join(destination_path, NAME_HERO, 'Skill')
    FILES_XML = [file for file in os.listdir(THU_MUC_SKILL) if file.endswith('.xml')]
    
    SOAL = f'<SkinOrAvatarList id="{ID_SKIN}" />'
    SOAF = f'<SkinOrAvatarList id="99999" />'
    
    for file_name in FILES_XML:
        file_path = os.path.join(THU_MUC_SKILL, file_name)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                xml_content = file.read()
            
            updated_content = xml_content.replace(SOAL, SOAF)
            
            filter_types = re.findall(r'SkinAvatarFilterType="(.*?)"', updated_content)
            if len(filter_types) == 2:
                updated_content = re.sub(
                    r'SkinAvatarFilterType="(.*?)"',
                    lambda m: f'SkinAvatarFilterType="{filter_types[1] if m.group(1) == filter_types[0] else filter_types[0]}"',
                    updated_content
                )
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
                
        except UnicodeDecodeError:
            continue

class StringBytes:
    def __init__(self,String):
        self.String=String
        self.OldString=String
    def tell(self):
        return len(self.OldString)-len(self.String)
    def seek(self,I,O=0):
        if O==0:
            self.String=self.OldString[I:]
        elif O==1:
            self.String=self.String[I:]
    def read(self,Int=None):
        if Int==None:
            if type(self.String)==str:
                return ""
            else:
                return b""
        R=self.String[:Int]
        self.String=self.String[Int:]
        return R

class Bytes_XML:
    def decode(String):
        def get_int(A):
            return int.from_bytes(A.read(4), 'little')
        
        def get_str(A, pos=None):
            if pos is not None:
                A.seek(pos, 0)
            ofs = get_int(A)
            stri = A.read(ofs-4)
            return stri.decode()
        
        def get_node(A, fid=None, sta=None):
            global i
            ofs = get_int(A)
            stri = get_str(A)
            stri1 = stri
            myid = i
            i += 1
            A.seek(4, 1)
            aidx = get_int(A)
            ite = False
            attr = {}
            for j in range(0, aidx):
                attr1 = get_attr(A)
                if type(attr1) == str:
                    text1 = attr1
                    ite = True
                else:
                    attr.update(attr1)
            if fid is None:
                nod[myid] = ET.SubElement(root, stri1, attrib=attr)
            else:
                nod[myid] = ET.SubElement(nod[fid], stri1, attrib=attr)
            if ite:
                if text1 == '':
                    nod[myid].set("value",' ')
                else:
                    nod[myid].set("value",text1)
            check_four(A)
            chk = sta + ofs - A.tell()
            if chk > 12:
                A.seek(4, 1)
                sidx = get_int(A)
                for h in range(0, sidx):
                    get_node(A, myid, A.tell())
            A.seek(sta + ofs, 0)
        
        def get_attr(A, pos=None):
            if pos is None:
                pos = A.tell()
            ofs = get_int(A)
            type = get_int(A)
            if type == 5:
                stri = A.read(ofs - 8).decode()[1:]
                check_four(A)
                A.seek(pos + ofs, 0)
                return stri
            else:
                if type == 6:
                    stri = A.read(ofs - 8).decode()
                    if stri[0:2] == 'JT':
                        if stri == 'JTArr':
                            stri = 'Array'
                        elif stri == 'JTPri':
                            stri = 'String'
                        else:
                            stri = stri[2:]
                        name = 'var'
                    else:
                        name = 'var_Raw'
                elif type == 8:
                    stri2 = A.read(ofs - 8).decode()
                    if stri2[0:4] == 'Type':
                        stri = stri2[4:]
                        name = 'type'
                    else:
                        stri = stri2
                        name = 'type_Raw'
                else:
                    stri = A.read(ofs - 8).decode()
                    name = str(type)
                    A.seek(pos + ofs, 0)
                return {name:stri}
        
        def check_four(A):
            if get_int(A) != 4:
                A.seek(-4, 1)
        A=StringBytes(String)
        global i, nod, root
        i = 0
        nod = {}
        ofs = get_int(A)
        stri = get_str(A)
        stri1 = stri
        A.seek(4, 1)
        aidx = get_int(A)
        ite = False
        attr = {}
        for j in range(0, aidx):
            attr1 = get_attr(A)
            if type(attr1) == str:
                text1 = attr1
                ite = True
            else:
                attr.update(attr1)
        root = ET.Element(stri1, attrib=attr)
        if ite:
            nod[myid].set("value",text1)
        check_four(A)
        chk = ofs - A.tell()
        if chk > 12:
            A.seek(4, 1)
            sidx = get_int(A)
            for h in range(0, sidx):
                get_node(A, None, A.tell())
                
        try:return minidom.parseString(ET.tostring(root,"utf-8").decode()).toprettyxml(indent="  ",newl="\r\n").encode()
        except: return ET.tostring(root,"utf-8").decode()
    
    def encode(xmlfile):
        def byteint(num):
            return num.to_bytes(4, byteorder='little')

        def bytestr(stri):
            outbyte = byteint(len(stri) + 4)
            outbyte = outbyte + stri.encode()
            return outbyte

        def byteattr(key, attr):
            if key == 'var':
                if attr[key] == 'Array':
                    stri = 'JTArr'
                elif attr[key] == 'String':
                    stri = 'JTPri'
                else:
                    stri = 'JT' + attr[key]
                aid = 6
            elif key == 'var_Raw':
                stri = attr[key]
                aid = 6
            elif key == 'type':
                stri = 'Type' + attr[key]
                aid = 8
            elif key == 'type_Raw':
                stri = attr[key]
                aid = 8
            elif key == "value": return b""
            else:
                import unicodedata
                if unicodedata.numeric(key):
                    stri = attr[key]
                    aid = int(key)
            stripro = stri.encode()
            outbyte = byteint(len(stripro) + 8) + byteint(aid) + stripro
            return outbyte

        def bytenode(node):
            iftex = False
            name1 = node.tag
            name = bytestr(name1)
            attr1 = b''
            aindex = len(node.attrib)
            
            plus = 8
            for key in node.attrib:
                if key=="value":aindex-=1
                attr1 = attr1 + byteattr(key, node.attrib)
            if (node.get("value") != None) and (node.get("value")[0:1] != '\n'):
                if node.get("value") == ' ':
                    stri1 = ''
                else:
                    stri1 = node.get("value")
                iftex = True
                stripro = ('V' + stri1).encode()
                attr1 = attr1 + byteint(len(stripro) + 8) + byteint(5) + stripro + byteint(4)
                aindex += 1
                plus = 4
            attr1 = byteint(len(attr1) + plus) + byteint(aindex) + attr1 + byteint(4)
            alchild = b''
            if len(node):
                cindex = 0
                for child in node:
                    alchild = alchild + bytenode(child)
                    cindex += 1
                alchild = byteint(len(alchild) + 8) + byteint(cindex) + alchild
            else:
                if iftex == False:
                    alchild = byteint(4)
            bnode = name + attr1 + alchild
            bnode = byteint(len(bnode) + 4) + bnode
            return bnode

        tree = ET.fromstring(xmlfile)
        byt = bytenode(tree)
        return byt
def process_file(file_path, LC):
    with open(file_path, "rb") as f:
        G = f.read()
        with open(file_path, "wb") as f1:
            try:
                if LC == "1":
                    f1.write(Bytes_XML.decode(G))
                elif LC == "2":
                    f1.write(Bytes_XML.encode(G.decode()))
            except:
                f1.write(G)


def process_file(file_path, LC):
    with open(file_path, "rb") as f:
        G = f.read()
        with open(file_path, "wb") as f1:
            try:
                if LC == "1":
                    f1.write(Bytes_XML.decode(G))
                elif LC == "2":
                    f1.write(Bytes_XML.encode(G.decode()))
            except Exception as e:
                print(f"ERROR {file_path}: {e}")#CHONAYNE

def process_directory(directory_path, LC):

    file_path = directory_path
    process_file(file_path, LC)
    
import re
import xml.etree.ElementTree as ET

def ngoaihinh(ID_SKIN, file_path, P_K, chonpk1, NAME_HERO):
    #print(P_K)#CHONAYNE
    IDINFO=int(ID_SKIN)+1
    IDINFO=str(IDINFO)
    if str(IDINFO)[3:4] == '0':
        IDINFO=IDINFO[:3]+IDINFO[4:]
    IDINFO=str(IDINFO)
    if len(str(IDINFO)) == 5:
        ID_SKIN_EFF = int(IDINFO) - 1
    elif len(str(IDINFO)) == 4:
        ID_SKIN_EFF = (int(IDINFO[:-1] + "0" + IDINFO[-1]) - 1)
    code_skin_mod = ''
    with open(file_path, 'r',  encoding="utf-8") as file:
        ALL_CODE_GOC = file.read()
        STAR_END = re.compile(r'\n    <Element var="Com" type="Assets.Scripts.GameLogic.SkinElement">.*?\n    </Element>', re.DOTALL)
        DOAN_CODE = STAR_END.findall(ALL_CODE_GOC)
    for codeskinmod in DOAN_CODE:
        if '/'+ IDINFO + '_' in codeskinmod:
            kiemtra = codeskinmod.split('\n')
            if '/'+ IDINFO + '_' in kiemtra[3]:                
                if 'hero_skill_effects' in codeskinmod.lower() and str(ID_SKIN_EFF) not in ['13311', '16707']:
                    dongcode = codeskinmod.split('\n')
                    for dongcodeeff in dongcode:
                        if 'hero_skill_effects' in dongcodeeff.lower():
                            dongcodeeff1 = dongcodeeff[58:-3]
                            chiacodeeff = dongcodeeff.split('/')
                            hero = chiacodeeff[2]
                            dongcodeeff2 = dongcodeeff.replace(hero, hero+'/'+str(ID_SKIN_EFF)).replace('/'+str(ID_SKIN_EFF)+'/'+str(ID_SKIN_EFF)+'/', '/'+str(ID_SKIN_EFF)+'/')
                            codeskinmod = codeskinmod.replace(dongcodeeff, dongcodeeff2)

                if IDINFO == '13312':
                    codeskinmod = codeskinmod.replace(
                        'Prefab_Characters/Prefab_Hero/133_DiRenJie/13312_DiRenJie_AW1_',
                        'Prefab_Characters/Prefab_Hero/133_DiRenJie/awaken/13312_DiRenJie_04_'
                    ).replace(
                        'Prefab_Characters/Prefab_Hero/133_DiRenJie/1331_DiRenJie_Cam',
                        'Prefab_Characters/Prefab_Hero/133_DiRenJie/awaken/13312_DiRenJie_aw5_Cam'
                    )

                if IDINFO == '1678':
                    codeskinmod = codeskinmod.replace(
                        'Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_Cam"/>',
                        'Prefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_SunWuKong_03_Cam"/>\n  <ArtSkinLobbyShowMovie var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_SunWuKong_03_Movie"/>'
                    ).replace(
                        'Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_',
                        'Prefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_SunWuKong_03_'
                    ).replace(
                        'prefab_skill_effects/hero_skill_effects/167_WuKong/',
                        'prefab_skill_effects/component_effects/16707/16707_5/'
                    )

                if P_K != '' and chonpk1 != 1:
                    if str(ID_SKIN_EFF) not in ['13312', '1678']:
                        dongcode = codeskinmod.split('\n')
                        for dongcodeeff in dongcode:
                            if 'prefab_characters/prefab_hero/' in dongcodeeff.lower() and 'artskinlobbyshowcamera' not in dongcodeeff.lower():
                                dongcodeeff1 = dongcodeeff[58:-3]
                                chiacodeeff = dongcodeeff.split('/')
                                hero = chiacodeeff[2]
                                dongcodeeff2 = dongcodeeff.replace(hero, f'{hero}/Component').replace('_LOD', f'{P_K.decode()}LOD').replace('_Show', f'{P_K.decode()}Show')
                                codeskinmod = codeskinmod.replace(dongcodeeff, dongcodeeff2)

                code_skin_mod = codeskinmod
                #code_skin_mod = code_skin_mod.replace('<Element var="String" type="System.String" value=" "/>', f'<Element var="String" type="System.String" value=" CRE_B208_MOD_{IDINFO} "/>')
                code_skin_mod = codeskinmod.replace('_LOD2', '_LOD1').replace('_LOD3', '_LOD1').replace('Show3"/>', 'Show1"/>').replace('show3"/>', 'Show1"/>').replace('Show2"/>', 'Show1"/>').replace('show2"/>', 'Show1"/>')
                code_skin_mod = code_skin_mod.replace('<Element var="String" type="System.String" value=" "/>', f'<Element var="String" type="System.String" value=" CREDIT_B208_MOD_{NAME_HERO}-{IDINFO} "/>')

    if code_skin_mod != '':
        for codeskinphu in DOAN_CODE:
            if IDINFO[:3] in codeskinphu:
                with open(file_path, 'r',  encoding="utf-8") as file:
                    ALL_CODE_GOC = file.read()
                ALL_CODE_GOC = ALL_CODE_GOC.replace(codeskinphu, code_skin_mod)
                with open(file_path, 'w', encoding="utf-8") as file: 
                    file.write(ALL_CODE_GOC)
        with open(file_path, 'r',  encoding="utf-8") as file:
            ALL_CODE_GOC = file.read()
        STAR_END = re.compile(r'\n  <ArtPrefabLOD var="Array" type="System\.String\[\]">.*?\n  <SkinPrefab var="Array" type="Assets\.Scripts\.GameLogic\.SkinElement\[\]">', re.DOTALL)
        DOAN_CODE = STAR_END.findall(ALL_CODE_GOC)
        for codemd in DOAN_CODE:
            codemd = codemd.replace('\n  <SkinPrefab var="Array" type="Assets.Scripts.GameLogic.SkinElement[]">','')
        codemdskin = code_skin_mod.replace('\n    <Element var="Com" type="Assets.Scripts.GameLogic.SkinElement">','').replace('\n    </Element>', '').replace('ArtSkinPrefabLOD', 'ArtPrefabLOD').replace('ArtSkinPrefabLODEx', 'ArtPrefabLODEx').replace('ArtSkinLobbyShowLOD', 'ArtLobbyShowLOD').replace('ArtSkinLobbyIdleShowLOD', 'ArtLobbyIdleShowLOD').replace('      <', '  <').replace('        <', '    <').replace('          <', '      <')
        with open(file_path, 'r', encoding="utf-8") as file:
            ALL_CODE_GOC = file.read()
        ALL_CODE_GOC = ALL_CODE_GOC.replace(codemd, codemdskin)
        with open(file_path, 'w', encoding="utf-8") as file: 
            file.write(ALL_CODE_GOC)
        tree = ET.ElementTree(ET.fromstring(ALL_CODE_GOC))
        root = tree.getroot()

        # Xóa giá trị của <ActorName>
        actor_name = root.find('ActorName')
        if actor_name is not None:
            actor_name.set('value', 'Copyright protects original works of authorship, ensuring that creators have exclusive rights to their creations.\n\nUnauthorized access or use of copyrighted material is prohibited, as it infringes on the creator\'s rights and undermines their ability to benefit from their work.\n\nIt is crucial to respect these rights to foster creativity and innovation in our society.')

        # Thêm phần tử <Credit>
        credit = ET.Element('Credit', var="String", type="System.String", value="B208MOD")
        root.append(credit)

        # Lưu lại file
        tree.write(file_path, encoding='utf-8', xml_declaration=True)

        print(Style.BRIGHT + Fore.CYAN + '[•]', Style.BRIGHT + Fore.CYAN + f'Actor_{IDINFO[:3]}_Infos.pkg.bytes', Style.BRIGHT + Fore.GREEN + ' Done!')
    else:
        print(Style.BRIGHT + Fore.CYAN + '[•]', Style.BRIGHT + Fore.CYAN + f'Actor_{IDINFO[:3]}_Infos.pkg.bytes', Style.BRIGHT + Fore.RED + ' ID Not Found!')

    if IDINFO in ['12913', '19016']:
      for actor in root.findall(".//ActorName"):
          new_element = ET.Element("useStateDrivenMecanim")
          new_element.set("var", "String")
          new_element.set("type", "System.Boolean")
          new_element.set("value", "True")
        
          parent = actor.getparent() if hasattr(actor, "getparent") else root
          index = list(parent).index(actor)
          parent.insert(index + 1, new_element)
  
      for use_mecanim in root.findall(".//useMecanim[@var='String'][@type='System.Boolean'][@value='True']"):
          use_mecanim.set("value", "False")

      tree.write(file_path, encoding="utf-8", xml_declaration=True)
  
    
    
def timpk(ID_SKIN, file_mod_Character, file_map):
    with open(file_mod_Character, 'rb') as f:
        p5 = f.read()
    with open(file_map, 'rb') as f:
        files = f.readlines()

    DS_PK = []
    ID_1 = ID_SKIN
    DS_RT = []
    DDSK = hex(int(ID_1))[2:]
    if len(DDSK) % 2 != 0:
         DDSK = '0' + DDSK
    DDSK = DDSK[-2:] + DDSK[-4:-2]
    DDSK = bytes.fromhex(DDSK)
    DDSK = b'\x00\x00'+DDSK+b'\x00\x00'
    VT=p5.find(int(ID_1).to_bytes(4,'little'))-155
    VT1 = DDSK
    while True:
        dem=b''
        VT1=p5[VT:VT+4]
        VTR=int.from_bytes(VT1,'little')
        VT1=p5[VT:VT+VTR+4]
        CodeCuoi=p5[VTR+4:]
        p5=CodeCuoi
        if DDSK not in VT1:
            break
        a = VT1.hex()[76:]
        b = a[:38]
        b = b.encode().fromhex(b)

        for dong in files:
            if b in dong:
                tenpk = dong[22:-2].decode(errors='ignore')
                DS_PK.append(tenpk)
    P_K = ''
    chonpk1 = ''
    if len(DS_PK) != 0:
        print(Style.BRIGHT + Fore.RED +f'==========> [Input Character] <==========')
        for pk in range (len(DS_PK)):
            pk1 = '['+str(pk+1) +'] '+ (DS_PK[pk])
            DS_RT.append(b'_RT_' + str(pk+1).encode()+b'_')
            print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + pk1)
        SO_PK = len(DS_RT)
        chonpk1 = 1#int(input(Style.BRIGHT + Fore.CYAN + '[•]'+Style.BRIGHT + Fore.GREEN + 'INPUT: ' + Style.BRIGHT + Fore.BLUE))
        chonpk = chonpk1 - 1
        modpk = DS_RT[chonpk]
        P_K = modpk
    return P_K, chonpk1
def process_input_numbers(numbers):
    results = []

    for number in numbers:
        number_str = str(number)
        
        if len(number_str) == 5:
            results.append(number - 1)
        elif len(number_str) == 4:
            results.append(int(number_str[:-1] + "0" + number_str[-1]) - 1)
        else:
            return None
    
    return results
def zip_folder(folder_path, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_STORED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    shutil.rmtree(folder_path)
    

def giai(path_directory):

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        sys.exit(1)

    if not args:
        args = [path_directory]

    path_directory = set(args)

    for inp_path in list(path_directory):
        if os.path.isdir(inp_path):
            path_directory.discard(inp_path)
            for entry in os.scandir(inp_path):
                if entry.is_file():
                    path_directory.add(entry.path)

    for inp_path in path_directory:
        inp_dl1 = None
        try:
            with open(inp_path, "rb") as f:
                inp_dl1 = f.read()
        except FileNotFoundError:
            continue

        opt = None
        for o, a in opts:
            if o in ("-h", "--help"):
                sys.exit()
            elif o in ("-c", "--compress"):
                opt = "-c"
            elif o in ("-d", "--decompress"):
                opt = "-d"

        if opt is None:
            pos = inp_dl1.find(b"\x22\x4a\x67\x00")
            if pos != -1:
                opt = "-d"
            else:
                opt = "-d"

        try:
            if opt in ("-d", "--decompress"):
                inp_dl1 = inp_dl1[inp_dl1.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã hoá"
                DL1 = pyzstd.decompress(inp_dl1, pyzstd.ZstdDict(ZSTD_DICT, True))

                out_path = inp_path
                with open(out_path, "wb") as output_file:
                    output_file.write(DL1)
        except pyzstd.ZstdError:
            continue

def tinhcondition(Back):
    DS_code = []
    with open (Back, 'rb') as f:
        code_back = f.readlines()
    for code in code_back:
        if b'<Track trackName="' in code:
            DS_code.append(code)
    condition = len(DS_code)

    return condition

    
def bv15412(Back):
    DS_track = []
    with open ('FILES_CODE/15412_Back.xml', 'rb') as f:
        codefix = f.read()
    with open (Back, 'rb') as f:
        code = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', codefix)
    with open (Back, 'wb') as f:
        f.write(code)
    with open (Back, 'rb') as f:
        track = f.readlines()
    for track1 in track:
        if b'<Track trackName="' in track1:
            DS_track.append(track1)
    for i in range (len(DS_track)):
        if b'<Track trackName="CreditB208MOD_15412" eventType="CheckHeroIdTick" guid="CreditB208MOD_15412"' in DS_track[i]:
            condition1 = str(i).encode()
        if b'<Track trackName="CreditB208MOD_15412_2" eventType="CheckSkillCombineConditionTick" guid="CreditB208MOD_15412_2"' in DS_track[i]:
            condition2 = str(i).encode()
        if b'<Track trackName="CreditB208MOD_15412_3" eventType="CheckSkillCombineConditionTick" guid="CreditB208MOD_15412_3"' in DS_track[i]:
            condition3 = str(i).encode()
    with open (Back, 'rb') as f:
        code = f.read().replace(b'condition1', condition1).replace(b'condition2', condition2).replace(b'condition3', condition3)
    with open (Back, 'wb') as f:
        f.write(code)

def bienve(ID_SKIN, NAME_HERO,ID_HERO, Back, code_bv_skill):
    if ID_SKIN == '15412':
        bv15412(Back)
    else:
        with open('FILES_CODE/CHECK_BV.xml', 'rb') as f:
            check_bv = f.read()
        with open('FILES_CODE/CODE_BV.xml', 'rb') as f:
            code_bv = f.read()
        condition = tinhcondition(Back)
        code_bv_tong = check_bv+code_bv_skill.replace(b'stopAfterLastEvent="true">', b'stopAfterLastEvent="true">\r\n      <Condition id="'+str(condition).encode()+b'" guid="'+b'CreditB208MOD_'+ID_SKIN.encode()+b'" status="true" />')+code_bv.replace(b'stopAfterLastEvent="true">', b'stopAfterLastEvent="true">\r\n      <Condition id="'+str(condition).encode()+b'" guid="'+b'CreditB208MOD_'+ID_SKIN.encode()+b'" status="true" />')
        code_bv_tong = code_bv_tong.replace(b'ID_SKIN', ID_SKIN.encode()).replace(b'ID_HERO', ID_HERO.encode()).replace(b'NAME_HERO', NAME_HERO.encode())
        with open(Back, 'rb') as f:
            code_back = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', code_bv_tong)
        with open(Back, 'wb') as f:
            f.write(code_back)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.BLUE + "Back.xml Đã Mod !", Style.BRIGHT + Fore.GREEN + ' Done!')
    if ID_SKIN == '13112':
       with open(Back, 'rb') as f:
           content = f.read()
           content = content.replace(b'131_libai/Huicheng_tongyong_01_qipao', b'131_libai/13112/Huicheng_tongyong_01_qipao')
       with open(Back, 'wb') as f:
           f.write(content)
    elif ID_SKIN == '17106':
       with open(Back, 'rb') as f:
           content = f.read()
           content = content.replace(b'171_zhangfei/ZhangFei', b'171_zhangfei/17106/ZhangFei')
           content = content.replace(b'guid="00257a6b-f79e-4032-b768-b3a43bd13fba" enabled="true"', b'guid="00257a6b-f79e-4032-b768-b3a43bd13fba" enabled="false"')
       with open(Back, 'wb') as f:
           f.write(content)
    elif ID_SKIN == '50604':
       with open(Back, 'rb') as f:
           content = f.read()
           content = content.replace(b'506_DarkKnight/5065_Huicheng_01', b'506_DarkKnight/50604/5065_Huicheng_01')
       with open(Back, 'wb') as f:
           f.write(content)
    elif ID_SKIN == '52710':
       with open(Back, 'rb') as f:
           content = f.read()
           content = content.replace(b'<SkinOrAvatarList id="52710" />', b'<HeroOrAvatarList id="527" />')
       with open(Back, 'wb') as f:
           f.write(content)       
    elif ID_SKIN == '13015':
       with open(Back, 'rb') as f:
           content = f.read()
           content = content.replace(b'130_gongbenwuzang/huicheng_tongyong_01_new', b'130_gongbenwuzang/13015/huicheng_tongyong_01_new')
       with open(Back, 'wb') as f:
           f.write(content)
    
def giatoc(ID_SKIN, NAME_HERO, ID_HERO, hasteE1, HasteE1_leave):
    FILES = [hasteE1, HasteE1_leave]
    for file in FILES:

        with open('FILES_CODE/CHECK_GT.xml', 'rb') as f:
            check_gt = f.read()
        with open('FILES_CODE/CODE_GT.xml', 'rb') as f:
            code_gt1 = f.read()
        condition = tinhcondition(file)
        
        # Kiểm tra ID_SKIN và chọn tệp XML phù hợp
        if ID_SKIN == '15710':
            with open('FILES_CODE/CODE_GT_15710.xml', 'rb') as f:
                code_gt1 = f.read()
            code_gt_tong = check_gt.replace(b'ID_SKIN', ID_SKIN.encode()).replace(b'ID_HERO', ID_HERO.encode()).replace(b'NAME_HERO', NAME_HERO.encode()) + code_gt1.replace(b'stopAfterLastEvent="true">', b'stopAfterLastEvent="true">\r\n      <Condition id="' + str(condition).encode() + b'" guid="' + b'CreditB208MOD_' + ID_SKIN.encode() + b'" status="true" />')
        
        elif ID_SKIN == '15015':
            with open('FILES_CODE/CODE_GT_15015.xml', 'rb') as f:
                code_gt1 = f.read()
            code_gt_tong = check_gt.replace(b'ID_SKIN', ID_SKIN.encode()).replace(b'ID_HERO', ID_HERO.encode()).replace(b'NAME_HERO', NAME_HERO.encode()) + code_gt1.replace(b'stopAfterLastEvent="true">', b'stopAfterLastEvent="true">\r\n      <Condition id="' + str(condition).encode() + b'" guid="' + b'CreditB208MOD_' + ID_SKIN.encode() + b'" status="true" />')
        
        else:
            code_gt_tong = check_gt + code_gt1.replace(b'stopAfterLastEvent="true">', b'stopAfterLastEvent="true">\r\n      <Condition id="' + str(condition).encode() + b'" guid="' + b'CreditB208MOD_' + ID_SKIN.encode() + b'" status="true" />')
            code_gt_tong = code_gt_tong.replace(b'ID_SKIN', ID_SKIN.encode()).replace(b'ID_HERO', ID_HERO.encode()).replace(b'NAME_HERO', NAME_HERO.encode())
        
        with open(file, 'rb') as f:
            code_gt = f.read().replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>', code_gt_tong)
        
        with open(file, 'wb') as f:
            f.write(code_gt)
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.BLUE + "HasteE1 and HasteE1_L  Xong !", Style.BRIGHT + Fore.GREEN + ' Done!')
        if ID_SKIN == '54307':
            with open(file, 'rb') as f:
                content = f.read()
            content = content.replace(b'54307/JiaSu_tongyong_01', b'54307/Yao_Sprint')
            with open(file, 'wb') as f:
                f.write(content)
            #print(Style.BRIGHT + Fore.CYAN + '[•]', Style.BRIGHT + Fore.BLUE + file, Style.BRIGHT + Fore.GREEN + ' Updated!')
        elif ID_SKIN == '11607':
            with open(file, 'rb') as f:
                content = f.read()
            content = content.replace(b'11607/JiaSu_tongyong_01', b'11607/jingke_sprint_01')
            with open(file, 'wb') as f:
                f.write(content)
        elif ID_SKIN == '15412':
            with open(file, 'rb') as f:
                content = f.read()
            content = content.replace(b'15412/JiaSu_tongyong_01', b'15412/huijidi_01_lobby')
            with open(file, 'wb') as f:
                f.write(content)
        elif ID_SKIN == '52011':
            with open(file, 'rb') as f:
                content = f.read()
            content = content.replace(b'52012/JiaSu_tongyong_01', b'52011/520_Veres_long_sprint_loop')
            with open(file, 'wb') as f:
                f.write(content)
        elif ID_SKIN == '16307':
            with open(file, 'rb') as f:
                content = f.read()
            content = content.replace(b'16307/JiaSu_tongyong_01', b'16307/juyoujing_jiasu_01')
            with open(file, 'wb') as f:
                f.write(content)

        elif ID_SKIN == '14111':
            with open(file, 'rb') as f:
                content = f.read()
            content = content.replace(b'<String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/JiaSu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />', b'<String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/14111_luoer_sprint" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.0" z="0.0" refParamName="" useRefParam="false" />')
            with open(file, 'wb') as f:
                f.write(content)
            #print(Style.BRIGHT + Fore.CYAN + '[•]', Style.BRIGHT + Fore.BLUE + file, Style.BRIGHT + Fore.GREEN + ' Updated!')


def fixlag(ID_SKIN, NAME_HERO, files_fix):
    ID_SKIN = ID_SKIN.encode()
    if ID_SKIN not in [b'13311', b'16707']:
        with open(files_fix, 'rb') as file:
            text = file.read()
        text = re.sub(re.escape(b"prefab_skill_effects/hero_skill_effects/" + NAME_HERO.encode() + b'/'), b"prefab_skill_effects/hero_skill_effects/" + NAME_HERO.encode() + b'/' + ID_SKIN + b'/', text, flags=re.IGNORECASE)
        text = re.sub(re.escape(b'/'+ID_SKIN+b'/'+ID_SKIN+b'/'), b'/'+ID_SKIN+b'/', text, flags=re.IGNORECASE)
        with open(files_fix, 'wb') as file:
            file.write(text)
        if ID_SKIN in [b'15704', b'11107']:
            if ID_SKIN == b'15704':
                with open(files_fix, 'rb') as file:
                    text = file.read()
                text = text.replace(b'<v1 var="String" type="System.String" value="Born"/>', b'<v1 var="String" type="System.String" value="15704/Born"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Revival"/>', b'<v1 var="String" type="System.String" value="15704/Revival"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Revival2"/>', b'<v1 var="String" type="System.String" value="15704/Revival2"/>')
                #text = text.replace(b'<v1 var="String" type="System.String" value="Dead"/>', b'<v1 var="String" type="System.String" value="15704/Dead"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Atk4"/>', b'<v1 var="String" type="System.String" value="15704/Atk4"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Atk1"/>', b'<v1 var="String" type="System.String" value="15704/Atk1"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Atk3"/>', b'<v1 var="String" type="System.String" value="15704/Atk3"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Hit"/>', b'<v1 var="String" type="System.String" value="15704/Hit"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Stun"/>', b'<v1 var="String" type="System.String" value="15704/Stun"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell2"/>', b'<v1 var="String" type="System.String" value="15704/Spell2"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell1_2"/>', b'<v1 var="String" type="System.String" value="15704/Spell1_2"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell1_1"/>', b'<v1 var="String" type="System.String" value="15704/Spell1_1"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell1_1_2"/>', b'<v1 var="String" type="System.String" value="15704/Spell1_1_2"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell3"/>', b'<v1 var="String" type="System.String" value="15704/Spell3"/>')
                with open(files_fix, 'wb') as file:
                    file.write(text)
            if ID_SKIN == b'11107':
                with open(files_fix, 'rb') as file:
                    text = file.read()
                text = text.replace(b'<v1 var="String" type="System.String" value="Born"/>', b'<v1 var="String" type="System.String" value="11107/Born"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Revival"/>', b'<v1 var="String" type="System.String" value="11107/Revival"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Revival2"/>', b'<v1 var="String" type="System.String" value="11107/Revival2"/>')
                #text = text.replace(b'<v1 var="String" type="System.String" value="Dead"/>', b'<v1 var="String" type="System.String" value="11107/Dead"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Atk1"/>', b'<v1 var="String" type="System.String" value="11107/Atk1"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Atk2"/>', b'<v1 var="String" type="System.String" value="11107/Atk2"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell1"/>', b'<v1 var="String" type="System.String" value="11107/Spell1"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Atk3"/>', b'<v1 var="String" type="System.String" value="11107/Atk3"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Run"/>', b'<v1 var="String" type="System.String" value="11107/Run"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Run2"/>', b'<v1 var="String" type="System.String" value="11107/Run2"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Idle"/>', b'<v1 var="String" type="System.String" value="11107/Idle"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Idle2"/>', b'<v1 var="String" type="System.String" value="11107/Idle2"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell2"/>', b'<v1 var="String" type="System.String" value="11107/Spell2"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell_SSX"/>', b'<v1 var="String" type="System.String" value="11107/Spell_SSX"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell2_1"/>', b'<v1 var="String" type="System.String" value="11107/Spell2_1"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell3_1"/>', b'<v1 var="String" type="System.String" value="11107/Spell3_1"/>')
                text = text.replace(b'<v1 var="String" type="System.String" value="Spell3"/>', b'<v1 var="String" type="System.String" value="11107/Spell3"/>')
                with open(files_fix, 'wb') as file:
                    file.write(text)
                    
        elif ID_SKIN == b'13210':
            with open(files_fix, 'rb') as file:
                text = file.read()
            text = text.replace(b'    </skillCombines>', b'      <Element var="Com" type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">\r\n        <v1 var="String" type="System.UInt32" value="130912"/>\r\n        <v2 var="String" type="System.Int32" value="1"/>\r\n      </Element>\r\n      <Element var="Com" type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">\r\n        <v1 var="String" type="System.UInt32" value="130913"/>\r\n        <v2 var="String" type="System.Int32" value="1"/>\r\n      </Element>\r\n      <Element var="Com" type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">        <v1 var="String" type="System.UInt32" value="130914"/>\r\n        <v2 var="String" type="System.Int32" value="1"/>\r\n      </Element>\r\n    </skillCombines>')
            with open(files_fix, 'wb') as file:
                file.write(text)
                
        elif ID_SKIN == b'59702':
            with open(files_fix, 'rb') as file:
                text = file.read()
            text = text.replace(b'prefab_skill_effects/hero_skill_effects/KuangTie_attack_spell03_1', b'prefab_skill_effects/hero_skill_effects/597_kuangtie/'+ID_SKIN+b'/KuangTie_attack_spell03_1')
            text = text.replace(b'prefab_skill_effects/hero_skill_effects/KuangTie_attack02_spell03_1', b'prefab_skill_effects/hero_skill_effects/597_kuangtie/'+ID_SKIN+b'/KuangTie_attack02_spell03_1')     
            with open(files_fix, 'wb') as file:
                file.write(text)      
                 
        elif ID_SKIN[:3] == b'111':
            with open(files_fix, 'rb') as file:
                text = file.read()
            text = text.replace(b'prefab_skill_effects/hero_skill_effects/T3_Sunshuangxiang_skill_01_attack_01', b'prefab_skill_effects/hero_skill_effects/111_sunshangxiang/'+ID_SKIN+b'/T3_Sunshuangxiang_skill_01_attack_01')
            with open(files_fix, 'wb') as file:
                file.write(text)
        
        elif ID_SKIN in [b'13311', b'16707']:
            with open(files_fix, 'rb') as file:
                text = file.read()
            text = re.sub(re.escape(b"prefab_skill_effects/hero_skill_effects/" + NAME_HERO.encode() + b'/'), b"prefab_skill_effects/component_effects/" + ID_SKIN + b'/' + ID_SKIN + b'_5/', text, flags=re.IGNORECASE)
            with open(files_fix, 'wb') as file:
                file.write(text)
            
    #print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + files_fix, Style.BRIGHT + Fore.GREEN + ' Done!')

def HD_HIEUUNG_AGES(destination_path, NAME_HERO):
    THU_MUC_SKILL =destination_path+'/'+NAME_HERO+'/Skill'
    FILES_XML = [file for file in os.listdir(THU_MUC_SKILL) if file.endswith('.xml')]
    for files in FILES_XML:
        file = THU_MUC_SKILL+'/'+ files
        with open(file, 'rb') as f:
            ds = f.readlines()
        for i in ds:
            if b'prefab_skill_effects' in i.lower():
                im = i.replace(b'" refParamName=""', b'.prefab" refParamName=""').replace(b'_E.prefab"', b'_E"').replace(b'_e.prefab"', b'_e"').replace(b'.prefab.prefab', b'.prefab')
                with open(file, 'rb') as f1:
                    code = f1.read().replace(i,im)
                with open(file, 'wb') as f1:
                    f1.write(code)
def HD_HIEUUNG_FIX_LAG(files_fix):

    with open(files_fix, 'rb') as f:
        ds = f.readlines()
    for i in ds:
        if b'prefab_skill_effects/hero_skill_effects' in i.lower():
            im = i.replace(b'"/>', b'.prefab"/>').replace(b'_E.prefab"', b'_E"').replace(b'_e.prefab"', b'_e"').replace(b'.prefab.prefab', b'.prefab')
            with open(files_fix, 'rb') as f1:
                code = f1.read().replace(i,im)
            with open(files_fix, 'wb') as f1:
                f1.write(code)
def botimskin(file_actor_mod, DANHSACH):
    map1 = 'EX/kb.txt'
    DS_SKIN_MOD = []
    for i in DANHSACH:
        with open(map1, 'rb') as f:
            rpl = f.readlines()
        with open(file_actor_mod, 'rb') as f:
            RPL = f.read()
        i = int(i)
        IDFIND = RPL.find(i.to_bytes(4, 'little') + int(str(i)[:3]).to_bytes(4, 'little'))
        if IDFIND != -1:
            VT = RPL[IDFIND + 12:IDFIND + 31]
            Hero = [x for x in rpl if VT in x and b'[ex]' not in x]
            if len(Hero) == 0:
                Hero = 'Hero: ?'
            else:
                Hero = Hero[0][22:].decode().strip()

            VT = RPL[IDFIND + 40:IDFIND + 59]
            Skin = [x for x in rpl if VT in x and b'[ex]' not in x]
            if len(Skin) == 0:
                Skin = 'Skin: ?'
            else:
                Skin = Skin[0][22:].decode().strip()

            All_find = f"{Hero} {Skin}"
            DS_SKIN_MOD.append(All_find)

    with open('List_Skin.txt', 'a', encoding='utf-8') as file:
        for TT_TEN_SKIN in range(len(DS_SKIN_MOD)):
            LUU_SKIN1 = f"{TT_TEN_SKIN + 1}. {DS_SKIN_MOD[TT_TEN_SKIN]}"
            print(LUU_SKIN1)
            file.write(LUU_SKIN1 + "\n")
def heroskinxml(filename11, option1):

    
    HEADER_BYTES = bytes.fromhex(
        '4D53455307000000F5010000580B00006161616161616161616161616161616161616161616161616161616161616161000000000000000000000000000000005554462D380000000000000000000000000000000000000000000000000000003231666261393832376564343536623733303263346433373633373166396662000000008C00000000000000'
    )
    
    def bytes_to_xml(byte_data):
        xml_elements = []
        i = 0
        while i < len(byte_data):
            try:
                if i + 16 > len(byte_data):
                    break
    
                total_length, skin_id = struct.unpack_from('<I4s', byte_data, i)
                skin_id = int.from_bytes(skin_id, byteorder='little')
    
                if i + total_length + 4 > len(byte_data):
                    break
    
                hero_id = struct.unpack_from('<I4s', byte_data, i + 8)[0]
    
                hero_name_length = struct.unpack_from('<I4s', byte_data, i + 12)[0]
                hero_name_end = i + 16 + hero_name_length - 1
                hero_name = byte_data[i + 16:hero_name_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                skin_number = byte_data[hero_name_end + 1]
    
                skin_name_length = struct.unpack_from('<I', byte_data, i + 40)[0]
                skin_name_end = i + 44 + skin_name_length - 1
                skin_name = byte_data[i + 44:skin_name_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                icon_index_length = struct.unpack_from('<I', byte_data, i + 64)[0]
                icon_index_end = i + 68 + icon_index_length - 1
                icon_index = byte_data[i + 68:icon_index_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                icon_hex_pos = icon_index_end + 1
                icon_hex = struct.unpack_from('<I4s', byte_data, icon_hex_pos)[0]
    
                nothing_01_end = icon_hex_pos + 5 + 108
                nothing_01 = byte_data[icon_hex_pos + 5:nothing_01_end].hex()
    
                bytes_01 = byte_data[nothing_01_end:nothing_01_end + 12].hex()
                bytes_01_end = nothing_01_end + 12
    
                Image_1_length = struct.unpack_from('<I', byte_data, bytes_01_end)[0]
                Image_1_end = bytes_01_end + 4 + Image_1_length
                Image_1 = byte_data[bytes_01_end + 4:Image_1_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                Image_2_length = struct.unpack_from('<I', byte_data, Image_1_end)[0]
                Image_2_end = Image_1_end + 4 + Image_2_length
                Image_2 = byte_data[Image_1_end + 4:Image_2_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                Image_3_length = struct.unpack_from('<I', byte_data, Image_2_end)[0]
                Image_3_end = Image_2_end + 4 + Image_3_length
                Image_3 = byte_data[Image_2_end + 4:Image_3_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                Image_4_length = struct.unpack_from('<I', byte_data, Image_3_end)[0]
                Image_4_end = Image_3_end + 4 + Image_4_length
                Image_4 = byte_data[Image_3_end + 4:Image_4_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_1_length = struct.unpack_from('<I', byte_data, Image_4_end + 4)[0]
                buff_icon_1_end = Image_4_end + 8 + buff_icon_1_length
                buff_icon_1 = byte_data[Image_4_end + 8:buff_icon_1_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_1_length = struct.unpack_from('<I', byte_data, buff_icon_1_end)[0]
                buff_name_1_end = buff_icon_1_end + 4 + buff_name_1_length
                buff_name_1 = byte_data[buff_icon_1_end + 4:buff_name_1_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_2_length = struct.unpack_from('<I', byte_data, buff_name_1_end)[0]
                buff_icon_2_end = buff_name_1_end + 4 + buff_icon_2_length
                buff_icon_2 = byte_data[buff_name_1_end + 4:buff_icon_2_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_2_length = struct.unpack_from('<I', byte_data, buff_icon_2_end)[0]
                buff_name_2_end = buff_icon_2_end + 4 + buff_name_2_length
                buff_name_2 = byte_data[buff_icon_2_end + 4:buff_name_2_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_3_length = struct.unpack_from('<I', byte_data, buff_name_2_end)[0]
                buff_icon_3_end = buff_name_2_end + 4 + buff_icon_3_length
                buff_icon_3 = byte_data[buff_name_2_end + 4:buff_icon_3_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_3_length = struct.unpack_from('<I', byte_data, buff_icon_3_end)[0]
                buff_name_3_end = buff_icon_3_end + 4 + buff_name_3_length
                buff_name_3 = byte_data[buff_icon_3_end + 4:buff_name_3_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_4_length = struct.unpack_from('<I', byte_data, buff_name_3_end)[0]
                buff_icon_4_end = buff_name_3_end + 4 + buff_icon_4_length
                buff_icon_4 = byte_data[buff_name_3_end + 4:buff_icon_4_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_4_length = struct.unpack_from('<I', byte_data, buff_icon_4_end)[0]
                buff_name_4_end = buff_icon_4_end + 4 + buff_name_4_length
                buff_name_4 = byte_data[buff_icon_4_end + 4:buff_name_4_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_5_length = struct.unpack_from('<I', byte_data, buff_name_4_end)[0]
                buff_icon_5_end = buff_name_4_end + 4 + buff_icon_5_length
                buff_icon_5 = byte_data[buff_name_4_end + 4:buff_icon_5_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_5_length = struct.unpack_from('<I', byte_data, buff_icon_5_end)[0]
                buff_name_5_end = buff_icon_5_end + 4 + buff_name_5_length
                buff_name_5 = byte_data[buff_icon_5_end + 4:buff_name_5_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_6_length = struct.unpack_from('<I', byte_data, buff_name_5_end)[0]
                buff_icon_6_end = buff_name_5_end + 4 + buff_icon_6_length
                buff_icon_6 = byte_data[buff_name_5_end + 4:buff_icon_6_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_6_length = struct.unpack_from('<I', byte_data, buff_icon_6_end)[0]
                buff_name_6_end = buff_icon_6_end + 4 + buff_name_6_length
                buff_name_6 = byte_data[buff_icon_6_end + 4:buff_name_6_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_7_length = struct.unpack_from('<I', byte_data, buff_name_6_end)[0]
                buff_icon_7_end = buff_name_6_end + 4 + buff_icon_7_length
                buff_icon_7 = byte_data[buff_name_6_end + 4:buff_icon_7_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_7_length = struct.unpack_from('<I', byte_data, buff_icon_7_end)[0]
                buff_name_7_end = buff_icon_7_end + 4 + buff_name_7_length
                buff_name_7 = byte_data[buff_icon_7_end + 4:buff_name_7_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_8_length = struct.unpack_from('<I', byte_data, buff_name_7_end)[0]
                buff_icon_8_end = buff_name_7_end + 4 + buff_icon_8_length
                buff_icon_8 = byte_data[buff_name_7_end + 4:buff_icon_8_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_8_length = struct.unpack_from('<I', byte_data, buff_icon_8_end)[0]
                buff_name_8_end = buff_icon_8_end + 4 + buff_name_8_length
                buff_name_8 = byte_data[buff_icon_8_end + 4:buff_name_8_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_9_length = struct.unpack_from('<I', byte_data, buff_name_8_end)[0]
                buff_icon_9_end = buff_name_8_end + 4 + buff_icon_9_length
                buff_icon_9 = byte_data[buff_name_8_end + 4:buff_icon_9_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_9_length = struct.unpack_from('<I', byte_data, buff_icon_9_end)[0]
                buff_name_9_end = buff_icon_9_end + 4 + buff_name_9_length
                buff_name_9 = byte_data[buff_icon_9_end + 4:buff_name_9_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                buff_icon_10_length = struct.unpack_from('<I', byte_data, buff_name_9_end)[0]
                buff_icon_10_end = buff_name_9_end + 4 + buff_icon_10_length
                buff_icon_10 = byte_data[buff_name_9_end + 4:buff_icon_10_end].decode('utf-8', errors='ignore').rstrip('\x00')
                buff_name_10_length = struct.unpack_from('<I', byte_data, buff_icon_10_end)[0]
                buff_name_10_end = buff_icon_10_end + 4 + buff_name_10_length
                buff_name_10 = byte_data[buff_icon_10_end + 4:buff_name_10_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                bg_length = struct.unpack_from('<I', byte_data, buff_name_10_end)[0]
                bg_end = buff_name_10_end + 4 + bg_length
                bg = byte_data[buff_name_10_end + 4:bg_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                link_length = struct.unpack_from('<I', byte_data, bg_end)[0]
                link_end = bg_end + 4 + link_length
                link = byte_data[bg_end + 4:link_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                img_yt_length = struct.unpack_from('<I', byte_data, link_end)[0]
                img_yt_end = link_end + 4 + img_yt_length
                img_yt = byte_data[link_end + 4:img_yt_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                abc_length = struct.unpack_from('<I', byte_data, img_yt_end)[0]
                abc_end = img_yt_end + 4 + abc_length
                abc = byte_data[img_yt_end + 4:abc_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                bytes_02 = byte_data[abc_end:(abc_end + 8)].hex()
                bytes_02_end = abc_end + 8
            
                object_length = struct.unpack_from('<I', byte_data, bytes_02_end)[0]
                object_end = bytes_02_end + 4 + object_length
                object = byte_data[bytes_02_end + 4:object_end].decode('utf-8', errors='ignore').rstrip('\x00')
            
                object_01_length = struct.unpack_from('<I', byte_data, object_end)[0]
                object_01_end = object_end + 4 + object_01_length
                object_01 = byte_data[object_end + 4:object_01_end].decode('utf-8', errors='ignore').rstrip('\x00')
            
                object_02_length = struct.unpack_from('<I', byte_data, object_01_end)[0]
                object_02_end = object_01_end + 4 + object_02_length
                object_02 = byte_data[object_01_end + 4:object_02_end].decode('utf-8', errors='ignore').rstrip('\x00')
            
                object_03_length = struct.unpack_from('<I', byte_data, object_02_end)[0]
                object_03_end = object_02_end + 4 + object_03_length
                object_03 = byte_data[object_02_end + 4:object_03_end].decode('utf-8', errors='ignore').rstrip('\x00')
            
                bytes_04 = byte_data[object_03_end:object_03_end + 16].hex()
                pos_start = object_03_end + 16
                pos_index = struct.unpack_from('<I4s', byte_data, pos_start)[0]
                pos_end = pos_start + 16
                bytes_05 = byte_data[pos_start + 4:pos_start + 16].hex()
    
                img_load_length = struct.unpack_from('<I', byte_data, pos_end)[0]
                img_load_end = pos_end + 4 + img_load_length
                img_load = byte_data[pos_end + 4:img_load_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                img_head_length = struct.unpack_from('<I', byte_data, img_load_end)[0]
                img_head_end = img_load_end + 4 + img_head_length
                img_head = byte_data[img_load_end + 4:img_head_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                img_0003_length = struct.unpack_from('<I', byte_data, img_head_end)[0]
                img_0003_end = img_head_end + 4 + img_0003_length
                img_0003 = byte_data[img_head_end + 4:img_0003_end].decode('utf-8', errors='ignore').rstrip('\x00')
    
                bytes_03 = byte_data[img_0003_end:img_0003_end + 12].hex()
                bytes_03_end = img_0003_end + 12
    
                mot_length = struct.unpack_from('<I', byte_data, bytes_03_end)[0]
                mot_end = bytes_03_end + 4 + mot_length
                mot = byte_data[bytes_03_end + 4:mot_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                hai_length = struct.unpack_from('<I', byte_data, mot_end)[0]
                hai_end = mot_end + 4 + hai_length
                hai = byte_data[mot_end + 4:hai_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                imprint_length = struct.unpack_from('<I', byte_data, hai_end)[0]
                imprint_end = hai_end + 4 + imprint_length
                imprint = byte_data[hai_end + 4:imprint_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                json_length = struct.unpack_from('<I', byte_data, imprint_end)[0]
                json_end = imprint_end + 4 + json_length
                json = byte_data[imprint_end + 4:json_end].hex()
    
                track = (
                    '<Track skinId="{}" heroId="{}" skinNumber="{}" icon="{}" iconHex="{}">\n'
                    '    <Name heroName="{}" skinName="{}" />\n'
                    '    <Splash s1="{}" s2="{}" s3="{}" s4="{}" />\n'
                    '    <buff_01 icon="{}" name="{}" />\n'
                    '    <buff_02 icon="{}" name="{}" />\n'
                    '    <buff_03 icon="{}" name="{}" />\n'
                    '    <buff_04 icon="{}" name="{}" />\n'
                    '    <buff_05 icon="{}" name="{}" />\n'
                    '    <buff_06 icon="{}" name="{}" />\n'
                    '    <buff_07 icon="{}" name="{}" />\n'
                    '    <buff_08 icon="{}" name="{}" />\n'
                    '    <buff_09 icon="{}" name="{}" />\n'
                    '    <buff_10 icon="{}" name="{}" />\n'
                    '    <Background path="{}" />\n'
                    '    <Clipyt link="{}" thumbnail="{}" noname="{}" />\n'
                    '    <Object a="{}" b="{}" c="{}" d="{}" />\n'
                    '    <Int posIndex="{}" />\n'
                    '    <Image imgLoad="{}" imgHead="{}" img0003="{}" />\n'
                    '    <Bytes nothing_01="{}" bytes_01="{}" bytes_02="{}" bytes_03="{}" bytes_04="{}" bytes_05="{}" />\n'
                    '    <More mot="{}" hai="{}" />\n'
                    '    <Imprint path="{}" />\n'
                    '    <Choose json="{}" />\n'
                    '</Track>'
                    
                ).format(skin_id, hero_id, skin_number, icon_index, icon_hex, hero_name, skin_name, Image_1, Image_2, Image_3, Image_4,
                         buff_icon_1, buff_name_1, buff_icon_2, buff_name_2, buff_icon_3, buff_name_3, buff_icon_4, buff_name_4,
                         buff_icon_5, buff_name_5, buff_icon_6, buff_name_6, buff_icon_7, buff_name_7, buff_icon_8, buff_name_8,
                         buff_icon_9, buff_name_9, buff_icon_10, buff_name_10,
                         bg, link, img_yt, abc, object, object_01, object_02, object_03, pos_index,
                         img_load, img_head, img_0003, nothing_01, bytes_01, bytes_02, bytes_03, bytes_04, bytes_05,
                         mot, hai, imprint, json)
                xml_elements.append(track)
                
                i += total_length + 4
    
            except struct.error as e:
                print(f"Lỗi giải nén tại vị trí {i}: {e}")
                break
    
        return '\n\n'.join(xml_elements)
    
    def int_to_bytes(value, length):
        return value.to_bytes(length, byteorder='little')
    
    def save_xml_from_bytes(file_path):
        with open(file_path, 'rb') as file:
            byte_content = file.read()
    
        xml_content = bytes_to_xml(byte_content[140:])
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(xml_content)
    
    
    def xml_to_bytes(xml_str):
        xml_str = xml_str.replace('&', '1')
        byte_data = bytearray()
        root = ET.ElementTree(ET.fromstring(f'<root>{xml_str}</root>')).getroot()
        last_total_length = 0
        for track in root:
            skin_id = int(track.attrib['skinId'])
            hero_id = int(track.attrib['heroId'])
            hero_name = track.find('Name').attrib['heroName']
            skin_number = int(track.attrib['skinNumber'])
            skin_name = track.find('Name').attrib['skinName']
            icon_index = track.attrib['icon']
            icon_hex = int(track.attrib['iconHex'])
            
            a1 = track.find('Splash').attrib['s1']
            a2 = track.find('Splash').attrib['s2']
            a3 = track.find('Splash').attrib['s3']
            a4 = track.find('Splash').attrib['s4']
            
            buff_icon_1 = track.find('buff_01').attrib['icon']
            buff_name_1 = track.find('buff_01').attrib['name']
    
            buff_icon_2 = track.find('buff_02').attrib['icon']
            buff_name_2 = track.find('buff_02').attrib['name']
    
            buff_icon_3 = track.find('buff_03').attrib['icon']
            buff_name_3 = track.find('buff_03').attrib['name']
            
            buff_icon_4 = track.find('buff_04').attrib['icon']
            buff_name_4 = track.find('buff_04').attrib['name']
    
            buff_icon_5 = track.find('buff_05').attrib['icon']
            buff_name_5 = track.find('buff_05').attrib['name']
    
            buff_icon_6 = track.find('buff_06').attrib['icon']
            buff_name_6 = track.find('buff_06').attrib['name']
    
            buff_icon_7 = track.find('buff_07').attrib['icon']
            buff_name_7 = track.find('buff_07').attrib['name']
    
            buff_icon_8 = track.find('buff_08').attrib['icon']
            buff_name_8 = track.find('buff_08').attrib['name']
    
            buff_icon_9 = track.find('buff_09').attrib['icon']
            buff_name_9 = track.find('buff_09').attrib['name']
    
            buff_icon_10 = track.find('buff_10').attrib['icon']
            buff_name_10 = track.find('buff_10').attrib['name']
            
            background = track.find('Background').attrib['path']
            link = track.find('Clipyt').attrib['link']
            thumbnail = track.find('Clipyt').attrib['thumbnail']
            noname = track.find('Clipyt').attrib['noname']
            
            object = track.find('Object').attrib['a']
            object_01 = track.find('Object').attrib['b']
            object_02 = track.find('Object').attrib['c']
            object_03 = track.find('Object').attrib['d']
            
            posIndex = int(track.find('Int').attrib['posIndex'])
            
            imgLoad = track.find('Image').attrib['imgLoad']
            imgHead = track.find('Image').attrib['imgHead']
            img0003 = track.find('Image').attrib['img0003']
    
            nothing_01 = bytes.fromhex(track.find('Bytes').attrib['nothing_01'])
            bytes_01 = bytes.fromhex(track.find('Bytes').attrib['bytes_01'])
            bytes_02 = bytes.fromhex(track.find('Bytes').attrib['bytes_02'])
            bytes_03 = bytes.fromhex(track.find('Bytes').attrib['bytes_03'])
            bytes_04 = bytes.fromhex(track.find('Bytes').attrib['bytes_04'])
            bytes_05 = bytes.fromhex(track.find('Bytes').attrib['bytes_05'])
            
            mot = track.find('More').attrib['mot']
            hai = track.find('More').attrib['hai']
            imprint = track.find('Imprint').attrib['path']
            json = bytes.fromhex(track.find('Choose').attrib['json'])
           
            total_valid_attributes = sum(
                1 for i in range(1, 11)
                if any(track.find(f'./buff_{i:02d}').attrib.get(attr) for attr in ['icon', 'name'])
            )
            valid_buff_count = total_valid_attributes
    
            hero_name_length = len(hero_name) + 1
            skin_name_length = len(skin_name) + 1
            icon_index_length = len(icon_index) + 1
            
            a1_length = len(a1) + 1
            a2_length = len(a2) + 1
            a3_length = len(a3) + 1
            a4_length = len(a4) + 1
            
            buff_icon_1_length = len(buff_icon_1) + 1
            buff_name_1_length = len(buff_name_1) + 1
            buff_icon_2_length = len(buff_icon_2) + 1
            buff_name_2_length = len(buff_name_2) + 1
            buff_icon_3_length = len(buff_icon_3) + 1
            buff_name_3_length = len(buff_name_3) + 1
            buff_icon_4_length = len(buff_icon_4) + 1
            buff_name_4_length = len(buff_name_4) + 1
            buff_icon_5_length = len(buff_icon_5) + 1
            buff_name_5_length = len(buff_name_5) + 1
            buff_icon_6_length = len(buff_icon_6) + 1
            buff_name_6_length = len(buff_name_6) + 1
            buff_icon_7_length = len(buff_icon_7) + 1
            buff_name_7_length = len(buff_name_7) + 1
            buff_icon_8_length = len(buff_icon_8) + 1
            buff_name_8_length = len(buff_name_8) + 1
            buff_icon_9_length = len(buff_icon_9) + 1
            buff_name_9_length = len(buff_name_9) + 1
            buff_icon_10_length = len(buff_icon_10) + 1
            buff_name_10_length = len(buff_name_10) + 1
            
            link_length = len(link) + 1
            thumbnail_length = len(thumbnail) + 1
            noname_length = len(noname) + 1
            
            background_length = len(background) + 1
            object_length = len(object) + 1
            object_01_length = len(object_01) + 1
            object_02_length = len(object_02) + 1
            object_03_length = len(object_03) + 1
            imgLoad_length = len(imgLoad) + 1
            imgHead_length = len(imgHead) + 1
            img0003_length = len(img0003) + 1
            mot_length = len(mot) + 1
            hai_length = len(hai) + 1
            imprint_length = len(imprint) + 1
            json_length = len(json)
            
            total_length = (20 + 8 + 130 + 12 + 8 + 96 + 8 + 35 + 16 + 28 +
                            hero_name_length + skin_name_length + icon_index_length +
                            a1_length + a2_length + a3_length + a4_length + 
                            buff_icon_1_length + buff_name_1_length + buff_icon_2_length + buff_name_2_length + 
                            buff_icon_3_length + buff_name_3_length + buff_icon_4_length + buff_name_4_length + 
                            buff_icon_5_length + buff_name_5_length + buff_icon_6_length + buff_name_6_length + 
                            buff_icon_7_length + buff_name_7_length + buff_icon_8_length + buff_name_8_length + 
                            buff_icon_9_length + buff_name_9_length + buff_icon_10_length + buff_name_10_length + 
                            link_length + thumbnail_length + noname_length + background_length +
                            object_length + object_01_length + object_02_length + object_03_length + 
                            imgLoad_length + imgHead_length + img0003_length + mot_length + hai_length + imprint_length + json_length)
    
            byte_data.extend(struct.pack('<I', total_length))
            byte_data.extend(skin_id.to_bytes(4, byteorder='little'))
            byte_data.extend(hero_id.to_bytes(4, byteorder='little'))
            byte_data.extend(struct.pack('<I', hero_name_length))
            byte_data.extend(hero_name.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', skin_number))
            byte_data.extend(struct.pack('<I', skin_name_length))
            byte_data.extend(skin_name.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', icon_index_length))
            byte_data.extend(icon_index.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', icon_hex))
            byte_data.append(0)
            byte_data.extend(nothing_01)
            byte_data.extend(bytes_01)
            
            byte_data.extend(struct.pack('<I', a1_length))
            byte_data.extend(a1.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', a2_length))
            byte_data.extend(a2.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', a3_length))
            byte_data.extend(a3.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', a4_length))
            byte_data.extend(a4.encode('utf-8') + b'\x00')
            
            byte_data.extend(struct.pack('<I', valid_buff_count))
            
            byte_data.extend(struct.pack('<I', buff_icon_1_length))
            byte_data.extend(buff_icon_1.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_1_length))
            byte_data.extend(buff_name_1.encode('utf-8') + b'\x00')
            
            byte_data.extend(struct.pack('<I', buff_icon_2_length))
            byte_data.extend(buff_icon_2.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_2_length))
            byte_data.extend(buff_name_2.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_3_length))
            byte_data.extend(buff_icon_3.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_3_length))
            byte_data.extend(buff_name_3.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_4_length))
            byte_data.extend(buff_icon_4.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_4_length))
            byte_data.extend(buff_name_4.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_5_length))
            byte_data.extend(buff_icon_5.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_5_length))
            byte_data.extend(buff_name_5.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_6_length))
            byte_data.extend(buff_icon_6.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_6_length))
            byte_data.extend(buff_name_6.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_7_length))
            byte_data.extend(buff_icon_7.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_7_length))
            byte_data.extend(buff_name_7.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_8_length))
            byte_data.extend(buff_icon_8.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_8_length))
            byte_data.extend(buff_name_8.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_9_length))
            byte_data.extend(buff_icon_9.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_9_length))
            byte_data.extend(buff_name_9.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', buff_icon_10_length))
            byte_data.extend(buff_icon_10.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', buff_name_10_length))
            byte_data.extend(buff_name_10.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', background_length))
            byte_data.extend(background.encode('utf-8') + b'\x00')
    
            byte_data.extend(struct.pack('<I', link_length))
            byte_data.extend(link.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', thumbnail_length))
            byte_data.extend(thumbnail.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', noname_length))
            byte_data.extend(noname.encode('utf-8') + b'\x00')
            
            byte_data.extend(bytes_02)
            
            byte_data.extend(struct.pack('<I', object_length))
            byte_data.extend(object.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', object_01_length))
            byte_data.extend(object_01.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', object_02_length))
            byte_data.extend(object_02.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', object_03_length))
            byte_data.extend(object_03.encode('utf-8') + b'\x00')
            
            byte_data.extend(bytes_04)
            byte_data.extend(struct.pack('<I', posIndex))
            byte_data.extend(bytes_05)
            
            byte_data.extend(struct.pack('<I', imgLoad_length))
            byte_data.extend(imgLoad.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', imgHead_length))
            byte_data.extend(imgHead.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', img0003_length))
            byte_data.extend(img0003.encode('utf-8') + b'\x00')
            
            byte_data.extend(bytes_03)
            
            byte_data.extend(struct.pack('<I', mot_length))
            byte_data.extend(mot.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', hai_length))
            byte_data.extend(hai.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', imprint_length))
            byte_data.extend(imprint.encode('utf-8') + b'\x00')
            byte_data.extend(struct.pack('<I', json_length))
            byte_data.extend(json)
            last_total_length = total_length
    
        final_total_length = last_total_length + 4  # Including the length of the last total length
    
        total_tracks = len(root)  # Total number of tracks
    
        return bytes(byte_data), final_total_length, total_tracks
    
    def is_utf8(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file.read()
            return True
        except UnicodeDecodeError:
            return False
    
    def generate_header_bytes(final_total_length, total_tracks, byte_content):
        header_bytes = bytearray.fromhex(
            '4D5345530700000000000000000000006161616161616161616161616161616161616161616161616161616161616161000000000000000000000000000000005554462D380000000000000000000000000000000000000000000000000000003838653064656464636165663833333762656433363464343937343436626561000000008C00000000000000'
        )
        
        header_bytes[8:12] = int_to_bytes(final_total_length, 4)
        header_bytes[12:16] = int_to_bytes(total_tracks, 4)
        
        md5_hash = hashlib.md5(byte_content).hexdigest().encode('utf-8')
        header_bytes[96:128] = md5_hash[:32]
        
        return bytes(header_bytes)

    def process_file(file_path, option):
        if option == 1:  
            save_xml_from_bytes(file_path)
        elif option == 2:  
            if is_utf8(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    xml_content = file.read()
                byte_content, final_total_length, total_tracks = xml_to_bytes(xml_content)
                header_bytes = generate_header_bytes(final_total_length, total_tracks, byte_content)
                with open(file_path, 'wb') as file:
                    file.write(header_bytes + byte_content)
    filename1 = filename11
    option = option1
    process_file(filename1, option)

def heroskinshopxml(file_path, option):
    def bytes_to_xml(byte_data):
        xml_elements = []
        i = 0
        while i < len(byte_data):
            try:
                total_length, skin_id = struct.unpack_from('<I4s', byte_data, i)
                skin_id = int.from_bytes(skin_id, byteorder='little')
                hero_id = struct.unpack_from('<I', byte_data, i + 8)[0]
                            
                text_1_length = struct.unpack_from('<I', byte_data, i + 12)[0]
                text_1_end = i + 16 + text_1_length
                text_1 = byte_data[i + 16:text_1_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                skin_number = struct.unpack_from('<I', byte_data, text_1_end)[0]
                
                text_2_length = struct.unpack_from('<I', byte_data, text_1_end + 4)[0]
                text_2_end = text_1_end + 8 + text_2_length
                text_2 = byte_data[text_1_end + 8:text_2_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                text_3_length = struct.unpack_from('<I', byte_data, text_2_end)[0]
                text_3_end = text_2_end + 4 + text_3_length
                text_3 = byte_data[text_2_end + 4:text_3_end].decode('utf-8', errors='ignore').rstrip('\x00')

                byte_2 = byte_data[text_3_end:text_3_end + 1].hex()
                
                text_4_length = struct.unpack_from('<I', byte_data, text_3_end + 1)[0]
                text_4_end = text_3_end + 5 + text_4_length
                text_4 = byte_data[text_3_end + 5:text_4_end].decode('utf-8', errors='ignore').rstrip('\x00')

                text_5_length = struct.unpack_from('<I', byte_data, text_4_end)[0]
                text_5_end = text_4_end + 4 + text_5_length
                text_5 = byte_data[text_4_end + 4:text_5_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                text_6_length = struct.unpack_from('<I', byte_data, text_5_end)[0]
                text_6_end = text_5_end + 4 + text_6_length
                text_6 = byte_data[text_5_end + 4:text_6_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                byte_3 = byte_data[text_6_end:text_6_end + 2].hex()
                
                text_7_length = struct.unpack_from('<I', byte_data, text_6_end + 2)[0]
                text_7_end = text_6_end + 6 + text_7_length
                text_7 = byte_data[text_6_end + 6:text_7_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                byte_4 = byte_data[text_7_end:text_7_end + 51].hex()
                byte_4_end = text_7_end + 51
                
                text_8_length = struct.unpack_from('<I', byte_data, byte_4_end)[0]
                text_8_end = byte_4_end + 4 + text_8_length
                text_8 = byte_data[byte_4_end + 4:text_8_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                text_9_length = struct.unpack_from('<I', byte_data, text_8_end)[0]
                text_9_end = text_8_end + 4 + text_9_length
                text_9 = byte_data[text_8_end + 4:text_9_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                byte_5 = byte_data[text_9_end:text_9_end + 64].hex()
                byte_5_end = text_9_end + 64

                text_10_length = struct.unpack_from('<I', byte_data, byte_5_end)[0]
                text_10_end = byte_5_end + 4 + text_10_length
                text_10 = byte_data[byte_5_end + 4:text_10_end].decode('utf-8', errors='ignore').rstrip('\x00')
                
                daubuoi = i + total_length + 4
                byte_6 = byte_data[text_10_end:daubuoi].hex()

                track = (
                    '<Track\n'
                    '    SkinId="{}"\n'
                    '    HeroId="{}"\n'
                    '    SkinNumber="{}"\n'
                    '    T1="{}"\n'
                    '    T2="{}"\n'
                    '    T3="{}"\n'                
                    '    T4="{}"\n'
                    '    T5="{}"\n'
                    '    T6="{}"\n'                
                    '    T7="{}"\n'
                    '    T8="{}"\n'
                    '    T9="{}"\n'                
                    '    T10="{}"\n'                
                    '    B2="{}"\n'                
                    '    B3="{}"\n'                
                    '    B4="{}"\n'                
                    '    B5="{}"\n'                
                    '    B6="{}"/>\n'                
                ).format(skin_id, hero_id, skin_number, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10, byte_2, byte_3, byte_4, byte_5, byte_6)
                xml_elements.append(track)

                i = daubuoi
            except struct.error:
                break

        return '\n\n'.join(xml_elements)

    def save_xml_from_bytes(file_path):
        try:
            with open(file_path, 'rb') as file:
                byte_content = file.read()

            xml_content = bytes_to_xml(byte_content[140:])
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(xml_content)
        except FileNotFoundError:
            print("Error", f"File không tồn tại: {file_path}", "red")
        except Exception as e:
            print("Error", f"Lỗi khi chuyển đổi {file_path}: {e}", "red")

    def xml_to_bytes(xml_str):
        xml_str = xml_str.replace('&', '1')
        byte_data = bytearray()
        root = ET.ElementTree(ET.fromstring(f'<root>{xml_str}</root>')).getroot()
        last_total_length = 0 
        total_tracks = len(root)  

        for track in root:
            skin_id = int(track.attrib['SkinId'])
            hero_id = int(track.attrib['HeroId'])
            text_1 = track.attrib['T1']
            skin_number = int(track.attrib['SkinNumber'])
            text_2 = track.attrib['T2']
            text_3 = track.attrib['T3']
            text_4 = track.attrib['T4']
            text_5 = track.attrib['T5']
            text_6 = track.attrib['T6']
            text_7 = track.attrib['T7']
            text_8 = track.attrib['T8']
            text_9 = track.attrib['T9']
            text_10 = track.attrib['T10']
            byte_2 = bytes.fromhex(track.attrib['B2'])
            byte_3 = bytes.fromhex(track.attrib['B3'])
            byte_4 = bytes.fromhex(track.attrib['B4'])
            byte_5 = bytes.fromhex(track.attrib['B5'])
            byte_6 = bytes.fromhex(track.attrib['B6'])
            
            text_1_encoded = text_1.encode('utf-8')
            text_2_encoded = text_2.encode('utf-8')
            text_3_encoded = text_3.encode('utf-8')
            text_4_encoded = text_4.encode('utf-8')
            text_5_encoded = text_5.encode('utf-8')
            text_6_encoded = text_6.encode('utf-8')
            text_7_encoded = text_7.encode('utf-8')
            text_8_encoded = text_8.encode('utf-8')
            text_9_encoded = text_9.encode('utf-8')
            text_10_encoded = text_10.encode('utf-8')
            
            text_1_length = len(text_1_encoded) + 1
            text_2_length = len(text_2_encoded) + 1
            text_3_length = len(text_3_encoded) + 1
            text_4_length = len(text_4_encoded) + 1
            text_5_length = len(text_5_encoded) + 1
            text_6_length = len(text_6_encoded) + 1
            text_7_length = len(text_7_encoded) + 1
            text_8_length = len(text_8_encoded) + 1
            text_9_length = len(text_9_encoded) + 1
            text_10_length = len(text_10_encoded) + 1
            byte_6_length = len(byte_6)
            
            total_length = 16 + text_1_length + text_2_length + text_3_length + text_4_length + text_5_length + text_6_length + text_7_length + text_8_length + text_9_length + text_10_length + 40 + 64 + 50 + byte_6_length
            
            byte_data.extend(int_to_bytes(total_length, 4))
            byte_data.extend(int_to_bytes(skin_id, 4))
            byte_data.extend(int_to_bytes(hero_id, 4))
            byte_data.extend(int_to_bytes(text_1_length, 4))
            byte_data.extend(text_1_encoded + b'\x00')
            byte_data.extend(int_to_bytes(skin_number, 4))
            byte_data.extend(int_to_bytes(text_2_length, 4))
            byte_data.extend(text_2_encoded + b'\x00')
            byte_data.extend(int_to_bytes(text_3_length, 4))
            byte_data.extend(text_3_encoded + b'\x00')
            byte_data.extend(byte_2)
            byte_data.extend(int_to_bytes(text_4_length, 4))
            byte_data.extend(text_4_encoded + b'\x00')
            byte_data.extend(int_to_bytes(text_5_length, 4))
            byte_data.extend(text_5_encoded + b'\x00')
            byte_data.extend(int_to_bytes(text_6_length, 4))
            byte_data.extend(text_6_encoded + b'\x00')
            byte_data.extend(byte_3)
            byte_data.extend(int_to_bytes(text_7_length, 4))
            byte_data.extend(text_7_encoded + b'\x00')
            byte_data.extend(byte_4)
            byte_data.extend(int_to_bytes(text_8_length, 4))
            byte_data.extend(text_8_encoded + b'\x00')
            byte_data.extend(int_to_bytes(text_9_length, 4))
            byte_data.extend(text_9_encoded + b'\x00')
            byte_data.extend(byte_5)
            byte_data.extend(int_to_bytes(text_10_length, 4))
            byte_data.extend(text_10_encoded + b'\x00')
            byte_data.extend(byte_6)

            last_total_length = total_length  

        final_total_length = last_total_length + 4
        
        return bytes(byte_data), final_total_length, total_tracks

    def int_to_bytes(value, length):
        return value.to_bytes(length, byteorder='little')

    def is_utf8(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file.read()
            return True
        except UnicodeDecodeError:
            return False

    def generate_header_bytes(final_total_length, total_tracks, byte_content):
        header_bytes = bytearray.fromhex(
            '4D5345530700000000000000000000006161616161616161616161616161616161616161616161616161616161616161000000000000000000000000000000005554462D380000000000000000000000000000000000000000000000000000003838653064656464636165663833333762656433363464343937343436626561000000008C00000000000000'
        )
        
        header_bytes[8:12] = int_to_bytes(final_total_length, 4)
        header_bytes[12:16] = int_to_bytes(total_tracks, 4)
        
        md5_hash = hashlib.md5(byte_content).hexdigest().encode('utf-8')
        header_bytes[96:128] = md5_hash
        
        return bytes(header_bytes)

    def process_file(file_path, option):
        if option == 1:  
            save_xml_from_bytes(file_path)
        elif option == 2:  
            if is_utf8(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        xml_content = file.read()
                    byte_content, final_total_length, total_tracks = xml_to_bytes(xml_content)
                    header_bytes = generate_header_bytes(final_total_length, total_tracks, byte_content)
                    with open(file_path, 'wb') as file:
                        file.write(header_bytes + byte_content)
                except FileNotFoundError:
                    print("Error", f"File {file_path} không tồn tại", "red")
                except Exception as e:
                    print("Error", f"Lỗi khi chuyển đổi {file_path}: {e}", "red")
    process_file(file_path, option)
def hieuungvethan(ID_SKIN, OganSkin):
	ID = ID_SKIN
	file = open(OganSkin, "rb")
	IDN = str(hex(int(ID)))
	IDN = IDN[4:6] + IDN[2:4]
	IDN = bytes.fromhex(IDN)
	ALL_ID = []
	MD = int(ID[0:3] + "00")
	for IDNew in range(21):
		ALL_ID.append(str(MD))
		MD += 1
	ALL_ID.remove(ID)
	for x in range(20):
		IDK = str(hex(int(ALL_ID[x])))
		IDK = IDK[4:6] + IDK[2:4]
		IDK = bytes.fromhex(IDK)
		ALL_ID[x] = IDK
	Begin = file.read(140)
	Read = b"\x00"
	All = []
	while Read != b"":
		Read = file.read(36)
		if Read.find(IDN) != -1:
			All.append(Read)
		try:
			Max = Read[4] + (Read[5]*256)
			Max0 = str(hex(Max))
			if len(Max0) == 4:
				Max0 = Max0[2:4] + "00"
			if len(Max0) == 5:
				Max0 = Max0[3:5] + "0" + Max0[2]
			if len(Max0) == 6:
				Max0 = Max0[4:6] + Max0[2:4]
			Max0 = bytes.fromhex(Max0)
		except:
			None
	file.close()
	file = open(OganSkin, "ab+")
	Read0 = file.read()
	for i in range(len(ALL_ID)):
		for j in range(len(All)):
			CT = All[j]
			if CT.find(IDN) != -1:
				CT = CT.replace(IDN,ALL_ID[i])
			else:
				CT = CT.replace(ALL_ID[i-1],ALL_ID[i])
			CTN = str(hex(Max0[0]+(Max0[1]*256)+1))
			if len(CTN) == 4:
				CTN = CTN[2:4]
			if len(CTN) == 5:
				CTN = CTN[3:5] + "0" + CTN[2]
			if len(CTN) == 6:
				CTN = CTN[4:6] + CTN[2:4]
			CTN = bytes.fromhex(CTN)
			OZ = b" \x00\x00\x00"
			if len(CTN) == 1:
				CT = CT.replace(OZ+CT[4:6],OZ+CTN+b"\x00",1)
			if len(CTN) == 2:
				CT = CT.replace(OZ+CT[4:6],OZ+CTN,1)
			All[j] = CT
			XXX = file.write(CT)
			Max0 = CT[4:6]
	file.close()
	file = open(OganSkin, "rb")
	Read = file.read()
	Read = Read.replace(Begin[12:14],Max0,1)
	file.close()
	file = open(OganSkin, "wb")
	Z = file.write(Read)
	file.close()

	print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + "OganSkin", Style.BRIGHT + Fore.GREEN + ' Done!')
def modmatinfo(ID_SKIN, files):
    ID_SKIN = ID_SKIN.encode()
    with open (files, 'rb') as f:
        code = f.readlines()
    for i in code:
        if b'prefab_skill_effects' in i.lower():
            i1 = i.split(b'/')
            if len(i1) == 5:
                i2 = i.replace(i1[2], i1[2]+b'/'+ID_SKIN)
                with open (files, 'rb') as f:
                    code = f.read().replace(i, i2)
                with open (files, 'wb') as f:
                    f.write(code)
            if len(i1) == 6:
                i2 = i.replace(i1[3], ID_SKIN)
                with open (files, 'rb') as f:
                    code = f.read().replace(i, i2)
                with open (files, 'wb') as f:
                    f.write(code)
def modvien(ID_SKIN, HeadImage, HeadID):
    with open ('FILES_CODE/vien.xml', 'rb') as f:
        dk = f.readlines()
    with open ('FILES_CODE/vien.xml', 'rb') as f:
        dk2 =f.read()
    if ID_SKIN.encode() in dk2:
        for idvien in dk:
            if ID_SKIN.encode() in idvien:
                inp=HeadImage
                with open(inp,'rb') as f:
                    ab=f.read()
                a=bytes.fromhex('0000'+str(idvien.decode()[8:-2])+'0000')
                i=ab.find(a)-2
                vt=ab[i:i+2]
                vtr=int.from_bytes(vt,byteorder='little')
                vt1=ab[i:i+vtr]
                id2='000065000000'
                a1=bytes.fromhex(str(id2))
                f.close()
                i1=ab.find(a1)-2
                vt11=ab[i1:i1+2]
                vtr1=int.from_bytes(vt11,byteorder='little')
                vt2=ab[i1:i1+vtr1]
                vt1=vt1.replace(a,a1)
                vt11=ab.replace(vt2,vt1)
                with open(inp,'wb') as go:
                    go.write(vt11)
                print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.CYAN + "HeadImage đã mod !", Style.BRIGHT + Fore.GREEN + ' Done!')
    else:
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.CYAN + "HeadImage chưa mod !", Style.BRIGHT + Fore.RED + ' ID Not Found!')
            
    with open ('FILES_CODE/avatar.xml', 'rb') as f:
        dk = f.readlines()
    with open ('FILES_CODE/avatar.xml', 'rb') as f:
        dk2 =f.read()
    if ID_SKIN.encode() in dk2:
        for idvien in dk:
            if ID_SKIN.encode() in idvien:
                inp=HeadID
                with open(inp,'rb') as f:
                    ab=f.read()
                a=bytes.fromhex('0000'+str(idvien.decode()[8:-2])+'0000')
                i=ab.find(a)-2
                vt=ab[i:i+2]
                vtr=int.from_bytes(vt,byteorder='little')
                vt1=ab[i:i+vtr]
                id2='000069000000'
                a1=bytes.fromhex(str(id2))
                f.close()
                i1=ab.find(a1)-2
                vt11=ab[i1:i1+2]
                vtr1=int.from_bytes(vt11,byteorder='little')
                vt2=ab[i1:i1+vtr1]
                vt1=vt1.replace(a,a1)
                vt11=ab.replace(vt2,vt1)
                with open(inp,'wb') as go:
                    go.write(vt11)
                print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.CYAN + "HeadID đã mod !", Style.BRIGHT + Fore.GREEN + ' Done!')
    else:
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.CYAN + "HeadID chưa mod !", Style.BRIGHT + Fore.RED + ' ID Not Found!')
            
def xoacharacter(ID_SKIN, file_mod_Character):
    with open(file_mod_Character, 'rb') as file:
        fct = file.read()
    with open(file_mod_Character, 'rb') as file:
        ktr = file.read()
    user_input = ID_SKIN
    fpr = []
    Codeskdtb = fct
    for i in range(10500, 20000):
        if Codeskdtb.find(i.to_bytes(4, 'little')) != -1:
            fpr.append(str(i))
    for i in range(50100, 54899):
        if Codeskdtb.find(i.to_bytes(4, 'little')) != -1:
            fpr.append(str(i))
    rlvpt = [ptn for ptn in fpr if user_input[:3] in ptn[:3]]
    if rlvpt:
        ftpt = rlvpt[0]
        count = 0
        total = 0
        numrlvt = len(rlvpt)
        for ptn in rlvpt:
            count += fct.count(int(ptn).to_bytes(4, 'little'))
        stpsto = fct.find(int(ftpt).to_bytes(4, 'little')) - 155
        stpt = fct[stpsto:stpsto+4]
        stptvl = int.from_bytes(stpt, 'little')
        stpt = fct[stpsto:stpsto+stptvl+4]
        fcskdt = b''
        la = b'\x00'
        while True:
            dem = b''
            stpt = fct[stpsto:stpsto+4]
            stptvl = int.from_bytes(stpt, 'little')
            stpt = fct[stpsto:stpsto+stptvl+4]
            remic = fct[stptvl+4:]
            fct = remic
            for ptn in rlvpt:
                if stpt.find(int(ptn).to_bytes(4, 'little')) == -1:
                    dem += la
            if len(dem) == numrlvt:
                break
            fcskdt += stpt
        fcskdt = Codeskdtb.replace(fcskdt, b'')
        with open(file_mod_Character, 'wb') as file:
            file.write(fcskdt)
    with open(file_mod_Character, 'rb') as file:
        ktr1 = file.read()
    if ktr != ktr1:
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + "XOACHARACTER !", Style.BRIGHT + Fore.GREEN + ' Done!')
    else:
        print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + "XOACHARACTER !", Style.BRIGHT + Fore.RED + ' ID Not Found!')

def moddeskins(destination_path, NAME_HERO):
    LIST_CODE = []

    THU_MUC_SKILL =destination_path+'/'+NAME_HERO+'/Skill/'
    FILES_XML = [file for file in os.listdir(THU_MUC_SKILL) if file.endswith('.xml')]
    for filesxml in FILES_XML:
        filesxml = THU_MUC_SKILL + filesxml
        with open(filesxml, 'rb') as f:
            code = f.readlines()
        for eff in code:
            if b'hero_skill_effects' in eff:
                if eff not in LIST_CODE:

                    eff1 = eff.replace(b'useRefParam="false" />', b'useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>')
                    with open(filesxml, 'rb') as f:
                        code1 = f.read().replace(eff, eff1)
                    with open(filesxml, 'wb') as f:
                        f.write(code1)
                    LIST_CODE.append(eff)

def dkgtbv(ID_SKIN, Huanhua):
    with open(Huanhua, 'rb') as f:
        ab = f.read()
    ID_1 = ID_SKIN
    DINH_DANG_1 = hex(int(ID_1))[2:]
    if len(DINH_DANG_1) % 2 != 0:
        DINH_DANG_1 = '0' + DINH_DANG_1
    DINH_DANG_1 = DINH_DANG_1[-2:] + DINH_DANG_1[-4:-2]
    DINH_DANG_1 = bytes.fromhex(DINH_DANG_1)
    DINH_DANG_1 = b'\x00\x00' + DINH_DANG_1 + b'\x00\x00'
    a = DINH_DANG_1
    i = ab.find(a) - 2
    vt = ab[i:i+2]
    vtr = int.from_bytes(vt, byteorder='little') + 4
    vt1 = ab[i:i+vtr]
    DKMBVGT = vt1
    DDSKM = DINH_DANG_1
    return DKMBVGT, DDSKM
    
import xml.etree.ElementTree as ET
from colorama import Fore, Style

has_run = False

def update_junglemark_xml(junglemark_path):
    global has_run
    if has_run:
        #print(Style.BRIGHT + Fore.RED + "Hàm đã chạy trước đó. Không thực hiện lại!")
        return

    try:
        tree = ET.parse(junglemark_path)
        root = tree.getroot()

        new_tracks = ET.Element('Track', {
            'trackName': 'HAYMOD',
            'eventType': 'SetCameraHeightDuration',
            'guid': 'TK97Y5-RTX360-FK0B91-B208',
            'enabled': 'true',
            'useRefParam': 'false',
            'refParamName': '',
            'r': '0.000',
            'g': '0.000',
            'b': '0.000',
            'execOnForceStopped': 'false',
            'execOnActionCompleted': 'false',
            'stopAfterLastEvent': 'true'
        })

        new_event = ET.Element('Event', {
            'eventName': 'SetCameraHeightDuration',
            'time': '0.000',
            'length': '1.000',
            'isDuration': 'true',
            'guid': 'TK97Y5-RTX360-FK0B91-B208'
        })

        ET.SubElement(new_event, 'int', {'name': 'slerpTick', 'value': '0', 'refParamName': '', 'useRefParam': 'false'})
        ET.SubElement(new_event, 'float', {'name': 'heightRate', 'value': '1.5', 'refParamName': '', 'useRefParam': 'false'})
        ET.SubElement(new_event, 'bool', {'name': 'bOverride', 'value': 'true', 'refParamName': '', 'useRefParam': 'false'})
        ET.SubElement(new_event, 'bool', {'name': 'leftTimeSlerpBack', 'value': 'true', 'refParamName': '', 'useRefParam': 'false'})
        ET.SubElement(new_event, 'String', {'name': 'refParamName', 'value': '', 'refParamName': '', 'useRefParam': 'false'})

        new_tracks.append(new_event)

        new_track_msg = ET.Element('Track', {
            'trackName': 'HAYMOD',
            'eventType': 'InBattleMsgSendTick',
            'guid': 'TK97Y5-RTX360-FK0B91-B208',
            'enabled': 'true',
            'useRefParam': 'false',
            'refParamName': '',
            'r': '0.000',
            'g': '0.000',
            'b': '0.000',
            'execOnForceStopped': 'false',
            'execOnActionCompleted': 'false',
            'stopAfterLastEvent': 'true'
        })

        new_event_msg = ET.Element('Event', {
            'eventName': 'InBattleMsgSendTick',
            'time': '0.000',
            'isDuration': 'false',
            'guid': 'TK97Y5-RTX360-FK0B91-B208'
        })

        ET.SubElement(new_event_msg, 'TemplateObject', {'name': 'targetId', 'id': '0', 'objectName': 'self', 'isTemp': 'false', 'refParamName': '', 'useRefParam': 'false'})
        ET.SubElement(new_event_msg, 'String', {'name': 'msgKey', 'value': 'ĐÃ MOD CAM XA 10%', 'refParamName': '', 'useRefParam': 'false'})

        new_track_msg.append(new_event_msg)

        action = root.find('.//Action') 
        action.append(new_tracks)
        action.append(new_track_msg)

        tree.write(junglemark_path, encoding='utf-8', xml_declaration=True)
        print(Style.BRIGHT + Fore.CYAN + '⮕', Style.BRIGHT + Fore.YELLOW + "CAM XA 10%", Style.BRIGHT + Fore.GREEN + ' Done!')

        has_run = True  

    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"Lỗi khi xử lý XML: {e}")

def remove_ref_param(destination_path, NAME_HERO, ID_SKIN):
    THU_MUC_SKILL = os.path.join(destination_path, NAME_HERO, 'Skill')
    FILES_XML = [file for file in os.listdir(THU_MUC_SKILL) if file.endswith('.xml')]
    
    for file_name in FILES_XML:
        file_path = os.path.join(THU_MUC_SKILL, file_name)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                xml_content = file.read()
        except UnicodeDecodeError:
            continue
        
        xml_content = re.sub(r'refParamName="" useRefParam="false"\s*', '', xml_content)
        xml_content = re.sub(r'guid="(.*?)"', 'guid="BMH"', xml_content)
        xml_content = re.sub(r'trackName="(.*?)"', f'trackName="MOD-{NAME_HERO}-{ID_SKIN}"', xml_content)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(xml_content)
    
    print(Style.BRIGHT + Fore.CYAN + '[•]',Style.BRIGHT + Fore.YELLOW + "RÚT GỌN ACTIONS", Style.BRIGHT + Fore.GREEN + ' Done!')

    
import os
import re
from colorama import Style, Fore

def thongbao(RSBBC, ID_SKIN):
    if not os.path.exists(RSBBC):
        print("Tệp tin không tồn tại.")
        return

    try:
        with open(RSBBC, "rb") as file:
            content = file.read()

        # Giữ bản gốc để so sánh
        new_content = content

        # Thay thế nội dung theo ID_SKIN
        if ID_SKIN == b'15015':
            new_content = re.sub(rb"UI3D/Battle/Broadcast/18/\{0\}", b"UI3D/Battle/Broadcast/20/{0}", content)
        elif ID_SKIN in [b'15009', b'15013']:
            new_content = re.sub(rb"UI3D/Battle/Broadcast/18/\{0\}", b"UI3D/Battle/Broadcast/16/{0}", content)
        elif ID_SKIN == b'15012':
            new_content = re.sub(rb"UI3D/Battle/Broadcast/18/\{0\}", b"UI3D/Battle/Broadcast/9/{0}", content)

        # In nội dung trước và sau thay thế (nếu cần kiểm tra)
        print("Nội dung trước thay thế:", content[:100])  # In 100 byte đầu tiên
        print("Nội dung sau thay thế:", new_content[:100])

        # Chỉ ghi lại tệp và in thông báo nếu nội dung thay đổi
        if new_content != content:
            with open(RSBBC, "wb") as file:
                file.write(new_content)
            print(Style.BRIGHT + Fore.CYAN + '⮕', Style.BRIGHT + Fore.GREEN + "MOD THÔNG BÁO !")
        else:
            print(f"Không tìm thấy chuỗi cần thay thế trong tệp '{RSBBC}' với ID_SKIN: {ID_SKIN}.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        




nhapid = input(Style.BRIGHT + Fore.CYAN + '[1] (Input_Id.txt) | [2] (Image) | 1 or 2 : ' + Style.RESET_ALL)

hdhu = 'y'
deskins = 'y'

IDD = None

if nhapid == '1':
    try:
        with open('Input_Id.txt') as f:
            input_numbers = f.read()
        numbers = [int(num) for num in input_numbers.split('\n') if num.isdigit()]
        results = process_input_numbers(numbers)
        if results is not None:
            result_str = ' '.join(map(str, results))
            IDD = result_str.split()
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + 'Lỗi: Không tìm thấy tệp Input_Id.txt')

elif nhapid == '2':
    IDD = [file.replace('.jpg', '') for file in os.listdir('INPUT_ID') if file.endswith('.jpg')]

if IDD is not None:
    IDMODSKIN = IDD
    DANHSACH = IDD

    FILES_ICON = [HeroSkin, HeroSkinShop]
    botimskin(HeroSkin, DANHSACH)
    giai(Back)
    giai(hasteE1)
    giai(HasteE1_leave)
    giai(Dance)
    giai(RSBBC)
    giai(junglemark_path)
    

    filename1 = HeroSkin
    option = 1
    heroskinxml(filename1, option)
    file_path = HeroSkinShop
    option = 1
    heroskinshopxml(file_path, option)
    update_junglemark_xml(junglemark_path)
    

else:
    print(Style.BRIGHT + Fore.RED + 'Lỗi: Không có dữ liệu ID. Vui lòng kiểm tra tệp Input_Id.txt hoặc thư mục INPUT_ID.')

for ID_SKIN in IDMODSKIN:
    modsoundages = ''
    print(Style.BRIGHT + Fore.CYAN + f'\n\n\t───────────────[{ID_SKIN}]───────────────')
    for dir_name in os.listdir(source_path):
        source_dir = os.path.join(source_path, dir_name)
        if os.path.isdir(source_dir) and ID_SKIN[:3]+'_' in dir_name:
            NAME_HERO = dir_name
    #thongbao(RSBBC, ID_SKIN)    
    dieukienmod = modheroskin(ID_SKIN, HeroSkin)
    modheroskinshop(ID_SKIN, HeroSkinShop)
    montion(ID_SKIN, file_mod_Modtion)
    modvien(ID_SKIN, HeadImage, HeadID)
    with open (ktr_Sound, 'rb') as s:
        kts = s.read()
    if ID_SKIN.encode() in kts:
        modsoundages = 'y'
    sound_databin(ID_SKIN, Sound_Files)



    if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod:
        liteBulletCfg(ID_SKIN, file_mod_skill1)
        skillmark(ID_SKIN, file_mod_skill2)
        #thongbao(RSBBC, ID_SKIN)


    if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod or ID_SKIN == "53702" or ID_SKIN == '53002':
        destination_path = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/{ID_SKIN}'
        os.makedirs(destination_path, exist_ok=True)
        shutil.copytree(f'EX/AGES/{NAME_HERO}', f'{destination_path}/{NAME_HERO}', dirs_exist_ok=True)
        modhieuung(ID_SKIN,destination_path,NAME_HERO, modsoundages)
        replace_skin_avatar_list(destination_path, NAME_HERO, ID_SKIN)
        code_bv_skill = b''
        files_code_bv_skill = destination_path+'/'+NAME_HERO+'/Skill/'+ID_SKIN+'_Back.xml'
        if os.path.exists(files_code_bv_skill):
            with open(files_code_bv_skill, 'rb') as f: code_bv_skill = f.readlines()
            result_lines = []
            found = False
            for line in code_bv_skill:
                if found:
                    result_lines.append(line)
                if b'<Action tag="' in line:
                    found = True
            #filtered_lines = [line for line in result_lines if b'<Condition' not in line]
            result_lines = [line for line in result_lines if line.strip() not in [b'</Action>', b'</Project>']]
            code_bv_skill = b''.join(result_lines)
            code_bv_skill = b'\r\n'+code_bv_skill
        if hdhu == 'y':
            HD_HIEUUNG_AGES(destination_path, NAME_HERO)
        
        if deskins == 'y':
            moddeskins(destination_path, NAME_HERO)
            remove_ref_param(destination_path, NAME_HERO, ID_SKIN)

            
        folder_to_zip = destination_path
        output_zip = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/'+f'Actor_{ID_SKIN[:3]}_Actions.pkg.bytes'
        zip_folder(folder_to_zip, output_zip)

    if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod or ID_SKIN == "53702" or ID_SKIN == '53002':
        files_fix = f'FILES_MOD/files/Resources/{version}/AssetRefs/Hero/{ID_SKIN[:3]}_AssetRef.bytes'
        shutil.copy(f'EX/AssetRefs/{ID_SKIN[:3]}_AssetRef.bytes', files_fix)
        Directory = files_fix
        LC = '1'
        process_directory(Directory, LC)
        fixlag(ID_SKIN, NAME_HERO, files_fix)
        if hdhu == 'y':
            HD_HIEUUNG_FIX_LAG(files_fix)
        Directory = files_fix
        LC = '2'
        process_directory(Directory, LC)
    if ID_SKIN == '15009':
        giai(Blu15010)
        giai(Red15010)
        habua15010(Blu15010, Red15010)
    if ID_SKIN in ['15009', '14111', '11107', '50108', '13015']:
        hieuungvethan(ID_SKIN, OganSkin)
    if ID_SKIN == '15013':
        giai(Blu15013)
        with open(Blu15013, 'rb') as f:
            content = f.read()
            content = content.replace(b'CheckSkinIdVirtualTick', b'CheckSkinIdTick').replace(b'"skinId" value="'+ID_SKIN+b'"', b'"skinId" value="99999"')
        with open (Blu15013,'wb') as f : f.write(content)
        giai(Blu15013)
        print("BLU_SKILL")

    




    info = f'FILES_MOD/files/Resources/{version}/Prefab_Characters/{ID_SKIN}/Prefab_Hero/{NAME_HERO}'
    shutil.copytree(f'EX/INFO/Prefab_Hero/{NAME_HERO}', info, dirs_exist_ok=True)
    Directory = info+f'/{NAME_HERO}_actorinfo.bytes'
    LC = '1'
    process_directory(Directory, LC)
    if ID_SKIN[:3] in ['192', '196']:
        if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod:
            file = f'FILES_MOD/files/Resources/{version}/Prefab_Characters/{ID_SKIN}/Prefab_Hero/{NAME_HERO}/'
            if ID_SKIN[:3] == '196':
                files = file+'196_Elsu_trap_actorinfo.bytes'
            if ID_SKIN[:3] == '192':
                files = file+'192_HuangZhong_lantern_actorinfo.bytes'
            Directory1 = files
            LC1 = '1'
            process_directory(Directory1, LC1)
            modmatinfo(ID_SKIN, files)
            Directory1 = files
            LC1 = '2'
            process_directory(Directory1, LC)
    elif ID_SKIN[:3] in ['137', '526']:
        if ID_SKIN[:3] == '137':
            NAME_HERO1 = '137_SiMaYi_Pet'
        if ID_SKIN[:3] == '526':
            NAME_HERO1 = '526_Summoner_Pet'
        info1 = f'FILES_MOD/files/Resources/{version}/Prefab_Characters/{ID_SKIN}/Prefab_Pet/{NAME_HERO1}'
        shutil.copytree(f'EX/INFO/Prefab_Pet/{NAME_HERO1}', info1, dirs_exist_ok=True)
       
        if ID_SKIN[:3] == '526':
            #giai(info1)
            NAME_HERO1 = '526_Summoner_Pet'
            Directory2 = info1+f'/526_Summoner_Pet_actorinfo.bytes'
            LC2 = '1'
            process_directory(Directory2, LC2)
            
            P_K, chonpk1 = timpk(ID_SKIN, file_mod_Character, file_map)
            ngoaihinh(ID_SKIN, Directory2, P_K, chonpk1, NAME_HERO1)
            LC2 = '2'
            process_directory(Directory2, LC2)

            
    P_K,chonpk1 = timpk(ID_SKIN, file_mod_Character, file_map)
    ngoaihinh(ID_SKIN, Directory, P_K, chonpk1, NAME_HERO)
    LC = '2'
    process_directory(Directory, LC)
    folder_to_zip = f'FILES_MOD/files/Resources/{version}/Prefab_Characters/{ID_SKIN}'
    output_zip = f'FILES_MOD/files/Resources/{version}/Prefab_Characters/'+f'Actor_{ID_SKIN[:3]}_Infos.pkg.bytes'
    zip_folder(folder_to_zip, output_zip)
    ID_HERO = ID_SKIN[:3]


    DKMBVGT, DDSKM = dkgtbv(ID_SKIN, Huanhua)
    if DDSKM in  DKMBVGT:
        bienve(ID_SKIN, NAME_HERO,ID_HERO, Back, code_bv_skill)
    if b'Sprint' in  DKMBVGT:
        giatoc(ID_SKIN, NAME_HERO,ID_HERO, hasteE1, HasteE1_leave)

    update_junglemark_xml(junglemark_path)
    xoacharacter(ID_SKIN, file_mod_Character)
    


    if hdhu == 'y':
        print(Style.BRIGHT + Fore.RED + '[•]',Style.BRIGHT + Fore.MAGENTA + 'HDR HIỆU ỨNG', Style.BRIGHT + Fore.GREEN + '[YES]')
    if deskins == 'y':
        print(Style.BRIGHT + Fore.RED + '[•]',Style.BRIGHT + Fore.MAGENTA + 'ĐÈ HIỆU ỨNG', Style.BRIGHT + Fore.GREEN + '[YES]')


filename1 = HeroSkin
option = 2
heroskinxml(filename1, option)
file_path = HeroSkinShop
option = 2
heroskinshopxml(file_path, option)
folder_to_zip = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/MOD'
output_zip = f'FILES_MOD/files/Resources/{version}/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'
zip_folder(folder_to_zip, output_zip)
print(Style.BRIGHT + Fore.RED + '[•]',Style.BRIGHT + Fore.CYAN + 'NÉN FILES', Style.BRIGHT + Fore.GREEN + 'Xong !')

