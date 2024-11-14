# Instagram Automation Bot

This is a Python script that automates actions on Instagram using Selenium. It allows you to like, comment, and follow accounts based on hashtags. The bot will navigate through the site, select posts, like them, leave comments, and follow users.

## Prerequisites

- Install Python 3.x
- Install Firefox browser
- Download geckodriver (compatible with your Firefox version) from [here](https://github.com/mozilla/geckodriver/releases) and place it in the same directory as this script.
- Create a config.ini file with your Instagram username and password:

```ini
[AUTH]
USERNAME = your_username
PASSWORD = your_password
```

## Usage

1. Make sure you have installed the necessary dependencies (Python, Firefox, geckodriver).
2. Place the `geckodriver` executable in the same directory as this script.
3. Create a `config.ini` file with your Instagram username and password.
4. Run the script using Python:

```shell
python ig_bot.py
```

## Customization

- You can customize the hashtags, comments, and other settings in the `IgBot` class.
- Adjust the sleep times and random ranges to better mimic human behavior.

## Disclaimer

Please use this script responsibly and in accordance with Instagram's terms of service. Automated actions may violate these terms, so use this tool at your own risk.
