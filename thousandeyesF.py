import requests
import os
import json


base_url = "https://api.thousandeyes.com/v6/"


TE_headers = {
        "Authorization": "Bearer 6f37c38a-1808-4e3b-ba41-239c5c5a5cea",
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
def list_ENagents():
    res = requests.get(url=base_url+"agents", headers=TE_headers)
    data = json.loads(res.text)
    "print(data)"
    message="Here is your list of Enterprise agents: \n\n"

    for agent in data['agents']:
        "print(agent)"
        if agent['agentType'] == "Enterprise":
            message = message+("Agent Name: {name} \n".format(name = agent['agentName']))


    return message
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




if __name__ == "__main__":
    print(RulesDetails())
