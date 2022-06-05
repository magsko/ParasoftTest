#Page locators live here

class Locators(object):

    #parabank homepage locators
    username_field = "//*[@id=\"loginPanel\"]/form/div[1]/input"
    password_field = "//*[@id=\"loginPanel\"]/form/div[2]/input"

    #Register New User Page
    first_name = "//*[@id=\"customer.firstName\"]"
    last_name = "//input[@id=\"customer.lastName\"]"
    address = "//input[@id=\"customer.address.street\"]"
    city = "//input[@id=\"customer.address.city\"]"
    state = "//input[@id=\"customer.address.state\"]"
    zip = "//input[@id=\"customer.address.zipCode\"]"
    phone = "//input[@id=\"customer.phoneNumber\"]"
    ssn = "//input[@id=\"customer.ssn\"]"
    username = "//input[@id=\"customer.username\"]"
    password = "//input[@id=\"customer.password\"]"
    confirm_password = "//input[@id=\"repeatedPassword\"]"
    register_btn = "//input[@class=\"button\" and @value=\"Register\"]"

    #Locators for error messages during user registration
    first_name_error = "//*[@id=\"customer.firstName.errors\"]"
    last_name_error = "//*[@id=\"customer.lastName.errors\"]"
    address_error = "//input[@id=\"customer.address.street.errors\"]"
    city_error = "//input[@id=\"customer.address.city.errors\"]"
    state_error = "//input[@id=\"customer.address.state.errors\"]"
    zip_error = "//input[@id=\"customer.address.zipCode.errors\"]"
    phone_error = "//input[@id=\"customer.phoneNumber.errors\"]"
    ssn_error = "//input[@id=\"customer.ssn.errors\"]"
    username_error = "//input[@id=\"customer.username.errors\"]"
    password_error = "//input[@id=\"customer.password.errors\"]"
    confirm_password_error = "//input[@id=\"repeatedPassword.errors\"]"
    register_btn_error = "//input[@class=\"button\" and @value=\"Register\"]"




