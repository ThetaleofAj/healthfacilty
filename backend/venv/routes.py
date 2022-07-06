from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from .app import HealthFacility,ContactDetails,Services,Equipment,OperatingHours

@app.route('api/')
def all_facilities():
    HealthFacility.query.all()

@app.route('api/create/', methods=['GET', 'POST'])
def create_facilities():
     HealthFacility.query.all()

@app.route('api/addequipment/', methods=['GET', 'POST'])
def app_equipment():
    ContactDetails.query.all()

@app.route('api/addcontact/', methods=['GET', 'POST'])
def add_contacts():
    Equipment.query.all()

@app.route('api/addservices/', methods=['GET', 'POST'])
def add_services():
    Services.query.all()

@app.route('api/addhours/', methods=['GET', 'POST'])
def add_oepratingHours():
    OperatingHours.query.all()

@app.route('api/entry/<int:pk>', methods=['GET'])
def single_entry():
    HealthFacility.query.all()

@app.route('api/editmain/<int:pk>', methods=['GET', 'POST','PUT'])
def edit_main():
    HealthFacility.query.all()

@app.route('api/editservices/<int:pk>', methods=['GET', 'POST','PUT'])
def edit_services():
    Services.query.all()

@app.route('api/editequipment/<int:pk>', methods=['GET', 'POST','PUT'])
def edit_equipment():
    Equipment.query.all()

@app.route('api/editcontact/<int:pk>', methods=['GET', 'POST','PUT'])
def edit_contact():
    ContactDetails.query.all()

@app.route('api/edithours/<int:pk>', methods=['GET', 'POST','PUT'])
def edit_facilities():
    OperatingHours.query.all()



