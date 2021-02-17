import praw
import config
import time
import os
import random 

subreddit_list = 'copypasta+centrist+dirtbagcenter+enlightenedcentrism+videos+blackpeopletwitter+starterpacks+todayilearned+earthporn+geopolitics'
Alabama = ['Alabama', 'alabama', 'ALABAMA']
Alaska = ['Alaska', 'alaska', 'ALASKA'] 
Arizona = ['Arizona', 'arizona', 'ARIZONA'] 
Arkansas = ['Arkansas', 'arkansas', 'ARKANSAS']
California = ['California', 'california', 'CALIFORNIA']
Colorado = ['Colorado', 'colorado', 'COLORADO']
Connecticut = ['Connecticut', 'connecticut', 'CONNECTICUT']
Delaware = ['Delaware', 'delaware', 'DELAWARE']
Florida = ['Florida', 'florida', 'FLORIDA']
Georgia = ['Georiga', 'georgia', 'GEORGIA']
Hawaii = ['Hawaii', 'hawaii', 'HAWAII']
Idaho = ['Idaho', 'idaho', 'IDAHO']
Illinois = ['Illinois', 'illinois', 'ILLINOIS']
Indiana = ['Indiana', 'indiana', 'INDIANA']
Iowa = ['Iowa', 'iowa', 'IOWA']
Kansas = ['Kansas', 'kansas', 'KANSAS']
Kentucky = ['Kentucky', 'kentucky', 'KENTUCKY']
Louisiana = ['Louisiana', 'louisiana', 'LOUISIANA']
Maine = [' maine', ' Maine', ' MAINE']
Maryland = ['Maryland', 'maryland', 'MARYLAND']
Massachusetts = ['massachusetts', 'Massachusetts', 'MASSACHUSETTS']
Michigan = ['Michigan', 'michigan', 'MICHIGAN']
Minnesota = ['Minnesota', 'minnesota', 'MINNESOTA']
Mississippi = ['Mississippi', 'mississippi', 'MISSISSIPPI']
Missouri = ['Missouri', 'missouri', 'MISSOURI']
Montana = ['Montana', 'montana', 'MONTANA']
Nebraska = ['Nebraska', 'nebraska', 'NEBRASKA']
Nevada = ['Nevada', 'nevada', 'NEVADA']
NewHampshire = ['New Hampshire', 'new hamphsire']
NewJersey = ['New Jersey', 'new jersey']
NewMexico = ['New Mexico', 'new mexico']
NewYork = ['New York', 'new york']
NorthCarolina = ['North Carolina', 'north carolina']
NorthDakota = ['North Dakota', 'north dakota']
Ohio = ['ohio', 'Ohio', 'OHIO']
Oklahoma = ['Oklahoma', 'oklahoma', 'OKLAHOMA']
Oregon = ['Oregon', 'oregon', 'OREGON']
Pennsylvania = ['Pennsylvania', 'pennsylvania', 'PENNSYLVANIA']
RhodeIsland = ['Rhode Island', 'rhode island']
SouthCarolina = ['South Carolina', 'south carolina']
SouthDakota = ['South Dakota', 'south dakota']
Tennessee = ['Tennessee', 'tennessee', 'TENNESSEE']
Texas = ['Texas', 'texas', 'TEXAS']
Utah = ['Utah', 'utah', 'UTAH']
Vermont = ['Vermont', 'vermont', 'VERMONT']
Virginia = ['Virginia', 'virginia', 'VIRGINIA']
Washington = ['Washington state', 'washington state']
WestVirginia = ['West Virginia', 'west virginia']
Wisconsin = ['Wisconsin', 'wisconsin', 'WISCONSIN']
Wyoming = ['Wyoming', 'wyoming', 'WYOMING']

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "State Fact Bot")
	print "Logged in!"

	return r

