# SevenStories

Text-adventure game in very early stages of development.

### Latest Release Notes

[**v0.1a1**](https://github.com/huntermalm/SevenStories/releases/tag/v0.1a1)

This is the first initial pre-release.  The contents of this release are intended to demonstrate the basic core game functionality at a very simple, but working stage.  Below are the features presented in this release:

##### Additions

* A text parser capable of handling multiple actions in a single command.
* Text parser removes various punctuation characters from user's command.
* A game loop to continuously invoke the text parser.  The loop can be stopped with the "quit" action.
* Saving/loading/deleting/resetting characters in a main menu-like interface.
* The saves directory is operating system dependant:
  * Windows: "%LocalAppData%\SevenStories\saves"
  * Linux: "~/.SevenStories/saves"
* Four usable actions: name, health, save, quit
* A reminder to save in the event that a user tries to quit and the previous action was not "save".


### Documentation

A more extensive understanding of the game's functionality can be observed by reading the documentation, provided [here](http://sevenstories.readthedocs.io/en/latest/index.html).


### Releases

Click [here](https://github.com/huntermalm/SevenStories/releases) for releases.
