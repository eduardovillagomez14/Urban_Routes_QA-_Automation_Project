import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Check if Urban Routes server is reachable before running tests
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Task 3: Placeholder function for setting route (will add Selenium in Sprint 8)
        print("function created for set route")
        pass

    def test_select_plan(self):
        # Task 3: Placeholder function for selecting plan
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Task 3: Placeholder for filling phone number
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Task 3: Placeholder for filling payment card details
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Task 3: Placeholder for adding driver message
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Task 3: Placeholder for ordering additional items
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Task 5: Loop prepared for ordering two ice creams (logic added in Sprint 8)
        for _ in range(2):
            # Add Selenium actions here in Sprint 8
            pass

    def test_car_search_model_appears(self):
        # Task 3: Placeholder to verify car search model appears
        print("function created for car search model appears")
        pass
