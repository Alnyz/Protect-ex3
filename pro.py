# -*- coding: utf-8 -*
# AUTHOR ALI id Line @uhuuyyy
from linepy import *
from datetime import datetime, timedelta
import time, asyncio, json, os, sys, traceback
#al = LINE('EMAIL', 'PASSWORD')
al = LINE('EqTVVCqaa5Q5OnTb8MH6.89AjSGSdgP5hk9f/sGA3fG.lFqcxG9G7IX9smSpRNQ6sUKfy3JgbVgQg7uSH4TbFhk=')
li = LINE('EqE5w3xxdjMv7PkVEi50.EZub91DHxrSbVfTrRIAqua.MfeJTeGsMvjou2NotF9lizs5+Sel2DDGWMVDU3HdhJI=')
al.log("Auth Token : " + str(al.authToken))
li.log("Auth Token : " + str(li.authToken))
alMid = al.getProfile().mid
liMid = li.getProfile().mid
author = ["Your MID"]
print("Sunccess Loggin")
with open('pro1.json') as fp:
    wait = json.load(fp)
with open('pro2.json') as fp:
    wait2 = json.load(fp)
# Initialize OEPoll with LINE instance
oepoll = OEPoll(al)
def backupjson1():
    with open('pro1.json','w') as fp:
        json.dump(wait,fp,ensure_ascii=True,indent=4)
def backupjson2():
    with open('pro2.json','w') as fp:
        json.dump(wait2,fp,ensure_ascii=True,indent=4)
def leftGroup(to,mid):
    al.sendMessageWithMention2(to,"Thanks for invited",mid,"")
    al.leaveGroup(to)
    li.leaveGroup(to)
def blacklist(to):
    if wait['blacklist'] == []:
        al.sendMessage(to,"Opps! Blacklist is empty")
    else:
        list = [contact for contact in wait['blacklist']]
        al.sendMessageWithMention3(to,"「 Blacklist User 」\nList:\n",list)
def admilist(to):
    if wait['admin'] == []:
        al.sendMessage(to,"Opps! Admin list is empty")
    else:
        list = [contact for contact in wait['admin']]
        al.sendMessageWithMention3(to,"「 Admin List 」\nList:\n",list)
def deleteBL(to):
    wait['blacklist'] = []
    backupjson1()
    al.sendMessage(to,"Succes Clear all Blacklist")
def joinall(to):
    g = al.getGroup(to)
    g.preventedJoinByTicket = False
    al.updateGroup(g)
    ti = al.reissueGroupTicket(to)
    li.acceptGroupInvitationByTicket(to,ti)
    g.preventedJoinByTicket = True
    li.updateGroup(g)
def speed(to):
    t = time.time()
    al.sendMessage(to,"...")
    al.sendMessage(to,"%s" % (time.time() - t))
def restart(to):
    al.sendMessage(to,'Trying to restarted ..')
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)
def protectList(to):
    if wait2['protect']['aliKick'] == []:
        pro = "  「 Protect List 」\nProtect Kick:\n  None!"
    else:
        pro = "  「 Protect List 」\nProtect Kick:"
    no=0
    for a in wait2['protect']['aliKick']:
        no+=1
        pro+= "\n  %i. %s" % (no,al.getGroup(a).name)
    if wait2['protect']['aliInvt'] == []:
        pro1 = "\nProtect Invited: \n  None!"
    else:
        pro1 = "\nProtect Invited: "
    num=0
    for b in wait2['protect']['aliInvt']:
        num+=1
        pro1+="\n  %i. %s" % (no,al.getGroup(b).name)
    if wait2['protect']['aliQr'] == []:
        pro2 = "\nProtect Qr: \n  None!"
    else:
        pro2 = "\nProtect Qr: "
    nums=0
    for C in wait2['protect']['aliQr']:
        nums+=1
        pro2+="\n  %i. %s" % (no,al.getGroup(C).name)
    if wait2['protect']['aliCancel'] == []:
        pro3 = "\nProtect Cancel: \n  None!"
    else:
        pro3 = "\nProtect Cancel: "
    numss=0
    for d in wait2['protect']['aliCancel']:
        numss+=1
        pro3+="\n  %i. %s" % (no,al.getGroup(d).name)
    lens = "\n\nTotal Protect kick:{}\nTotal Protect Invite:{}\nTotal Protect Qr:{}\nTotal Protect Cancel:{}".format(len(wait2['protect']['aliKick']),len(wait2['protect']['aliInvt']),len(wait2['protect']['aliQr']),len(wait2['protect']['aliCancel']))
    al.sendMessage(to,pro+pro1+pro2+pro3+lens)
