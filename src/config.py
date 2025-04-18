"""
Configuration settings for the Social Media Analysis project.
"""

# Twitter API credentials
TWITTER_API_KEY = '8RQ5xPiDzAg1duMVpj9pWYEdX'
TWITTER_API_KEY_SECRET = 'BqfcElqH5G6yAFHafuMQWO5ljp8Bosa402DzldWgc3mzCOSrSB'
TWITTER_ACCESS_TOKEN = '1570146620653850629-erndFgwUuLXuK8prEhhrpkqlBUICih'
TWITTER_ACCESS_TOKEN_SECRET = 'hwjy8IzsfECPVje0SAzdg3YorFifjAZbpBBgmLxBxnGVc'

# Search parameters
DEFAULT_TWEET_COUNT = 300
DEFAULT_START_DATE = '2019-12-12'

# Search queries
PRO_VACCINE_HASHTAGS = [
    '#GetVaccinated',
    '#VaccineMandate',
    '#VaccinesWork',
    '#FullyVaccinated',
    'GetVaccinatedOrGetCovid'
]

ANTI_VACCINE_HASHTAGS = [
    '#vaccineinjury',
    '#NoVaccineMandates',
    '#SayNoToVaccineMandate',
    '#NoVaxMandates',
    '#AntiVaccine'
]

# File paths
DATA_DIR = '../data'
FIGURES_DIR = '../figures' 