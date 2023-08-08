# cd
Hierbij een verslag van mijn project, CD, die ik heb op moeten zetten. Hiervoor heb ik een virtuele server via Digital Ocean gebruikt, en een simpele flask app geschreven via VS code.
De uiteneindelijke bedoeling van het project is: bij een wijziging in Flask-app, en na het pushen en/of uploaden van het project naar github, moet mijn project op mijn virtuele server ook wijzigen. 


# 3 Components of my solutions
## Github actions
In github/actions hoefde ik uiteindelijk alleen een main.yml bestand te maken. 
In deze bestand staan de acties die uitgevoerd moeten worden: in dit geval twee acties; test en 
deploy acties. Pytest doet de eerste fase en wanneer de test compleet is kan mijn project door eerst in te loggen in mijn virtuele server uiteindelijk aangewend worden; deploy-fase! 
## SSH keys
Om in te loggen op je server maak je gebruik van een speciale sleutel. Deze sleutel heb ik gegeneerd in github. Ik heb een private en een public key gegenereerd. Mijn public-key staat in mijn map .ssh directory in de map: authorized_keys.
En mijn private-key staat onder secrets in Github. Ik had wel moeite om te begrijpen hoe het allemaal werkte en hoe ik uiteindelijk alles moest genereren en opslaan.
## Github-secrets
In Github-secrets heb je de mogelijkheid om je inloggegevens zoals je username, ip adressen en keys op te slaan. Ik kwam er iets later achter dat je de data die je wilt opslaan in Secrets niet ziet. 


Ik vond dit een lastige eindopracht. Achteraf kan ik zeggen dat ik ook de opdracht zelf niet altijd duidelijk vond, maar dat ik tegelijkertijd ook veel nieuwe dingen heb geleerd die ik zeer interessant vind en een eventuele voortgang in back-end en python zeker de moeite waard vind.
Wat betreft de opdracht viel het muntje wat betreft Ubuntu en de commando's wat later. Ik begreep ook niet gelijk hoe ik door de mappenstructuur door kon surfen met de diverse commano's. 
Een ander probleem was het bewerken en aanpassen van mijn CD.service en die ook weer in de juiste directory zetten. Daar heb ik even mee moeten worstelen maar dankzij de docenten en het internet is het toch gelukt. 
En als het goed is werkt nu alles zoals het zou moeten :)

