import requests
def getdata(ipaddress):
    #ipaddress=input("Enter IP address: ")
    headers = {'User-agents':'Mozilla/5.0'}
    txtfile=requests.get("http://rbl-check.org/rbl_api.php?ipaddress="+ipaddress, headers=headers)
    txtfile=txtfile.text
    txtfile=txtfile.replace(";",",")
    txtfile=txtfile.replace("\n",",")
    txtfile=txtfile.split(",")
    result=[]
    for i in range(136):
        if(txtfile[i]=="listed"):
            result.append(txtfile[i-3]+" Listed")
    result='\n'.join(result)
    return result
#mytoken = "" #Token of your Telegram bot
#chats=[""] #ID's of the chats that you want to send results (use @userinfobot to learn)
ipaddress=input("IP address to check: ")
print(getdata(ipaddress))
#for i in range(len(chats)):
#    send_result = 'https://api.telegram.org/bot' + mytoken + '/sendMessage?chat_id='+chats[i]+'&parse_mode=Markdown&text='+getdata(ipaddress)
#    requests.get(send_result)
