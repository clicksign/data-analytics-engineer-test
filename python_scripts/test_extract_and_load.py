""" Tests for extract_and_load.py """
import unittest
import os
import pandas as pd
from extract_and_load import replace_nan_in_json, read_csv_and_clean, is_json_data


class TestCSVProcessing(unittest.TestCase):
    """Tests for CSV processing functions."""

    def test_replace_nan_in_json(self):
        """Tests that NaN values in JSON data are replaced with None."""
        data = '{"key1": 42, "key2": NaN, "key3": "value"}'
        expected_result = '{"key1": 42, "key2": null, "key3": "value"}'
        self.assertEqual(replace_nan_in_json(data), expected_result)

    def test_is_json_data(self):
        """Tests that is_json_data() correctly identifies JSON data."""
        self.assertTrue(is_json_data('{"key": "value"}'))
        self.assertTrue(is_json_data('{"key": NaN}'))
        self.assertFalse(is_json_data("not json"))
        self.assertFalse(is_json_data("42"))

    def test_read_csv_and_clean(self):
        """Tests that read_csv_and_clean() correctly reads and cleans a CSV file."""
        file_path = "data/test.csv"
        # Create a test DataFrame with appropriate columns and data
        test_data = {
            "column1": ['{"key": "value"}', '{"key": "value2"}', '{"key3": "value2"}'],
            "column2": ['{"key": NaN}', '{"key": "value"}', '{"key": "value"}'],
            "column3": ["some text", "other one", "last one"],
        }
        test_df = pd.DataFrame(test_data)

        # Write the test DataFrame to a CSV file
        test_df.to_csv(file_path, index=False)

        cleaned_table = read_csv_and_clean(file_path)
        self.assertTrue("column1" in cleaned_table.columns)
        self.assertTrue("column2" in cleaned_table.columns)
        self.assertTrue("column3" in cleaned_table.columns)
        # Add more assertions based on your expectations

        # Clean up by removing the test CSV file
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
