import re
from bs4 import BeautifulSoup

def get_sub(soup, tag, key):
    tags =[]
    subs = soup.find_all(tag)
    if len(subs) > 0:
        for sub in subs:
            attrs = sub.attrs
            if len(attrs.keys()) > 0:
                for k in attrs.keys():
                    if key in k:
                        tags.append(k.split('-')[1])
    return tags

def get_scheme(scheme):
    tags = []
    soup = BeautifulSoup(scheme, 'html.parser')
    divTags = get_sub(soup, 'div', 'piintu-')
    if len(divTags) > 0:
        for divTag in divTags:
            tags.append(divTag)
        bTags = get_sub(soup, 'b', 'sc-')
        if len(bTags) > 0:
            for bTag in bTags:
                tags.append(bTag)        
        iTags = get_sub(soup, 'i', 'sc-')
        if len(iTags) > 0:
            for iTag in iTags:
                tags.append(iTag)
        uTags = get_sub(soup, 'u', 'sc-')
        if len(uTags) > 0:
            for uTag in uTags:
                tags.append(uTag)
    else:
        bTags = get_sub(soup, 'b', 'piintu-')
        if len(bTags) > 0:
            for bTag in bTags:
                tags.append(bTag)
 
        iTags = get_sub(soup, 'i', 'piintu-')
        if len(iTags) > 0:
            for iTag in iTags:
                tags.append(iTag)

        uTags = get_sub(soup, 'u', 'piintu-')
        if len(uTags) > 0:
            for uTag in uTags:
                tags.append(uTag)

    return tags

def testGet_scheme():
    schemes = [
        "<i piintu-root>Hello</i>",
        '<div><div piintu-rootbear title="Oh My">Hello<i sc-org>World</i></div></div>'
    ]

    for scheme in schemes:
        print(get_scheme(scheme))

testGet_scheme()
