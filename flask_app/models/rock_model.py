from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Rock:
    def __init__(self, data):
        self.id = data ['id']
        self.date_found = data ['date_found']
        self.city = data ['city']
        self.state = data ['state']
        self.description = data ['description']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO rocks (date_found, city, state, description) VALUES( %(date_found)s, %(city)s, %(state)s, %(description)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM rocks;"
        results = connectToMySQL(DATABASE).query_db(query)
        rocks = []
        for r in results:
            rocks.append(cls(r))
        return rocks


    # @staticmethod
    # def validate_rock(data):
    #     is_valid = True
    #     # if len(data['date_found']) == "":
    #     #     flash("Date may not be left blank", "error_log_date_found")
    #     #     is_valid = False
    #     if len(data['city']) == "":
    #         flash("City may not be left blank", "error_log_city")
    #         is_valid = False
    #     if len(data['state']) == "":
    #         flash("State may not be left blank", "error_log_state")
    #         is_valid = False
    #     if len(data['description']) == "":
    #         flash("Description may not be left blank", "error_log_description")
    #         is_valid = False
    #     return is_valid