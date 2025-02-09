import ssl
import certifi
import nltk
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
nltk.download('punkt_tab')
