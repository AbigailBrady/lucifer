# lucifer
Curses based Hue control application 

In the long term this is intended to be useful for all types of setups.
Currently it is designed for the author's bedroom, but most things
are customisable.

Settings can be configured in settings.py (including bridge IP address, and
the name of the room to control), keybindings can be configured in bindings.py. 
The keybindings were set up with an OSMC RF remote control in mind; this has a 
USB dongle that plugs into the server and produces keyboard input on the active 
terminal. Some of the keys don't produce distinct keyboards - I have provided a
keymap for linux's loadkeys command.

To run: Just run it on a console. Default keybindings are:

  up/down - select scene
  left/right - select scene within "favorites"
  enter - switch entire lights on/off
  -/= - lighten or darken current settings
  * - mark a scene favorite or not
  home/c - pick two particular scenes

  [letter] - select next scene starting with letter
  page up - restore last set scene
  escape - quit

LIMITATIONS/TODO

  the scene selection commands don't work very well with scenes being
  via another method.  we need to be able to work out what scene is currently
  active: the API doesn't tell us this, but we should be able to compare
  the light's state to the scenes' values and work out a best match.  this then
  will be used as the 'current' scene when going prev/next.  the light data
  for scene's doesn't seem to be in the data returned by .get_api(); i think
  we maybe need to make a GET based api call per scene (this should be cached).

  it won't pick up on changes to scenes/rooms dynamically.  we should watch
  for those.

  need to test behaviour on network fallover.

  can only address one room at a time. this is fine for my (Abigail's) purposes
  but in larger multi-user installations won't do.  what is the UX for this like?
  in an IDEAL world the remote controls would know what room they are in and operate
  on that, but that's probably unfeasible, so they need to be associated with
  rooms on a per-remote-control basis? should there be a buttom to change room?
  i don't like this because it's too easy to press accidentally and not realise 
  you've done it and be accidentally affecting your housemate's room.

  there should be less settings/better defaults
  + auto-discover bridge
  + room selection should default to a room, let you override and let you save
  + default scenes for home/i scenes should be built-in hue scenes, and then
    you should be able to change these somehow in the app
  + faves scenes should save, as well
  + keyboard bindings should show up on screen

there should be a headless version which connects to the USB device for the 
remote control directly, and doesn't need to worry about running on a console
and just gets run as a daemon?

MORE IDEAS

  + a 'random' button (random hsb, not scene)
  + can we use ANSI colour in the app to show the predominant colour of scenes? 
