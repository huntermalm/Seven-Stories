# Change Log

## [v0.3.0](https://github.com/huntermalm/SevenStories/tree/v0.3.0) (2017-08-03)

### Additions

* Start of location system
* Moving system through the new action function: go
* Working direct object system:

    > go to the second room

* Word filter system to remove unnecessary words that may interfere with the text parser


## [v0.2.0](https://github.com/huntermalm/SevenStories/tree/v0.2.0) (2017-07-31)

### Additions

* Update system to automatically update player save when loading a player
* Start to a location system.  For now, there is only one location called "First room" which is the player's initial location
* New action "location" to display the player's current location


## [v0.1.1](https://github.com/huntermalm/SevenStories/tree/v0.1.1) (2017-07-30)

### Additions

* Option to quit in the main menu
* Temporary game icon

## [v0.1a1](https://github.com/huntermalm/SevenStories/tree/v0.1a1) (2017-07-29)

This is the first initial pre-release.  The contents of this release are intended to demonstrate the basic core game functionality at a very simple, but working stage.  Below are the features presented in this release:

### Additions

* A text parser capable of handling multiple actions in a single command.
* Text parser removes various punctuation characters from user's command.
* A game loop to continuously invoke the text parser.  The loop can be stopped with the "quit" action.
* Saving/loading/deleting/resetting characters in a main menu-like interface.
* The saves directory is operating system dependent:
  * Windows: "%LocalAppData%\SevenStories\saves"
  * Linux: "~/.SevenStories/saves"
* Four usable actions: name, health, save, quit
* A reminder to save in the event that a user tries to quit and the previous action was not "save".
