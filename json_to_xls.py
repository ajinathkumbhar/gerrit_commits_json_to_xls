import json
from openpyxl import workbook
import codecs


def process_json():
    try:
        j_file = codecs.open("commit_list.json",'rU','utf-8')
    except IOError as err:
        print 'failed to open json file ' + str(err)
    for line in j_file:
        print line
        data = json.loads(line)
        print type(data)
        ownerdata = data['owner']
        print type(ownerdata)
        for key, val in ownerdata.iteritems():
            print key + " " + val

        break
    # commit_data = json.load(j_file)
    # print commit_data
    # print data

def main():
    process_json()





if __name__ == '__main__':
    main()