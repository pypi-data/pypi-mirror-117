#!/usr/bin/env python3

"""
This Python script is designed to query multiple online repositories for the
antonyms associated with a specific word.
"""
__author__ = 'John Bumgarner'
__date__ = 'October 15, 2020'
__status__ = 'Production'
__license__ = 'MIT'
__copyright__ = "Copyright (C) 2020 John Bumgarner"

##################################################################################
# Date Completed: October 15, 2020
# Author: John Bumgarner
#
# Date Last Revised: August 23, 2021
# Revised by: John Bumgarner
##################################################################################

##################################################################################
# “AS-IS” Clause
#
# Except as represented in this agreement, all work produced by Developer is
# provided “AS IS”. Other than as provided in this agreement, Developer makes no
# other warranties, express or implied, and hereby disclaims all implied warranties,
# including any warranty of merchantability and warranty of fitness for a particular
# purpose.
##################################################################################

##################################################################################
# Python imports required for basic operations
##################################################################################
import bs4
import logging
import requests
import traceback
from bs4 import BeautifulSoup
from wordhoard.utilities import basic_soup, caching, cleansing, word_verification

logger = logging.getLogger(__name__)


class Antonyms(object):
    """
    This class is used to query multiple online repositories for the antonyms associated
    with a specific word.

    Usage: antonym = Antonyms(word)
           results = antonym.find_antonyms()
    """

    def __init__(self, word):
        """
        :param word: string containing the variable to search for
        """
        self._word = word

    def _validate_word(self):
        """
        This function is designed to validate that the syntax for
        a string variable is in an acceptable format.

        :return: True or False
        :rtype: boolean
        """
        valid_word = word_verification.validate_word_syntax(self._word)
        if valid_word:
            return valid_word
        else:
            logger.error(f'The word {self._word} was not in a valid format.')
            logger.error(f'Please verify that the word {self._word} is spelled correctly.')

    def _check_cache(self):
        check_cache = caching.cache_antonyms(self._word)
        return check_cache

    def _update_cache(self, antonyms):
        caching.insert_word_cache_antonyms(self._word, antonyms)
        return

    def find_antonyms(self):
        """
        This function queries multiple online repositories to discover antonyms
        associated with the specific word provided to the Class Antonyms.
        The antonyms are deduplicated and sorted alphabetically.

        :returns:
            antonyms: list of antonyms

        :rtype: list
        """
        valid_word = self._validate_word()
        if valid_word:
            check_cache = self._check_cache()
            if check_cache is False:
                antonyms_01 = self._query_synonym_com()
                antonyms_02 = self._query_thesaurus_com()
                antonyms = ([x for x in [antonyms_01, antonyms_02] if x is not None])
                antonyms_results = cleansing.flatten_multidimensional_list(antonyms)
                return sorted(set(antonyms_results))
            else:
                antonyms = cleansing.flatten_multidimensional_list([val for val in check_cache.values()])
                return sorted(set(antonyms))

    def _query_synonym_com(self):
        """
        This function queries synonym.com for antonyms associated
        with the specific word provided to the Class Antonyms.

         :returns:
            antonyms: list of antonyms

        :rtype: list

        :raises
            AttributeError: Raised when an attribute reference or assignment fails.

            KeyError: Raised when a mapping (dictionary) key is not found in the set of existing keys.

            TypeError: Raised when an operation or function is applied to an object of inappropriate type.

            bs4.FeatureNotFound: raised by the BeautifulSoup constructor if no parser with the requested features
            is found
        """
        try:
            results_antonyms = basic_soup.get_single_page_html(f'https://www.synonym.com/synonyms/{self._word}')
            soup = BeautifulSoup(results_antonyms, "lxml")
            status_tag = soup.find("meta", {"name": "pagetype"})
            if status_tag.attrs['content'] == '404':
                logger.error(f'synonym.com had no reference for the word {self._word}')
                logger.error(f'Please verify that the word {self._word} is spelled correctly.')
            elif status_tag.attrs['content'] == 'Term':
                antonyms_class = soup.find('div', {'data-section': 'antonyms'})
                antonyms = [word.text for word in antonyms_class.find('ul', {'class': 'section-list'}).find_all('li')]
                if antonyms:
                    antonyms = sorted([x.lower() for x in antonyms])
                    self._update_cache(antonyms)
                    return antonyms
                else:
                    logger.error(f'The word {self._word} no antonyms on synonym.com.')
        except bs4.FeatureNotFound as error:
            logger.error('An error occurred in the following code segment:')
            logger.error(''.join(traceback.format_tb(error.__traceback__)))
        except AttributeError as error:
            logger.error('An AttributeError occurred in the following code segment:')
            logger.error(''.join(traceback.format_tb(error.__traceback__)))
        except KeyError as error:
            logger.error('A KeyError occurred in the following code segment:')
            logger.error(''.join(traceback.format_tb(error.__traceback__)))
        except TypeError as error:
            logger.error('A TypeError occurred in the following code segment:')
            logger.error(''.join(traceback.format_tb(error.__traceback__)))

    def _query_thesaurus_com(self):
        """
        This function queries thesaurus.com for antonyms associated
        with the specific word provided to the Class Antonyms.

        :returns:
            antonyms: list of antonyms

        :rtype: list

        :raises

            IndexError: Raised when a sequence subscript is out of range.

            requests.ConnectionError: Raised when a connection error has occurred.

            requests.HTTPError: Raised when an HTTP error has occurred.

            requests.RequestException: Raised when an unknown error has occurred.

            requests.Timeout: Raised when the request timed out.
        """
        try:
            req = requests.get(f'https://tuna.thesaurus.com/pageData/{self._word}',
                               headers=basic_soup.http_headers,
                               allow_redirects=True, verify=True, timeout=30)
            if '{"data":null}' not in req.text:
                dict_antonyms = req.json()['data']['definitionData']['definitions'][0]['antonyms']
                if len(dict_antonyms) > 0:
                    antonyms = sorted([r["term"].lower() for r in dict_antonyms])
                    self._update_cache(antonyms)
                    return antonyms
            else:
                logger.error(f'The word {self._word} was not found on thesaurus.com.')
        except requests.HTTPError as error:
            logger.error('A HTTP error has occurred.')
            logger.error(''.join(traceback.format_tb(error.__traceback__)))
        except requests.ConnectionError as error:
            if requests.codes:
                'Failed to establish a new connection'
                logger.error(''.join(traceback.format_tb(error.__traceback__)))
        except requests.Timeout as error:
            logger.error('A connection timeout has occurred.')
            logger.error(''.join(traceback.format_tb(error.__traceback__)))
        except requests.RequestException as error:
            logger.error('An ambiguous exception occurred.')
            logger.error(''.join(traceback.format_tb(error.__traceback__)))
