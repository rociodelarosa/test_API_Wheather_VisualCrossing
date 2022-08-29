"""
This script has functions that connect to the Wheather VisualCrossing API.
The obtained data are stored in csv files.
"""

import csv
import codecs
import urllib.request
import urllib.error
import sys


def data_weather_loc(location, startdate, enddate, contenttype='csv', unitgroup='metric', include="days"):
    """Obtains data from the weather API via location."""
    baseurl = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

    apikey='7CKN3MUH7QBN7HYWKNPY6S69K'
    print('')
    print(' - Requesting weather : ')

    #basic query including location
    apiquery=baseurl + location

    #append the start and end date if present
    if startdate:
        apiquery+="/"+startdate
        if enddate:
            apiquery+="/"+enddate

    #Url is completed. Now add query parameters (could be passed as GET or POST)
    apiquery+="?"

    #append each parameter as necessary
    if unitgroup:
        apiquery+="&unitGroup="+unitgroup

    if contenttype:
        apiquery+="&contentType="+contenttype

    if include:
        apiquery+="&include="+include

    apiquery+="&key="+apikey

    print(' - Running query URL: ', apiquery)
    print()

    try:
        csvbytes = urllib.request.urlopen(apiquery)
    except urllib.error.HTTPError as exc:
        errorinfo= exc.read().decode()
        print('Error code: ', exc.code, errorinfo)
        sys.exit()
    except  urllib.error.URLError as exc:
        errorinfo= exc.read().decode()
        print('Error code: ', exc.code, errorinfo)
        sys.exit()


    # Parse the results as CSV
    csvtext = csv.reader(codecs.iterdecode(csvbytes, 'utf-8'))

    # Gets the header
    header = next(csvtext)

    # Obtains the data
    rows = []
    for row in csvtext:
        rows.append(row)

    startdate = startdate.replace(':', '')
    enddate = enddate.replace(':', '')

    # Write the file to csv
    filename = r'C:\Users\Chio\Documents\pruebas\test_houm\prueba\pregunta_3\weather_{}_{}_{}.csv'.format(location, startdate, enddate)

    with open(filename, 'w', newline="", encoding='utf-8') as file:
        csvwriter = csv.writer(file, delimiter=';') # 2. create a csvwriter object
        csvwriter.writerow(header) # 4. write the header
        csvwriter.writerows(rows) # 5. write the rest of the data


def data_weather_latlon(latitude, longitude, startdate, enddate, question, contenttype='csv', unitgroup='metric', include="days"):
    """Obtains weather API data through latitude and longitude."""
    baseurl = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

    apikey='7CKN3MUH7QBN7HYWKNPY6S69K'
    # print('')
    # print(' - Requesting weather : ')

    #basic query including location
    apiquery=baseurl + latitude + '%2C' + longitude

    #append the start and end date if present
    if startdate:
        apiquery+="/"+startdate
        if enddate:
            apiquery+="/"+enddate

    #Url is completed. Now add query parameters (could be passed as GET or POST)
    apiquery+="?"

    #append each parameter as necessary
    if unitgroup:
        apiquery+="&unitGroup="+unitgroup

    if contenttype:
        apiquery+="&contentType="+contenttype

    if include:
        apiquery+="&include="+include

    apiquery+="&key="+apikey

    # print(' - Running query URL: ', apiquery)
    # print()

    try:
        csvbytes = urllib.request.urlopen(apiquery)
    except urllib.error.HTTPError as exc:
        errorinfo= exc.read().decode()
        print('Error code: ', exc.code, errorinfo)
        sys.exit()
    except  urllib.error.URLError as exc:
        errorinfo= exc.read().decode()
        print('Error code: ', exc.code, errorinfo)
        sys.exit()


    # Parse the results as CSV
    csvtext = csv.reader(codecs.iterdecode(csvbytes, 'utf-8'))

    # Gets the header
    header = next(csvtext)

    # Obtains the data
    rows = []
    for row in csvtext:
        rows.append(row)

    startdate = startdate.replace(':', '')
    enddate = enddate.replace(':', '')

    # Write the file to csv
    filename = r'C:\Users\Chio\Documents\pruebas\test_houm\prueba\pregunta_{}\weather_{}_{}_{}_{}.csv'.format(question, latitude, longitude, startdate, enddate)

    with open(filename, 'w', newline="", encoding='utf-8') as file:
        csvwriter = csv.writer(file, delimiter=';') # 2. create a csvwriter object
        csvwriter.writerow(header) # 4. write the header
        csvwriter.writerows(rows) # 5. write the rest of the data
