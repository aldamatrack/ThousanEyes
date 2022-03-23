import requests
import os
import json


base_url = "https://api.thousandeyes.com/v6/"


TE_headers = {
        "Authorization": "Bearer ca4d330c-2d42-4ac2-bcbf-944c376d622a",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }


def list_agents():
    res = requests.get(url=base_url+"agents", headers=TE_headers)
    data = json.loads(res.text)
    "print(data)"
    message="Here is your list of agents:"

    for agent in data['agents']:
        "print(agent)"
        message = message+("Agent Name: {name} Agent type: {agentt}".format(name = agent['agentName'], agentt = agent['agentType']))


    return message

# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # #
def list_ENagents(token):

    TE_headers = {
            "Authorization": "Bearer "+ token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }


    res = requests.get(url=base_url+"agents", headers=TE_headers)
    data = json.loads(res.text)
    "print(data)"
    message="Here is your list of Enterprise agents: \n\n"

    for agent in data['agents']:
        "print(agent)"
        if agent['agentType'] == "Enterprise":
            message = message+("Agent Name: {name} \n".format(name = agent['agentName']))

    data =  {"message": message, "code":res.status_code}
    return data
    # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #

def TEalerts():
    res = requests.get(url=base_url+"alerts", headers=TE_headers)
    data = json.loads(res.text)
    IDlist = []
    print(data)
    for alert in data:
        print(alert)
        # IDlist.append(alert['alertId'])
    # return IDlist


# # # # # # # # # # # # # # # # # # # # # # # # #

def RulesDetails():

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
            Message = Message + "The alert ID being analized is: {ID} \n The rule name is:  {name}\n Alert type: {type}\n Rule expression:{expresion} \n\n".format(ID = element, name = srule['ruleName'], type=srule['alertType'], expresion=srule['expression'])

    return Message


#FUniton to test split of messages of Message

def ConstantMessage(List):
    res = requests.get(url=base_url+"alert-rules", headers=TE_headers)
    data = json.loads(res.text)['alertRules']

    IDlist = []
    Message = "Here is the description of the actual alerts: \n\n"



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
"""
def listforWebex():
    a = listOfrules()
    print(a)
    list = []
    for element in a:
        #print(printMessage(element) + "\n\n\n")
        list.append(printMessage(element) + "\n\n\n")
        #print(list)



def listforWebex2():
    counter =0
    a = listOfrules()

    if counter != len(a):
        print(printMessage(a[counter]) + "\n")

        counter += 1
        listforWebex2()
"""




#if __name__ == "__main__":

#print(list_ENagents("beaef231-dae7-45a0-afaa-860728730871"))
