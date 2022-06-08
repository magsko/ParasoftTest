import sys
import self as self
from unittest import TestLoader, TestSuite, TextTestRunner
# import testtools as testtools
from test.scripts.test_Home_Page import ParasoftHomePage
from test.scripts.test_registration import NewUserRegistration


if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((
        # test_loader.loadTestsFromTestCase(ParasoftHomePage),
        test_loader.loadTestsFromTestCase(NewUserRegistration),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    # parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    # parallel_suite.run(testtools.StreamResult())
    # self.driver.set_page_load_timeout(30)