def protect(to,pl=""):
    grup = al.getGroup(to)
    if pl == "kick on":
        if grup.id in wait2['protect']['aliKick']:
            al.sendMessage(to,grup.name+" Already in Protect Kick")
        else:
            wait2['protect']["aliKick"].append(grup.id)
            backupjson2()
            al.sendMessage(to,"Success add "+grup.name+" Add to Protect kick")
    if pl == "kick off":
        if grup.id not in wait2['protect']['aliKick']:
            al.sendMessage(to,grup.name+" Not in Protect Kick")
        else:
            wait2['protect']["aliKick"].remove(grup.id)
            backupjson2()
            al.sendMessage(to,"Success remove "+grup.name+" Add to Protect kick")
    if pl == "invite on":
        if grup.id in wait2['protect']['aliInvt']:
            al.sendMessage(to,grup.name+" Already in Protect Invite")
        else:
            wait2['protect']["aliInvt"].append(grup.id)
            backupjson2()
            al.sendMessage(to,"Success add "+grup.name+" Add to Protect Invited")
    if pl == "invite off":
        if grup.id not in wait2['protect']['aliInvit']:
            al.sendMessage(to,grup.name+" Not in Protect Invited")
        else:
            wait2['protect']["aliInvt"].remove(grup.id)
            backupjson2()
            al.sendMessage(to,"Success remove "+grup.name+" Add to Protect Invited")
    if pl == "qr on":
        if grup.id in wait2['protect']['aliQr']:
            al.sendMessage(to,grup.name+" Already in Protect Qr")
        else:
            wait2['protect']["aliQr"].append(grup.id)
            backupjson2()
            al.sendMessage(to,"Success add "+grup.name+" Add to Protect Qr")
    if pl == "qr off":
        if grup.id not in wait2['protect']['aliQr']:
            al.sendMessage(to,grup.name+" Not in Protect Qr")
        else:
            wait2['protect']["aliQr"].remove(grup.id)
            backupjson2()
            al.sendMessage(to,"Success remove "+grup.name+" Add to Protect Qr")
    if pl == "cancel on":
        if grup.id in wait2['protect']['aliCancel']:
            al.sendMessage(to,grup.name+" Already in Protect Cancel")
        else:
            wait2['protect']["aliCancel"].append(grup.id)
            backupjson2()
            al.sendMessage(to,"Success add "+grup.name+" Add to Protect Cancel")
    if pl == "qr off":
        if grup.id not in wait2['protect']['aliCancel']:
            al.sendMessage(to,grup.name+" Not in Protect Cancel")
        else:
            wait2['protect']["aliCancel"].remove(grup.id)
            backupjson2()
            al.sendMessage(to,"Success remove "+grup.name+" Add to Protect Cancel")
def addAdmin(to):
    targets = []
    key = eval(msg.contentMetadata["MENTION"])
    key["MENTIONEES"][0]["M"]
    for x in key["MENTIONEES"]:
        targets.append(x["M"])
    for target in targets:
        if target in wait['admin']:
            al.sendMessageWithMention2(to,"Opps!",target,"Already in Admin list")
        else:
            wait['admin'].append(target)
            backupjson1()
            al.sendMessageWithMention2(to,"Succes add",target,"to Admin list")
