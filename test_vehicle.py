from vehicle import vehicle_details

def test_vehicle_details():
    vehicle_number = "0137"
    owner_name = "yashaswini"
    vehicle_type = "Car"
    year_of_manufacture = 2022
    expected_output = (
        "Vehicle Number: 0137\n"
        "Owner Name: yashaswini\n"
        "Vehicle Type: Car\n"
        "Year of Manufacture: 2022\n"
    )
    actual_output = vehicle_details(vehicle_number, owner_name, vehicle_type, year_of_manufacture)
    assert actual_output == expected_output
