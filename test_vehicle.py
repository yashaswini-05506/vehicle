from vehicle import vehicle_details

def test_vehicle_details():
    vehicle_number = "KA-01-1234"
    owner_name = "yashaswini"
    vehicle_type = "two wheeler"
    year_of_manufacture = 2022
    expected_output = (
        "Vehicle Number: KA-01-1234\n"
        "Owner Name: yashaswini\n"
        "Vehicle Type: two wheeler\n"
        "Year of Manufacture: 2022\n"
    )
    actual_output = vehicle_details(vehicle_number, owner_name, vehicle_type, year_of_manufacture)
    assert actual_output == expected_output
