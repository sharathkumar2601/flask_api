from flask import Flask
from flask_restx import Api, Resource, fields
import csv
import os

local_file_list = os.listdir("/home/sh/myactivity/pds/api_testing/");
app = Flask(__name__);
api = Api(app);

model = api.model('Model', {
    'user_name': fields.List(fields.String),
    'email': fields.List(fields.String)
})

class PDS(object):

    def __init__(self, user_name, email):
        self.user_name = user_name;
        self.email = email;

        self.status = 'Active'


@api.route('/pds_user_list/<file_name>')
class List_User(Resource):

    @api.marshal_with(model)
    def get(self, file_name):

        local_file_list = os.listdir("/home/sh/myactivity/pds/api_testing/");
        for local_file_list in local_file_list:
            print(local_file_list)

        required_file = local_file_list
            # list(filter(lambda x: x in file_name, local_file_list));
        print(required_file)
        user_list = [];
        mail_list = [];
        with open("/home/sh/myactivity/pds/api_testing/"+required_file, "r") as f:
            row = csv.reader(f);
            my_list = list(row);

        for j in my_list:
            if (len(j) > 0):
                print(j[[1][0]])
                user_list.append(j[0]);
                mail_list.append(j[1]);

        return PDS(user_name=user_list,email=mail_list)


app.run(host="127.0.0.3", debug=True)
