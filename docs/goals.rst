Project Goals
=============

Unorganized goals
-----------------

* Direct Objects - This goes without saying.  Direct objects are needed for actions to do anything to other objects.  In a sentence, the direct object is the thing you are performing the action on.  Same goes here.  When the user says "open the door", the door is the direct object.
* Prepositional phrases - This will be necessary for situations like "open the door with the key".  "with the key" is the prepositional phrase, where the key is the prepositional object telling us what to open the door with.
* Word filtering - Removing useless words that the user my enter.  These are words that may get in the way when parsing the user's command.  If the user enters "go to the room", the words "to" and "the" are unnecessary and get in the way when checking for direct objects for the go action.
* Alias system - Basically a way for the user to input "open chest" if there's only one chest in the location
    * If multiple chests appeared in the location, then the game would ask the player which one
* Movement system - A way for the player to be able to move from one location to another
* Container system - A way to store objects inside container objects
    * The floor/ground would be considered a container that the player can "drop" objects to
    * Tables and desks would also be considered containers
* Dynamic prompt generation - Generate a prompt based on the conditions of the player's location.  The prompt would be printed when the player loads, when they enter another location, or when the user enter's "look around"
* Looking/Inspection system - A way to get "visual" based information about a location, object, or other things.  Saying "inspect phone" would mean the sames as "look at phone", while a simple "inspect" would mean the same as "look around"
* Scripted NPCs - NPCs for the player to interact with.  Most likely need to be created individually to created different scripts for different NPCs
