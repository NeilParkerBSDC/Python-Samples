'''
================
Cloud Choice App
================
this is a program to demonstrate how to create a switch statement \
in Python using a 
'''

def cloudModel(OptIndex):
    options=["SaaS","PaaS","IaaS"]
    optChosen=options[OptIndex-1]
    print(optChosen)

question1=int(input("Pick an option: Do you want to \n \
(1) have everything on the cloud \n \
(2) load only your own applications to run from the cloud \n \
(We'll do everything else) \n \
(3) Let us handle just the infrastructure \n"))

cloudModel(question1)

