def process(sender, message):
	if "hello:" in message:
		from modules import hello
		hello.process(sender)
	if "mp3:" in message:
		from modules import mp3
		mp3.process(sender, message)
	if "nct:" in message:
		from modules import nct
		nct.process(sender, message)
	if "fb:" in message:
		from modules import fb
		fb.process(sender, message)
	if "help:" in message:
		from modules import help
		help.process(sender)

