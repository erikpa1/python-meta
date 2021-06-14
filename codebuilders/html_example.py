from codebuilders.html_constants import *
from codebuilders.html import *
from codebuilders.html_bootstrap import *


tmp = HtmlDocument()
tmp.head.AddBootstrapRequirment()

bar: bsNavBar = tmp.body.AddNode(bsNavBar())
bar.AddNavItem(bsNavItem("About"))
bar.AddNavItem(bsNavItem("Store"))
bar.AddNavItem(bsNavItem("Cloud"))
bar.AddNavItem(bsNavDropDownItem("Editors", ["Spot", "Map", "Tour"]))



print(tmp)

