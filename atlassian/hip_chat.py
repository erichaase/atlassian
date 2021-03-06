import collections
import json
import re
import urllib
from bs4 import BeautifulSoup
import HTMLParser

def get_properties (message):
    """
    Processes a given chat message to identify particular properties: mentions,
    emoticons and links. See the README.md file for more detailed documentation.

    Args:
        message (str): the chat message to process
    Returns:
        str: json data describing the properties of the message
    Raises:
        TypeError: if message parameter is not a string
    Considerations:
        Two approaches involving a tradeoff between performance and readability:

        1. Scan message *for each* property's regular expression (more readable code)
        2. Scan message *once* using a more complex regular expression (better performance)

        I choose to implement #2 so that the solution scales better
    """

    # validate message input data
    if type(message) != str:
        raise TypeError("message parameter must be a string")

    # data structure that we're going to return (JSON)
    properties = collections.defaultdict(list)

    # regular expressions used to extract properties from message
    REG_EXP = {
        "mentions"  : r"@\w+",
        "emoticons" : r"\(\w+?\)",
        "links"     : r"https?://[^\s]+"
    }
    """
    For simplicity, assume that 'links' use the http(s) URL scheme.
    The format of a URL can be very involved. A more correct, general approach
    would be to include multiple schemes, follow the RFC for URL formats (RFC 3986, 1808), etc.
    This would yield a complex regular expression outside the scope of this exercise.
    """

    # regular expression pattern used for search
    pattern = r"%s|%s|%s" % (REG_EXP["mentions"], REG_EXP["emoticons"], REG_EXP["links"])

    for match in re.findall(pattern, message):
        # setup key/value variables for properties dictionary
        key, value = None, None

        if re.match(REG_EXP["mentions"], match):
            key   = "mentions"
            value = match[1:] # "@eric"
        elif re.match(REG_EXP["emoticons"], match):
            key   = "emoticons"
            value = match[1:-1] # "(smiley)"
        elif re.match(REG_EXP["links"], match):
            url   = match # "http://twitter.com/"

            # get title of URL
            title = None
            try:
                f     = urllib.urlopen(url)
                html  = f.read()
                title = BeautifulSoup(html).title.string
            except IOError as e:
                sys.stderr.write("I/O error({0}): {1}\n".format(e.errno, e.strerror))
                continue
            except HTMLParser.HTMLParseError as e:
                sys.stderr.write("HTMLParseError error({0}): {1}\n".format(e.errno, e.strerror))
                continue
            finally:
                f.close()

            key = "links"
            value = {
                "url"   : url,
                "title" : title
            }
        else:
            sys.stderr.write("warning: the following match wasn't processed: {0}\n".format(match))
            continue

        # store processed key/value variables in properties *defaultdict*
        properties[key].append(value)

    return json.dumps(properties)
