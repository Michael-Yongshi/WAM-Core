# Warhammer Army Manager (WAM)

An application in order to create, update, view and save your warband details for use, including but not limited to, Mordheim and Killteam boardgames. Using this application there is no need anymore for manually calculating skills or looking up your warbands details, including references to all item, spells, abilities, etc. that are ingame.

In addition you can add your own warbands, items, rules, etc. for use in more custom made games.

## Roadmap

Import wildcards
- Remove the wildcards from the import statements

Inventory and items
- Split inventory again in Treasury object and in an itemlist seperately, as only the warband itself can have gold and wyrd, it makes for more elegancy to split these, although should have no practical implications

Magic
- Add dedicated Magic class and add a magic attribute to character and item (potentially also an item could enable a character to use a spell). Magic is very different from abilities and therefore warrant a special class

Generate overviews of warband, herolists, squads, etc. easily.

Add events
- Characters decorative events
- Characters history events of changes
- Item decorative events

Unique names
- Item name change, although this is kind of already possible
- Henchman, similar to item name change

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

