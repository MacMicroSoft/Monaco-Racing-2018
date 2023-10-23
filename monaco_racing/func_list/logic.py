import json
import xml.etree.ElementTree as ET
from flask import Response
from monaco_racing.models import Abbr


def sort_data_abbr(order):
    if order == 'asc':
        query = Abbr.select().order_by(Abbr.name_id)
        return query
    elif order == 'desc':
        query = Abbr.select().order_by(Abbr.name_id.desc())
        return query
    else:
        raise TypeError("Wrong format")


def get_data_format(data, data_format):
    if data_format == 'json':
        json_data = json.dumps(data)
        return Response(json_data, mimetype='application/json')
    elif data_format == 'xml':
        xml_root = ET.Element("Report")
        for driver_info in data:
            driver_element = ET.Element("Driver")
            for key, value in driver_info.items():
                element = ET.SubElement(driver_element, key)
                element.text = str(value)
            xml_root.append(driver_element)
        xml_string = ET.tostring(xml_root, encoding='utf-8', method='xml')
        return Response(xml_string, content_type='text/xml')
    else:
        response_text = "Invalid format specified"
        return Response(response_text, status=400, mimetype='text')


def get_data_from_database(table):
    mylist = []
    for row in table:
        mylist.append({row.name_id: [row.date, row.time]})
    return mylist


def get_all_personal_data_from_database(table):
    mylist = []
    for row in table:
        mylist.append({row.name_id: [row.person, row.car]})
    return mylist
