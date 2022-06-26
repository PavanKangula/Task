Feature:

  Scenario:Verify London Weather Report
    Given The Api is executed
    Then verify if the response contains four days of data
    Then all the forecast should be in the hourly interval ( no hour should be missed )
    Then For all 4 days, the temp should not be less than temp_min and not more than temp_max
    When the weather id is 500, the description should be light rain
    When the weather id is 800, the description should be a clear sky

