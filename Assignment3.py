#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 3, Assignment 3 (Text Processing)"""

import re
import urllib2
import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="Please enter the URL for a data")
args = parser.parse_args()

def main():
    """This is a new function which putes downloaddata and processdata into one script to
    enable a commend line"""

    if not args.url:
        raise SystemExit
    try:
        data = downloadData(args.url)
    except urllib2.URLError:
        print 'This is an invalid URL. Please enter a valid URL.'
        raise
    else:
        processData(data)
        
def downloadData(url):
    """This is new function to open a given URL."""
    
    csvfile = urllib2.urlopen(url)
    return csvfile

def processData(csvfile):
    """This function opens csv file."""

    readfile = csv.reader(csvfile)
    linecount = 0
    imgcount = 0
    
    firefox = ['Firefox', 0]
    chrome = ['Google Chrome', 0]
    safari = ['Safari', 0]
    IE = ['Internet Explorer', 0]
    
    for line in readfile:
        linecount += 1
        if re.search("firefox", line[2], re.I):
            firefox[1] += 1
        elif re.search(r"MSIE", line[2]):
            IE[1] += 1
        elif re.search(r"Chrome", line[2]):
            chrome[1] += 1
        elif re.search(r"Safari", line[2]) and not re.search("Chrome", line[2]):
            safari[1] += 1
        if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
            imgcount += 1

    img_hit_pct = (float(imgcount) / linecount) * 100

    brwsr_count = [chrome, IE, safari, firefox]

    top_brwsr = 0
    top_name = ' '
    for b in brwsr_count:
        if b[1] > top_brwsr:
            top_brwsr = b[1]
            top_name = b[0]
        else:
            continue

    imghits_popbrowser = ('There were {} page hits today.'
           'Image requests account for {}% of hits.'
           '\n{} has the most hits with {}.').format(linecount,
                                                           img_hit_pct,
                                                           top_name,
                                                           top_brwsr)
    print imghits_popbrowser

if __name__ == '__main__':
    main()
