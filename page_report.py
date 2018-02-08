"""
The script lists the number of views of each URL provided in the log file.

Each line of this file should contain one entry. 
The script also checks the correctness of each entry using several private functions. 
After the script has been executed, information about the number of incorrect logs will appear.
"""
import sys
import datetime


def __dict_iter(dictionary: dict, key):
    """The auxiliary function allows to increase the number of instances of a given key
     from the dictionary, or creates a key with the number of occurrences
     equal to one if it has not appeared before."""

    if key in dictionary.keys():
        dictionary[key] += 1
    else:
        dictionary[key] = 1


def __validate_ip(IPv4: str):
    """Validate IPv4

    Keyword arguments:
        IPv4 -- string which contain IP (e.g. '100.100.100.100' )
        """

    IPv4 = IPv4.split('.')
    if len(IPv4) != 4:
        raise ValueError('Not enough values in IP adress.')
    for element in IPv4:
        if element.isdigit() is False:
            raise ValueError('Parts of IP adress are not a numbers.')
        if int(element) < 0 or int(element) > 255:
            raise ValueError("Values of IP's parts are not correct")
        return True


def __validate_HTTP_request(HTTP_request: str):
    """ Checking if HTTP request is correct, so if cointain all information.

    Keyword arguments:
        HTTP_request -- str that should looks like "GET http://google.com HTTP://1.1"
           """

    if 'GET' in HTTP_request and 'HTTP/1.1' in HTTP_request and 'http://' in HTTP_request:
        if len(HTTP_request.strip('GET HTTP/1.1 http://')) > 0:
            return True
    raise ValueError('Wrong HTTP request.')


def __validate_HTTP_response_code(HTTP_response_code: int):
    """ Checking correctness of HTTP response code. """
    if HTTP_response_code == 200:
        return True
        # I assume that only 200 is acceptable response (not generally 2**)  #
    else:
        raise ValueError('Http reponse code is not valid.')


def __validate(log: str):
    """ Validation function of log. Checks if argument has right formula:
    <IPv4 address> [<datetime>] " <HTTP request> " <HTTP response code> <bytes sent>
    e.g. "10.10.110.222 [10/Feb/205:14:01:12 +0400] "GET http://google.com HTTP/1.1" 200 1024"
    """

    try:
        temp = log.split('"')
        IPv4_address = temp[0].split(' ')[0]
        date_time = temp[0].split('[')[1].strip('] ')
        HTTP_request = temp[1]
        HTTP_response_code = temp[2].split(' ')[1]
        bytes_sent = temp[2].split(' ')[2]

        __validate_ip(IPv4_address)
        datetime.datetime.strptime(date_time, '%d/%b/%Y:%H:%M:%S %z')
        # For strptime first argument must be a date in a format that is described as second argument.
        # In this case it is "day/month(abbreviated name)/year:hour(24):minutes:seconds UTC offset".
        # If first argument doesn't match, error occurs #
        __validate_HTTP_request(HTTP_request)
        __validate_HTTP_response_code(int(HTTP_response_code))
        int(bytes_sent)  # if bytes_sent could not be a integer error occurs #

    except:
        return False
    return True

links = {}  # main dictionary with links and number of occurrences in log file #
invalid_log = 0
if __name__ == "__main__":
	for line in open(sys.argv[1], 'r'):
	    if __validate(line.strip('\n')) is False:
	        invalid_log += 1
	    else:
	        shortened_log_line = line.split(' HTTP')[0]
	        # finding beginning of link
	        link = shortened_log_line[
	            shortened_log_line.find('http://') + len('http://'):]
	        if link.find('?') != -1:
	            link = link[:link.find('?')]
	        if link[-1] == '/':
	            link = link[:-1]
	        __dict_iter(links, link)
	sorted_links = sorted(
	    links.items(), key=lambda x: (-1 * x[1], x[0]), reverse=(False))
	# Sorting links by number of their occurrences.
	# Trick is to use opposite values of occurrences to sort ascending,
	# and that is because we also want to sort lexicographically when numbers
	# of occurrences are equal . #
	for element in sorted_links:
	    print(element[0], ',', element[1])
	sys.exit('Invalid log lines: ' + str(invalid_log))