from selenium.webdriver.common.by import By


class PaneLocators(object):
	# parent
	PANE = (By.CSS_SELECTOR, "#pane-side")

	# childs
	OPENED_CHATS = (By.CSS_SELECTOR, "#pane-side ._2aBzC")

	# grand child of each child
	## left side
	ICON = (By.CSS_SELECTOR, "._325lp img")  # attr(src)
	## right side
	### upper side
	NAME = (By.CSS_SELECTOR, "._35k-1._1adfa._3-8er")
	LAST_MESSAGE_TIME = (By.CSS_SELECTOR, "_15smv")
	### bottom side
	# ARROW_STATUS = (By.CSS_SELECTOR, "._210SC ._1582E .zFnXi")
	LAST_MESSAGE = (By.CSS_SELECTOR, "._2vfYK ._1DB2K ._35k-1._1adfa._3-8er")
	NOTIFICATION = (By.CSS_SELECTOR, "._2TiQe ._38M1B")
