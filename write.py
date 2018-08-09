import time
input="""
Research Assistant
School of Public Health - Envir Health - Kinney Lab
72 E. Concord Street
(617) 358-2469
mariadc@bu.edu
Castillo Castillo, Maria Daniela
44247
mariadc
X280300
---------------------------------
fopio@bu.edu
Opio, Abari Francis
fopio
X280301
---------------------------------
Lecturer
School of Law - Law JD Program Adjunct Faculty
765 Commonwealth Ave
(617) 353-3110
dmeier@bu.edu
Meier, David E
31200
dmeier
X280302
---------------------------------
Lecturer
English
236 Bay State Rd
(617) 353-2506
strub@bu.edu
Strub, Spencer
20207
strub
X280303
---------------------------------
ERROR
rany2@bu.edu
Yan, Ran
rany2
X280304
---------------------------------
stevenms@bu.edu
Stevens, Mitchell, P
stevenms
X280305
---------------------------------
ERROR
ERROR
---------------------------------
Timeout
haupandp@bu.edu
Boyd, Sean
haupandp
X280307
---------------------------------
Custodian, Lpt
Real Estate Management - Area 08
120 Ashford St
(617) 839-0538
ktsheeha@bu.edu
Sheehan, Kieran T
96409
ktsheeha
X280308
---------------------------------
liangheq@bu.edu
Liang, Heqiuyi
liangheq
X280309
---------------------------------
Custodian, Lpt
Real Estate Management - Area 16
120 Ashford St
(617) 353-2105
shirmimo@bu.edu
Mimouni, Shirley
96409
shirmimo
X280310
---------------------------------
bernstan@bu.edu
Bernstein, Alyssa, Nicole
bernstan
X280311
---------------------------------
sl513@bu.edu
Lee, Soo Jeong
sl513
X280312
---------------------------------
Graduation Advisor
Student Academic Life - CAS Academic Services
100 Bay State Rd
(617) 353-2400
cmwa@bu.edu
Ward, Christopher
20045
cmwa
X280313
---------------------------------
---------------------------------
Timeout
ERROR
---------------------------------
Timeout
hoping@bu.edu
Ho, Ping-Han
hoping
X280316
---------------------------------
jaryan@bu.edu
Ryan, Jill, Ann
jaryan
X280317
---------------------------------
goldbeas@bu.edu
Goldberg, Andrew, Stone
goldbeas
X280318
---------------------------------
perrieg@bu.edu
Gregg, Perrie
perrieg
X280319
---------------------------------
---------------------------------
botan@bu.edu
Tan, Bo
botan
X280321
---------------------------------
---------------------------------
---------------------------------
---------------------------------
ERROR
Research Dental Assistant
Division of School-Based Programs
560 Harrison Ave
(617) 638-4918
gmontoya@bu.edu
Montoya Almada, Guadalupe
58249
gmontoya
X280325
---------------------------------
---------------------------------
---------------------------------
ERROR
ERROR
---------------------------------
tianzhu@bu.edu
Liang, Tianzhu
tianzhu
X280329
---------------------------------
ERROR
mcquaidl@bu.edu
Mcquaid, Larry
mcquaidl
X280330
---------------------------------
ERROR
bryanq@bu.edu
Queme, Bryan, Michael
bryanq
X280331
---------------------------------
aclar015@bu.edu
Clarke, Adrian
aclar015
X280332
---------------------------------
khazanov@bu.edu
Khazanov, Alexey
khazanov
X280333
---------------------------------
---------------------------------
jadenp@bu.edu
Peng, Xin
jadenp
X280335
---------------------------------
ERROR
coatouca@bu.edu
Chisholm, Victor
coatouca
X280336
---------------------------------
jetsbilo@bu.edu
Ellison, Nicole
jetsbilo
X280337
---------------------------------
---------------------------------
mckinlem@bu.edu
Mckinley, Megan
mckinlem
X280339
---------------------------------
daspooja@bu.edu
Das, Pooja
daspooja
X280340
---------------------------------
ahlittle@bu.edu
Little, Ashley, Helen
ahlittle
X280341
---------------------------------
shanyns@bu.edu
Siegel, Shanyn
shanyns
X280342
---------------------------------
General Mechanic
Real Estate Management - Mechanical Services
750 Harrison Ave
(617) 638-4144
mforward@bu.edu
Forward, Mark
54475
mforward
X280343
---------------------------------
---------------------------------
ERROR
---------------------------------
agriff82@bu.edu
Griffin, Aaron, L
agriff82
X280346
---------------------------------
adilafs@bu.edu
Saptari, Adila, Fahmida
adilafs
X280347
---------------------------------
meristem@bu.edu
Min, Dong-Kook
meristem
X280348
---------------------------------
lvlu2017@bu.edu
Lu, Wen
lvlu2017
X280349
---------------------------------
hailasz@bu.edu
Almutairi, Haila, Saad Z
hailasz
X280350
---------------------------------
---------------------------------
lifeplans, Group
X280352
---------------------------------
sara99@bu.edu
Albuainain, Sara, Saqer S
sara99
X280353
---------------------------------
alhawait@bu.edu
Alhawaiti, Saleh, Ahmed E
alhawait
X280354
---------------------------------
fouzjame@bu.edu
Alzahrani, Faizah, Saeed J
fouzjame
X280355
---------------------------------
ERROR
ERROR
---------------------------------
ERROR
tflahbu@bu.edu
Flaherty, Theresa, Lynn
tflahbu
X280357
---------------------------------
School of Theology
ahahn@bu.edu
Hahn, Zintack
30040g
ahahn
X280358
---------------------------------
xzy1990@bu.edu
Xiao, Zhongyuan
xzy1990
X280359
---------------------------------
adamfro@bu.edu
Froehlich, Adam
adamfro
X280360
---------------------------------
---------------------------------
riyadh@bu.edu
Alzahrani, Riyadh, Abdullah M
riyadh
X280362
---------------------------------
---------------------------------
---------------------------------
yizhiw@bu.edu
Wang, Yizhi
yizhiw
X280365
---------------------------------
haifaoo@bu.edu
Alomair, Haifa, Nasser A
haifaoo
X280366
---------------------------------
Psychological & Brain Sciences
yoonjnam@bu.edu
Nam, Yoon Jung
yoonjnam
X280367
---------------------------------
---------------------------------
sabahzh@bu.edu
Alzahrani, Sabah, Ali D
sabahzh
X280369
---------------------------------
---------------------------------
bursaux@bu.edu
Bursaux, Anna, Laure
bursaux
X280371
---------------------------------
---------------------------------
clscnlp, Group
X280373
---------------------------------
ERROR
yushanch@bu.edu
Chen, Yushan
yushanch
X280374
---------------------------------
boskov@bu.edu
Boskov, Novak
boskov
X280375
---------------------------------
ameagle@bu.edu
Eagle, Annie
ameagle
X280376
---------------------------------
mma123@bu.edu
Altholtz, Madeline
mma123
X280377
---------------------------------
dhblair@bu.edu
Blair, David
dhblair
X280378
---------------------------------
jlopilat@bu.edu
Lopilato, Joseph, Michael
jlopilat
X280379
---------------------------------
charelsr@bu.edu
Casanova, Rosalia
charelsr
X280380
---------------------------------
Lecturer
School of Law - Grad Program in Banking Law
765 Commonwealth Ave
(617) 353-3023
sbleier@bu.edu
Bleier, Scott R.
31204
sbleier
X280381
---------------------------------
khalidz@bu.edu
Alshammari, Khalid, Zaben H
khalidz
X280382
---------------------------------
breyna11@bu.edu
Reyna, Brandon, Dickson
breyna11
X280383
---------------------------------
jenkenn@bu.edu
Kennedy, Jennifer, Kate
jenkenn
X280384
---------------------------------
vmodev@bu.edu
Modev, Viktor
vmodev
X280385
---------------------------------
smays@bu.edu
Mays, Sara
smays
X280386
---------------------------------
Lecturer
School of Social Work - Charles River Campus Instruction
264 Bay State Rd
(617) 353-3750
jeffersm@bu.edu
Jeffers, Misti
34203
jeffersm
X280387
---------------------------------
ERROR
ERROR
---------------------------------
ERROR
ignacibu@bu.edu
Lira Bustamante, Ignacia, Andrea
ignacibu
X280389
---------------------------------
sofisid@bu.edu
Sideri, Sofia
sofisid
X280390
---------------------------------
ERROR
tahanifa@bu.edu
Alkhuraiji, Tahani, Fahad A
tahanifa
X280391
---------------------------------
---------------------------------
kmalexan@bu.edu
Alexander, Kraig, M.
kmalexan
X280393
---------------------------------
yara7@bu.edu
Mannaa, Yara, Zuhair A
yara7
X280394
---------------------------------
cxiaoyu@bu.edu
Chen, Xiaoyu
cxiaoyu
X280395
---------------------------------
casavant@bu.edu
Casavant, Matthew
casavant
X280396
---------------------------------
gserrano@bu.edu
Serrano, Gabriel
gserrano
X280397
---------------------------------
---------------------------------
---------------------------------
dganjian@bu.edu
Ganjian, Danielle
bmc
dganjian
X280400
---------------------------------
kristar2@bu.edu
Ramiah, Krista
kristar2
X280401
---------------------------------
---------------------------------
tdhanji@bu.edu
Dhanji, Tehzeen
tdhanji
X280403
---------------------------------
---------------------------------
annili@bu.edu
Li, Anni
annili
X280405
---------------------------------
yusuke52@bu.edu
Arie, Yusuke
yusuke52
X280406
---------------------------------
dgavan@bu.edu
Gavan, Daniel, V
dgavan
X280407
---------------------------------
dfeigen1@bu.edu
Feigenbaum, Dylan, Richard
dfeigen1
X280408
---------------------------------
afnan409@bu.edu
Alyanallah, Afnan, Abdulrahman A
afnan409
X280409
---------------------------------
Timeout
oce7@bu.edu
Ehimiaghe, Ohiosumuan, Chibuikem
oce7
X280410
---------------------------------
Timeout
---------------------------------
---------------------------------
---------------------------------
---------------------------------
---------------------------------
---------------------------------
---------------------------------
---------------------------------
mafolabi@bu.edu
Afolabi, Moyosola, Olanrele
mafolabi
X280419
---------------------------------
ulena@bu.edu
Lena, Umme, Kulsum
ulena
X280420
---------------------------------
---------------------------------
ERROR
santjua@bu.edu
Santiago, Juanita
santjua
X280422
"""
input=input.split("---------------------------------")
for i in range(0,len(input)):
    input[i]=input[i].splitlines()

def rem(the_list, val):
    while val in the_list:
        the_list.remove(val)

for i in range(0,len(input)):
    rem(input[i],"")
    rem(input[i], "ERROR")
    rem(input[i], "Timeout")
    input[i].reverse()
rem(input,[])

for i in input:
    print
    for j in i:
        print(j,end="|")
    print("\n")


filename="info"+str(time.ctime())
with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    for i in input:
        f.write("|")
        for j in i:
            str=j+"|"
            f.write(str)
        f.write("\n")
print(filename)