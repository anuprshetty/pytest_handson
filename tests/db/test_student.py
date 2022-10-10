import pytest

from db.student import Student

class TestStudent:

    @pytest.fixture(scope="module")
    def db(self):
        # module_setup
        print("module_setup")
        db = Student()
        db.connect('student_data.json')
        yield db
        # module_teardown
        print("module_teardown")
        db.close()

    @pytest.fixture
    def log(self):
        # method_setup
        print("Test case ... Started")
        yield
        # method_teardown
        print("Test case... DONE")

    def test_ram_data(self, db, log):
        ram_data = db.get_data('Ram')
        assert ram_data["id"] == 1

    def test_sham_data(self, db, log):
        sham_data = db.get_data("Sham")
        assert sham_data["id"] == 2
