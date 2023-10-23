from flasgger import Swagger
from flask import Flask, request
from monaco_logic.monaco import Racing
from monaco_racing.func_list.logic import (sort_data_abbr, get_data_format, get_all_personal_data_from_database,
                                           get_data_from_database)
from monaco_racing.models import Abbr, Start, End
from monaco_racing.func_list.decorator_db import retry_database


app: Flask = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yml')

racing_instance = Racing()


@retry_database
@app.route('/api/v1/report/', methods=['GET'])
def get_data_racing():
    if request.method == 'GET':
        data_format = request.args.get('format', default='json')
        try:
            # Get data from database
            query_start = Start.select()
            query_end = End.select()
            query_abbr = Abbr.select()

            get_data_start = get_data_from_database(query_start)
            get_data_end = get_data_from_database(query_end)
            get_data_abbr = get_all_personal_data_from_database(query_abbr)

            # Initialize empty lists for using build_report() and print_report()
            racing_instance.racers_start_sorted = get_data_start
            racing_instance.racers_end_sorted = get_data_end
            racing_instance.racer_abbr_sorted = get_data_abbr

            result = racing_instance.build_report()

            mylist = []
            for elements in result:
                for key, value in elements.items():
                    for row in query_abbr:
                        if row.name_id == key:
                            mylist.append({key: [row.person, value]})
            res = get_data_format(mylist, data_format)
            return res, 200
        except ValueError as e:
            # Return an error response if there's an exception
            return f"Invalid data: {str(e)}", 400


@retry_database
@app.route('/api/v1/drivers/', methods=['GET'])
def get_data_person():
    if request.method == 'GET':
        data_format = request.args.get('format', default='json')
        order = request.args.get('order', default='asc')
        try:
            query = sort_data_abbr(order)
            get_data_abbr = get_all_personal_data_from_database(query)
            res = get_data_format(get_data_abbr, data_format)
            return res, 200
        except ValueError:
            raise (f"Invalid data format", 400)


@retry_database
@app.route('/api/v1/drivers/<driver_id>/', methods=['GET'])
def get_personal_info(driver_id):
    if request.method == 'GET':
        data_format = request.args.get('format', default='json')
        try:
            query_abbr = Abbr.select()
            mylist = []
            for row in query_abbr:
                if row.name_id == driver_id:
                    mylist.append({row.name_id: [row.person, row.car]})
            res = get_data_format(mylist, data_format)
            return res, 200
        except ValueError:
            raise (f"Invalid data format", 400)


if __name__ == '__main__':
    app.run(debug=False)
