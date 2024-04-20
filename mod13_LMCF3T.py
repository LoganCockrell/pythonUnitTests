from datetime import datetime
import re
import unittest

class UserInput:
    def get_symbol(self, symbol):
        while True:
            if not self.isValidString(symbol):
                print("ERROR: please enter a stock symbol!\n")
            else:
                if len(symbol) > 7:
                    return "ERROR: too many characters!"
                else:
                    if symbol == symbol.upper():
                        return symbol
                    else:
                        return "ERROR: not uppercase!"
    
    def get_chart(self, chart):
        valid_selections = ["1", "2"]
        while True:
            if not self.isValidString(chart) or chart not in valid_selections :
                return "ERROR: please enter a valid chart type!"
            else:
                return chart
            
    def get_series(self, series):
        valid_selections = ["1", "2", "3", "4"]
        while True:
            if not self.isValidString(series) or series not in valid_selections :
                return "ERROR: please enter a valid time series option!"
            else:
                return series

    def isValidString(self, string):
        if string == "":
            return False
        else:
            return True


    def get_date(self, date):
        date_regex = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
        
        while True:
            if re.match(date_regex, date):
                try:
                    #return the date as a date object
                    return datetime.strptime(date, "%Y-%m-%d")
                except ValueError as err:
                    print(f"ERROR: {str(err)}\n")

            else:
                return "ERROR: Enter the date in correct (YYYY-MM-DD) format!"

class TestInput(unittest.TestCase):
    def setUp(self):
        self.user = UserInput() 

    #tests
    def testSymbol(self):
        #verifies a valid input
        self.assertEqual(self.user.get_symbol('GOOGL'), 'GOOGL')
        #verifies that an input with too many characters does not work
        self.assertEqual(self.user.get_symbol('AAAAAAAAAAAAAA'), 'ERROR: too many characters!')
        #verifies that an input with not all uppercase characters does not work
        self.assertEqual(self.user.get_symbol('aaa'), 'ERROR: not uppercase!')

    def testChart(self):
        #verifies a valid input works
        self.assertEqual(self.user.get_chart('1'), '1')
        #verifies that an input besides '1' or '2' does not work
        self.assertEqual(self.user.get_chart('3'), 'ERROR: please enter a valid chart type!')
    
    def testSeries(self):
        #verifies a valid input
        self.assertEqual(self.user.get_series('1'), '1')
        #verifies that an input besides 1-4 does not work
        self.assertEqual(self.user.get_series('5'), 'ERROR: please enter a valid time series option!')

    def testDate(self):
        #verifies valid input
        self.assertEqual(self.user.get_date('2000-08-01'), datetime(2000, 8, 1, 0, 0))
        #verifies a non valid input is not accepted
        self.assertEqual(self.user.get_date('08-01-2000'), 'ERROR: Enter the date in correct (YYYY-MM-DD) format!')

if __name__ == '__main__':
    unittest.main()