while True:
    try:
        ops=oepoll.singleTrace(count=50)
        for op in ops:
            if op.type == 13:
                print("NOTIFIED INVITED")
                if alMid in op.param3: 
                    if op.param2 in wait['admin'] or op.param2 in wait['whitelist']:
                        al.acceptGroupInvitation(op.param1)
                        al.sendMessageWithMention2(op.param1,"Thanks for invited >,<",op.param2,""),
                    if op.param2 not in wait['admin'] and op.param2 in wait['blacklist']:
                        al.acceptGroupInvitation(op.param1)
                        al.sendMessageWithMention2(op.param1,'Opps sorry',op.param2,'only admin can Invite me')
                        al.leaveGroup(op.param1)
            if op.type == 19:
                print("NOTIFIE KICK [19]")
                try:
                    if op.param1 in wait2["protect"]["aliKick"]:
                        if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                            pass
                        else:
                            if op.param2 in wait['blacklist']:
                                al.kickoutFromGroup(op.param1,[op.param2])
                            else:
                                if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                                    pass
                                else:
                                    C = al.getContact(op.param2)
                                    al.kickoutFromGroup(op.param1,[C.mid])
                                    wait['blacklist'].append(C.mid)
                                    backupjson1()
                                    al.sendMessageWithMention2(op.param1,'Success add',C.mid,'To Blacklist')
                except Exception as e:
                    print(e)
            if op.type == 13:
                print("NOTIFIED INVITES MEMBERS [13]")
                try:
                    if op.param1 in wait2["protect"]["aliInvt"]:
                        if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                            pass
                        else:
                            if op.param2 in wait['blacklist']:
                                al.kickoutFromGroup(op.param1,[op.param2])
                                al.kickoutFromGroup(op.param1,[op.param3])
                            else:
                                if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                                    pass
                                else:
                                    C = al.getContact(op.param2)
                                    al.kickoutFromGroup(op.param1,[op.param3])
                                    li.kickoutFromGroup(op.param1,[C.mid])
                                    wait['blacklist'].append(C.mid)
                                    backupjson1()
                                    al.sendMessageWithMention2(op.param1,'Success add',C.mid,'To Blacklist')
                except Exception as e:
                    print(e)
            if op.type == 32:
                print("NOTIFIED CANCELED [32]")
                try:
                    if op.param1 in wait2["protect"]["aliCancel"]:
                        if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                            pass
                        else:
                            if op.param2 in wait['blacklist']:
                                al.kickoutFromGroup(op.param1,[op.param2])
                            else:
                                if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                                    pass
                                else:
                                    C = al.getContact(op.param2)
                                    li.kickoutFromGroup(op.param1,[C.mid])
                                    wait['blacklist'].append(C.mid)
                                    backupjson1()
                                    al.sendMessageWithMention2(op.param1,'Success add',C.mid,'To Blacklist')
                except Exception as e:
                    print(e)
            if op.type == 11:
                print("NOTIFIED UPDATE GROUP [11]")
                try:
                    if op.param1 in wait2["protect"]["aliQr"]:
                        if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                            pass
                        else:
                            if op.param2 in wait['blacklist']:
                                G = al.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                al.kickoutFromGroup(G.id,[op.param2])
                                al.updateGroup(G)
                            else:
                                if op.param2 in wait["admin"] or op.param2 in wait['whitelist'] or op.param2 in wait['bots']:
                                    pass
                                else:
                                    C = al.getContact(op.param2)
                                    G = al.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    al.updateGroup(G)
                                    li.kickoutFromGroup(G.id,[C.mid])
                                    wait['blacklist'].append(C.mid)
                                    backupjson1()
                                    al.sendMessageWithMention2(G.id,'Success add',C.mid,'To Blacklist')
                except Exception as e:
                    print(e)
            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                to = msg.to
                from_ = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            al.sendChatChecked(to,msg_id)
                            li.sendChatChecked(to,msg_id)
                            #This line to call Functional
                except Exception as e:
                    print(traceback.format_exc())
                    al.log("[RECEIVE_MESSAGE] ERROR : " + str(e))
            # Don't remove this line, if you wan't get error soon!
            oepoll.setRevision(op.revision)
            
    except Exception as e:
        print(traceback.format_exc())
        al.log("[SINGLE_TRACE] ERROR : " + str(e))
