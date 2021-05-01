
from meta.logging import *
from meta.codebuilders.html import HtmlDocument
from meta.codebuilders.html_bootstrap import *

import webbrowser
import os

document = HtmlDocument()

document.head.AddBootstrapRequirment()
document.head.SetTitle("Turtle")

navBar = document.body.AddNode(NavBar())

navBar.AddNavItem(Brand("About"))
navBar.AddNavItem(NavItem("Market")).SetActive(True)
navBar.AddNavItem(NavItem("Overview"))
navBar.AddNavItem(NavItem("Contact"))
navBar.AddNavItem(NavDropDownItem("Editors", ["Some editor", "Another editor"]))

container: Container = document.body.AddNode(Container())
container.topPadding = 5
container.skin = "dark"
container.fontSkin = "white"
container.AddItem(Header3("Dadada"))
container.AddItem(Header2("Dadada"))
container.AddItem(Header1("Dadada"))
container.AddItem(Paragraph("Here is some cool text inside the paragraf"))

container: Container = document.body.AddNode(Container())
container.fluidEnabled = True
container.AddItem(Header3("Dadada"))
container.AddItem(Header2("Dadada"))
container.AddItem(Header1("Dadada"))
container.AddItem(Paragraph("Here is some cool text inside the paragraf"))

container: Container = document.body.AddNode(Container())
container.fluidEnabled = True
container.borderEnabled = True
container.AddItem(Header3("Dadada"))
container.AddItem(Header2("Dadada"))
container.AddItem(Header1("Dadada"))
container.AddItem(Paragraph("Here is some cool text inside the paragraf"))

table: TableView = document.body.AddNode(TableView())


f = open('helloworld.html','w')

message = document.ToString()

LogD << message

if True:
    f.write(message)
    f.close()
    webbrowser.open_new_tab(os.getcwd() + '\helloworld.html')