def run_bot(r, replied):
	for comment in r.subreddit(subreddit_list).comments(limit=100):
		if comment.id not in replied and comment.author != r.user.me():
			if any(key in comment.body for key in Alabama):
				response = random.choice(open('Alabama.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Alabama*, so here's a fact about Alabama:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Alaska):
				response = random.choice(open('Alaska.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Alaska*, so here's a fact about Alaska:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Arizona):
				response = random.choice(open('Arizona.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Arizona*, so here's a fact about Arizona:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Arkansas):
				response = random.choice(open('Arkansas.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Arkansas*, so here's a fact about Arkansas:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in California):
				response = random.choice(open('California.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *California*, so here's a fact about California:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Colorado):
				response = random.choice(open('Colorado.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Colorado*, so here's a fact about Colorado:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Connecticut):
				response = random.choice(open('Connecticut.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Connecticut*, so here's a fact about Connecticut:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Delaware):
				response = random.choice(open('Delaware.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Delaware*, so here's a fact about Delaware:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Florida):
				response = random.choice(open('Florida.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Florida*, so here's a fact about Florida:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Georgia):
				response = random.choice(open('Georgia.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Georgia*, so here's a fact about Georgia:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Hawaii):
				response = random.choice(open('Hawaii.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Hawaii*, so here's a fact about Hawaii:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Idaho):
				response = random.choice(open('Idaho.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Idaho*, so here's a fact about Idaho:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Illinois):
				response = random.choice(open('Illinois.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Illinois*, so here's a fact about Illinois:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Indiana):
				response = random.choice(open('Indiana.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Indiana*, so here's a fact about Indiana:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Iowa):
				response = random.choice(open('Iowa.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Iowa*, so here's a fact about Iowa:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Kansas):
				response = random.choice(open('Kansas.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Kansas*, so here's a fact about Kansas:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Kentucky):
				response = random.choice(open('Kentucky.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Kentucky*, so here's a fact about Kentucky:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Louisiana):
				response = random.choice(open('Louisiana.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Louisiana*, so here's a fact about Louisiana:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Maine):
				response = random.choice(open('Maine.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Maine*, so here's a fact about Maine:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Maryland):
				response = random.choice(open('Maryland.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Maryland*, so here's a fact about Maryland:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Massachusetts):
				response = random.choice(open('Massachusetts.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Massachusetts*, so here's a fact about Massachusetts:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Michigan):
				response = random.choice(open('Michigan.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Michigan*, so here's a fact about Michigan:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Minnesota):
				response = random.choice(open('Minnesota.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Minnesota*, so here's a fact about Minnesota:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Mississippi):
				response = random.choice(open('Mississippi.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Mississippi*, so here's a fact about Mississippi:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Missouri):
				response = random.choice(open('Missouri.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Missouri*, so here's a fact about Missouri:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Montana):
				response = random.choice(open('Montana.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Montana*, so here's a fact about Montana:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Nebraska):
				response = random.choice(open('Nebraska.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Nebraska*, so here's a fact about Nebraska:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Nevada):
				response = random.choice(open('Nevada.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Nevada*, so here's a fact about Nevada:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in NewHampshire):
				response = random.choice(open('NewHampshire.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *New Hampshire*, so here's a fact about New Hampshire:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in NewJersey):
				response = random.choice(open('NewJersey.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *New Jersey*, so here's a fact about New Jersey:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in NewMexico):
				response = random.choice(open('NewMexico.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *New Mexico*, so here's a fact about New Mexico:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in NewYork):
				response = random.choice(open('NewYork.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *New York*, so here's a fact about New York:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in NorthCarolina):
				response = random.choice(open('NorthCarolina.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *North Carolina*, so here's a fact about North Carolina:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in NorthDakota):
				response = random.choice(open('NorthDakota.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *North Dakota*, so here's a fact about North Dakota:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Ohio):
				response = random.choice(open('Ohio.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Ohio*, so here's a fact about Ohio:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Oklahoma):
				response = random.choice(open('Oklahoma.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Oklahoma*, so here's a fact about Oklahoma:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Oregon):
				response = random.choice(open('Oregon.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Oregon*, so here's a fact about Oregon:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Pennsylvania):
				response = random.choice(open('Pennsylvania.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Pennsylvania*, so here's a fact about Pennsylvania:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in RhodeIsland):
				response = random.choice(open('RhodeIsland.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Rhode Island*, so here's a fact about Rhode Island:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in SouthCarolina):
				response = random.choice(open('SouthCarolina.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *South Carolina*, so here's a fact about South Carolina:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in SouthDakota):
				response = random.choice(open('SouthDakota.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *South Dakota*, so here's a fact about South Dakota:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Tennessee):
				response = random.choice(open('Tennessee.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Tennessee*, so here's a fact about Tennessee:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Texas):
				response = random.choice(open('Texas.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Texas*, so here's a fact about Texas:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Utah):
				response = random.choice(open('Utah.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Utah*, so here's a fact about Utah:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Vermont):
				response = random.choice(open('Vermont.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Vermont*, so here's a fact about Vermont:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Virginia):
				response = random.choice(open('Virginia.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Virginia*, so here's a fact about Virginia:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Washington):
				response = random.choice(open('Washington.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Washington*, so here's a fact about Washington:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in WestVirginia):
				response = random.choice(open('WestVirginia.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *West Virginia*, so here's a fact about West Virginia:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Wisconsin):
				response = random.choice(open('Wisconsin.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Wisconsin*, so here's a fact about Wisconsin:\n\n ") 
				reply += (response)
				comment.reply(reply)
				print("Replied to: " + comment.id)
				replied.append(comment.id)

			elif any(key in comment.body for key in Wyoming):
				response = random.choice(open('Wyoming.txt').readlines())
				reply = ("*Beep boop I'm a bot.* You mentioned *Wyoming*, so here's a fact about Wyoming:\n\n ") 
				reply += (response)
				comment.reply(reply)

				print("Replied to: " + comment.id)
				replied.append(comment.id)

		with open ("replied.txt", "a") as f:
			f.write(comment.id + "\n")
	time.sleep(20)

def get_saved_comments():
	if not os.path.isfile("replied.txt"):
		replied = []
	else:
		with open("replied.txt", "r") as f:
			replied = f.read()
			replied = replied.split("\n")
			replied = filter(None, replied)

	return replied

r = bot_login()
replied = get_saved_comments()

while True:
	run_bot(r, replied)