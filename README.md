### Donation 

<a href="https://ko-fi.com/AuraMoon55" alt="Donate!"> <img src="https://aleen42.github.io/badges/src/paypal.svg" /> </a>


**A modular Telegram Python bot running on python3 with a sqlalchemy, redis, telethon.**

## How to set up/deploy.

<details>
  <summary>Step to self Host!!</summary>

## Setting up the bot (Read this before trying to use!):

Please make sure to use python3.6, as I cannot guarantee everything will work as expected on older Python versions!
This is because markdown parsing is done by iterating through a dict, which is ordered by default in 3.6.

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AuraMoon55/voilet.git)

### Configuration

There are two possible ways of configuring your bot: a config.py file, or ENV variables.

The preferred version is to use a `config.py` file, as it makes it easier to see all your settings grouped together.
This file should be placed in your `zeldris` folder, alongside the `__main__.py` file. This is where your bot token will
be loaded from, as well as your database URI (if you're using a database), and most of your other settings.

It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all
defaults set in the sample_config, hence making it easier to upgrade.

An example `config.py` file could be:

```
from zeldris.sample_config import Config

class Development(Config):
    OWNER_ID = 123456789  # your telegram ID
    OWNER_USERNAME = "username"  # your telegram username
    API_KEY = "your bot api key"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-10007372' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1234, 1234]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
```

If you can't have a config.py file (EG on Heroku), it is also possible to use environment variables. The following env
variables are supported:

- `ENV`: Setting this to ANYTHING will enable env variables

- `TOKEN`: Your bot token, as a string.
- `OWNER_ID`: An integer of consisting of your owner ID
- `OWNER_USERNAME`: Your username

- `DATABASE_URL`: Your database URL
- `MESSAGE_DUMP`: optional: a chat where your replied saved messages are stored, to stop people deleting their old
- `LOAD`: Space-separated list of modules you would like to load
- `NO_LOAD`: Space-separated list of modules you would like NOT to load
- `WEBHOOK`: Setting this to ANYTHING will enable webhooks when in env mode messages
- `URL`: The URL your webhook should connect to (only needed for webhook mode)

- `SUDO_USERS`: A space-separated list of user_ids which should be considered sudo users
- `DEV_USERS`: A space-separated list of user_ids which should be considered dev users
- `SUPPORT_USERS`: A space-separated list of user_ids which should be considered support users (can gban/ungban, nothing
  else)
- `WHITELIST_USERS`: A space-separated list of user_ids which should be considered whitelisted - they can't be banned.
- `DONATION_LINK`: Optional: link where you would like to receive donations.
- `CERT_PATH`: Path to your webhook certificate
- `PORT`: Port to use for your webhooks
- `DEL_CMDS`: Whether to delete commands from users which don't have rights to use that command
- `STRICT_GBAN`: Enforce gbans across new groups as well as old groups. When a gbanned user talks, he will be banned.
- `WORKERS`: Number of threads to use. 8 is the recommended (and default) amount, but your experience may vary.
  __Note__ that going crazy with more threads won't necessarily speed up your bot, given the large amount of sql data
  accesses, and the way python asynchronous calls work.
- `BAN_STICKER`: Which sticker to use when banning people.
- `ALLOW_EXCL`: Whether to allow using exclamation marks ! for commands as well as /.

### Python dependencies

Install the necessary Python dependencies by moving to the project directory and running:

`pip3 install -r requirements.txt`.

This will install all the necessary python packages.

### Database

If you wish to use a database-dependent module (eg: locks, notes, userinfo, users, filters, welcomes), you'll need to
have a database installed on your system. I use Postgres, so I recommend using it for optimal compatibility.

In the case of Postgres, this is how you would set up a database on a Debian/ubuntu system. Other distributions may
vary.

- install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the Postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you need to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal. By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever DB you're using (e.g. Postgres, MySQL, SQLite, `etc.)
repeat for your username, password, hostname (localhost?), port (5432?), and DB name.

Or, register on [ElephantSQL](https://www.elephantsql.com/) for free Postgresql. Learn for your self, We won't teach you
anything.
</details>

## Credits

- [Skyleebot](https://github.com/SensiPeeps/skyleebot) Based this Bot.
- [1maverick1](https://github.com/1maverick1) for many stuffs.
- [AyraHikari](https://github.com/AyraHikari) for weather modules and some other stuffs.
- [RealAkito](https://github.com/RealAkito) for reverse search modules.
- [MrYacha](https://github.com/MrYacha) for connections module.
- [ATechnoHazard](https://github.com/SphericalKat) for many stuffs.
- [corsicanu](https://github.com/corsicanu) and nunopenim for android modules.
- [Saitama](https://github.com/AnimeKaizoku/SaitamaRobot) for anime modules and other stuffs.
- [Kigyō](https://github.com/AnimeKaizoku/EnterpriseALRobot) for greetings modules.
- [UserIndoBot](https://github.com/userbotindo/UserIndoBot) for any other stuffs.
- Thanks to Everyone who has [contributed](https://github.com/AuraMoon55/Violet/graphs/contributors) to this Project!

## Projects!

```
Violet is part of the [Hunters Association](https://github.com/orgs/The-hunter-association) project.
```
