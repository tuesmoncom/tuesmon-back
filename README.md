# Tuesmon Backend #

[![Kaleidos Project](http://kaleidos.net/static/img/badge.png)](https://github.com/kaleidos "Kaleidos Project")
[![Managed with Tuesmon.com](https://img.shields.io/badge/managed%20with-TUESMON.io-709f14.svg)](https://manage.tuesmon.com/project/tuesmon/ "Managed with Tuesmon.com")
[![Build Status](https://img.shields.io/travis/tuesmoncom/tuesmon-back.svg)](https://travis-ci.org/tuesmoncom/tuesmon-back "Build Status")
[![Coverage Status](https://img.shields.io/coveralls/tuesmoncom/tuesmon-back/master.svg)](https://coveralls.io/r/tuesmoncom/tuesmon-back?branch=master "Coverage Status")


## Contribute to Tuesmon ##

#### Where to start ####

There are many different ways to contribute to Tuesmon's development, just find the one that best fits with your skills. Examples of contributions we would love to receive include:

- **Code patches**
- **Documentation improvements**
- **Translations**
- **Bug reports**
- **Patch reviews**
- **UI enhancements**

Big features are also welcome but if you want to see your contributions included in Tuesmon codebase we strongly recommend you start by initiating a chat though our [mailing list](http://groups.google.co.uk/d/forum/tuesmoncom)


#### Code of Conduct ####

Help us keep the Tuesmon Community open and inclusive. Please read and follow our [Code of Conduct](https://github.com/tuesmoncom/code-of-conduct/blob/master/CODE_OF_CONDUCT.md).


#### License ####

Every code patch accepted in tuesmon codebase is licensed under [AGPL v3.0](http://www.gnu.org/licenses/agpl-3.0.html). You must be careful to not include any code that can not be licensed under this license.

Please read carefully [our license](https://github.com/tuesmoncom/tuesmon-back/blob/master/LICENSE) and ask us if you have any questions as well as the [Contribution policy](https://github.com/tuesmoncom/tuesmon-back/blob/master/CONTRIBUTING.md).


#### Bug reports, enhancements and support ####

If you **need help to setup Tuesmon**, want to **talk about some cool enhancemnt** or you have **some questions**, please write us to our [mailing list](http://groups.google.com/d/forum/tuesmoncom).

If you **find a bug** in Tuesmon you can always report it:

- in our [mailing list](http://groups.google.com/d/forum/tuesmoncom).
- in [github issues](https://github.com/tuesmoncom/tuesmon-back/issues).
- send us a mail to support@tuesmon.com if is a bug related to [manage.tuesmon.com](https://manage.tuesmon.com).
- send a mail to security@tuesmon.com if is a **security bug**.

One of our fellow Tuesmon developers will search, find and hunt it as soon as possible.

Please, before reporting a bug write down how can we reproduce it, your operating system, your browser and version, and if it's possible, a screenshot. Sometimes it takes less time to fix a bug if the developer knows how to find it and we will solve your problem as fast as possible.


#### Documentation improvements ####

We are gathering lots of information from our users to build and enhance our documentation. If you use the documentation to install or develop with Tuesmon and find any mistakes, omissions or confused sequences, it is enormously helpful to report it. Or better still, if you believe you can author additions, please make a pull-request to tuesmon project.

Currently, we have authored three main documentation hubs:

- **[API Docs](https://github.com/tuesmoncom/tuesmon-doc)**: Our API documentation and reference for developing from Tuesmon API.
- **[Installation Guide](https://github.com/tuesmoncom/tuesmon-doc)**: If you need to install Tuesmon on your own server, this is the place to find some guides.
- **[Tuesmon Support](https://github.com/tuesmoncom/tuesmon-doc)**: This page is intended to be the support reference page for the users. If you find any mistake, please report it.


#### Translation ####

We are ready now to accept your help translating Tuesmon. It's easy (and fun!) just access our team of translators with the link below, set up an account in Transifex and start contributing. Join us to make sure your language is covered! **[Help Tuesmon to translate content](https://www.transifex.com/tuesmon-agile-llc/tuesmon-back/ "Help Tuesmon to trasnlatecontent")**


#### Code patches ####

Tuesmon will always be glad to receive code patches to update, fix or improve its code.

If you know how to improve our code base or you found a bug, a security vulnerability or a performance issue and you think you can solve it, we will be very happy to accept your pull-request. If your code requires considerable changes, we recommend you first  talk to us directly. We will find the best way to help.


#### UI enhancements ####

Tuesmon is made for developers and designers. We care enormously about UI because usability and design are both critical aspects of the Tuesmon experience.

There are two possible ways to contribute to our UI:
- **Bugs**: If you find a bug regarding front-end, please report it as previously indicated in the Bug reports section or send a pull-request as indicated in the Code Patches section.
- **Enhancements**: If its a design or UX bug or enhancement we will love to receive your feedback. Please send us your enhancement, with the reason and, if possible, an example. Our design and UX team will review your enhancement and fix it as soon as possible. We recommend you to use our [mailing list](http://groups.google.co.uk/d/forum/tuesmoncom) so we can have a lot of different opinions and debate.
- **Language Localization**: We are eager to offer localized versions of Tuesmon. Some members of the community have already volunteered to work to provide a variety of languages. We are working to implement some changes to allow for this and expect to accept these requests in the near future.



## Setup development environment ##

Just execute these commands in your virtualenv(wrapper):

```
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py sample_data
```

**IMPORTANT: Tuesmon only runs with python 3.5+**

Initial auth data: admin/123123

If you want a complete environment for production usage, you can try the tuesmon bootstrapping
scripts https://github.com/tuesmoncom/tuesmon-scripts (warning: alpha state). All the information about the different installation methods (production, development, vagrant, docker...) can be found here http://tuesmoncom.github.io/tuesmon-doc/dist/#_installation_guide.
