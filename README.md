# malaybalay-covid

Simple Dashboard displaying data about COVID-19 in the City of Malaybalay.

## Setup

### Development
1. Clone this repository
2. Install the required development packages using `pipenv install --dev`
3. Create a copy of `local_settings.py.example` and name it `local_settings.py`. Modify it according to you own preference.
4. Run database migration.
5. Run the Django web application

### Production
1. Clone this repository
2. Install the required production packages
3. Set the following environment variables for your deployment:
    * `SECRET_KEY` - This value is the key to securing signed data – it is vital you keep this secure, or attackers could use it to generate their own signed values.
    * `ALLOWED_HOSTS` - Hostnames or IP Addresses that are allowed to access the server.
    * `DATABASE_URL` - URL that will be used to connect on your database.
4. Run database migration.
5. Run the Django web application.

## Requirements
* Database supported by Django (This was developed using MariaDB)
* Python packages specified on the `requirements.txt`
* Pipenv installed on your machine

## License
Code released under the [MIT License](https://gitlab.com/harriebird/malaybalay-covid/-/blob/master/LICENSE)

## Changelog
* pipenv support (28/03/2020)
* production ready configs (28/03/2020)
* Added chart visualization (29/03/2020)
* Added BHERT Hotline (31/03/2020)
* Added Timeline (01/04/2020)
