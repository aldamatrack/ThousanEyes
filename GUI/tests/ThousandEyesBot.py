
from webexteamsbot import TeamsBot
from dotenv import load_dotenv
import requests
import os
import json
from webexteamsbot.models import Response

#"Getting environmental variables"
load_dotenv()
WEBHOOKURL = os.getenv("TEAMS_BOT_URL")
BOTEMAIL = os.getenv("TEAMS_BOT_EMAIL")
TEAMSTOKEN = os.getenv("WEBEX_TEAMS_ACCESS_TOKEN")
TETOKEN = os.getenv("TETOKEN")
BOTAPPNAME = os.getenv("TEAMS_BOT_APP_NAME")
room_ID="Y2lzY29zcGFyazovL3VzL1JPT00vNmZmYzBlNTAtYTdiZC0xMWVjLWFkYWUtMzM1OGE2ZGY3N2E5"

#"TE BASE URL"
base_url = "https://api.thousandeyes.com/v6/"

#"Creating bot object"
bot = TeamsBot(
    BOTAPPNAME,
    teams_bot_token=TEAMSTOKEN,
    teams_bot_url=WEBHOOKURL,
    teams_bot_email=BOTEMAIL,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
    ],

)


#"TE API Request Heather"
TE_headers = {
        "Authorization": "Bearer "+ TETOKEN,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

#
# Here is  a list of predefined funtions for testing purposes
#

# ///////////////////////////////////////////////////////////////////////////////"
# Getting list of enterprise agents, return: EN AGENTS"
def list_ENagents(incoming_msg):
    res = requests.get(url=base_url+"agents", headers=TE_headers)
    data = json.loads(res.text)
    message="Here is your list of Enterprise agents: \n\n"

    for agent in data['agents']:
        if agent['agentType'] == "Enterprise":
            message = message+("Agent Name: {name} \n".format(name = agent['agentName']))


    return message
# ///////////////////////////////////////////////////////////////////////////////"

# ///////////////////////////////////////////////////////////////////////////////"
# "Getting a list of alerts, return alert name, start date, rule expresion, test name"

def TEalerts(incoming_msg):
    res = requests.get(url=base_url+"agents", headers=TE_headers)
    data = json.loads(res.text)


# ///////////////////////////////////////////////////////////////////////////////"



def RulesDetails(incoming_msg):

    res = requests.get(url=base_url+"alert-rules", headers=TE_headers)
    data = json.loads(res.text)['alertRules']

    IDlist = []
    Message = "Here is the description of the actual alerts: \n\n"

    for alert in data:
        IDlist.append(alert['ruleId'])



    for element in IDlist:
        res = requests.get(url=base_url+"alert-rules/"+str(element), headers=TE_headers)
        data = json.loads(res.text)['alertRules']


        for srule in data:
            Message = Message + """The alert ID being analized is: {ID} \n
            The rule name is:  {name}\n
            Alert type: {type}\n
            Rule expression:{expresion}
            \n""".format(ID = element, name = srule['ruleName'], type=srule['alertType'], expresion=srule['expression'])

    return Message
# ///////////////////////////////////////////////////////////////////////////////"
# """
# #
#COde for sending Webex message separate
#
#


def listOfrules():
    res = requests.get(url=base_url+"alert-rules", headers=TE_headers)
    data = json.loads(res.text)['alertRules']

    IDlist = []
    Message = "Here is the description of the actual alerts: \n\n"

    for alert in data:
        IDlist.append(alert['ruleId'])
    return IDlist

def printMessage(element):
    Message = "Here is the description of the actual alerts: \n\n"

    res = requests.get(url=base_url+"alert-rules/"+str(element), headers=TE_headers)
    data = json.loads(res.text)['alertRules'][0]
    #print (data)
    Message = "The alert ID being analized is: {ID} \n The rule name is:  {name}\n Alert type: {type}\n Rule expression:{expresion} \n\n".format(ID = str(element), name = data['ruleName'], type=data['alertType'], expresion=data['expression'])

    return Message

def listforWebex(incoming_msg):

    a = listOfrules()
    for x in a:
        res = Response()
        list = []

        for element in a:
            list.append(printMessage(element) + "\n")
            return list

def listforWebex2(incoming_msg):
    counter = 0
    a = listOfrules()
    res = Response()
    if counter != len(a):
        res = printMessage(a[counter]) + "\n"
        return res
        counter += 1
        listforWebex2()




#
#
#
#
#
bot.add_command("/listenagents", "This will list Enterprise agents", list_ENagents)
bot.add_command("/listofrules", "This will list Thousand EYes rules", RulesDetails)
bot.add_command("/list", "This will list Thousand Eyes rules one by one", listforWebex)
bot.add_command("/mist", "This will list Thousand Eyes rules one by one", listforWebex2)




if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
