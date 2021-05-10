# MC-Whitelist-discord-bot

This is a project that I've created for a streamer to link a discord server to minecraft. I was looking for a plugin that links twitch/discord with mc to create a sub whitelist and I have nothing found. All I found is a discord minecraft plugin that only works with online-mode: true. 

This whitelist bot works with **twitch and discord integration**. You have to link twitch with your discord server to know who is sub and who not. Every time you send a message to a specific chat the bot takes that message and if it has the sub role it takes it and send it to minecraft with the whitelist add command. If the user send another nickname the bot will send a message saying that you have already sent a nickname, because the bot automatically assign a whitelist role to every user that send a nickname. **It's important that on that nick channel you only send the nickname** and not some @ or _hi, my nick is..._ because the bot will take all the text and assign it to whitelist.

For making it work you have to pip install discord.py and mcrcon. It's easy to create a role system with that code, I mean, if a follower send a nickname it set a follower rank in minecraft and if a sub send a nickname, set a sub role.
