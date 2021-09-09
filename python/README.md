#Copyright 2021 Ben Belland

This is rocket-write, a rabbitmq powered desktop messaging system.

I intend for it to be a pop up app, easily configured, easily run.

Its colours are gay af and i intend the UI to look like your computer
was gargling skittles. I've got the art already from a previous project.
As well as the layout idea and general implementation. Using Qt and Python
for this means it will run on anything, save your ladder logic machine you've
got stuffed in the closet.

My app ecosystem goes supercut(which is a fork of the.terrible.download),
gomess, rocket-write. Supercut works on its own as a standalone web server
albeit simplified. Gomess interacts with the database and will probably
get forked after or during writing this.

You can text supercut now and supercut can text back thanks to gomess
and twilio. So the next layer to my app ecosystem is going to be messaging
the desktop from my phone and vice-versa

What follows is a few ideas:

Have the lines be only the most recent *or selected* message and let the
user expand to read more.

Have each line correspond to a user, rather than a mixed chronological timeline

Make server selection an active choice where you can pick and choose
the people to subscribe to *fancy bubble graphic?*
