from fastapi import FastAPI
from reactpy.backend.fastapi import configure

from reactpy import component,html

# NOW IMPORT reactpy_router
from reactpy_router import route,simple,link
# FOR GET PARAMETER 
from reactpy_router.core import use_params



@component
def myrouter():
	return simple.router(
		route("/",home()),
		route("/about",about()),
		# AND ROUTER FOR GET PARAMS
		route("/details/{names}",detailspage()),
		# NOW IF YOU ROUTER NOT FOUND 
		route("*",html.h1("YOU NOT FOUND ROUTE GUYS")),

		)

# NOW CREATE COMPONENT TO VIEW
@component
def home():
	# NOW I SEND SAMPLE PARAMS
	my_params = "youtube-kids"
	return html.div(
		html.h1("home page"),
		# NOW I CREATE NAVIGATION LINK
		link("about page",to="/about"),
		# AND LINK WITH PARAMETER
		link("details page",to="/details/{}".format(my_params))
		)

# FOR ABOUT PAGE
@component
def about():
	return html.div(
		html.h1("about page"),
		link("Home page",to="/")
		)

# AND FOR DETAILS PAGE
@component
def detailspage():
	# AND NOW I GET PARAMS FROM URL
	names = set(use_params()['names'].split("-"))
	# AND REMOVE -
	result_names = ' '.join(names)
	print(names)
	return html.div(
		html.h1(f"details page , you params is : {result_names}"),
		# LINK TO ABOUT PAGE
		link("about page",to="/about")
		)



app = FastAPI()
configure(app,myrouter)