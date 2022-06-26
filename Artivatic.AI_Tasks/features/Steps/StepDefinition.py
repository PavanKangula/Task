import json
import requests
import collections





@given('The Api is executed')
def step_impl(context):
    context.result = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    context.Data = json.loads(context.result.text)
    context.List = context.Data['list']


@then('verify if the response contains four days of data')
def step_impl(context):
    # context.Data = json.loads(context.result.text)
    #print(context.Data)
    #context.List = context.Data['list']
    context.Atleast_Four_Days = []
    for i in range(96):
        if context.List[i]['dt_txt'][0:10] not in context.Atleast_Four_Days:
            context.Atleast_Four_Days.append(context.List[i]['dt_txt'][0:10])
    print(context.Atleast_Four_Days)

    if len(context.Atleast_Four_Days) >= 4:
        print("Response has atleast 4 days of Data")
        assert True
    else:
        print("Response Doesn't have atleast 4 days of Data")
        assert False


@then('all the forecast should be in the hourly interval ( no hour should be missed )')
def step_impl(context):
    context.Forecast_In_Hours = []
    for i in range(96):
        context.Forecast_In_Hours.append(context.List[i]['dt_txt'][0:10])
    #print(context.Forecast_In_Hours)
    #print(len(context.Forecast_In_Hours))
    context.Total_Forecast_Hours = collections.Counter(context.Forecast_In_Hours)
    print(context.Total_Forecast_Hours)
    context.Total_Hours=sum(context.Total_Forecast_Hours.values())
    #print(type(Context.Total_Hours))

    if context.Total_Hours == 96:
        print("All the forecast has been released in hourly interval and no hour missed")
        assert True
    else:
        print("Forecast is not released in hourly interval")
        assert False



@then('For all 4 days, the temp should not be less than temp_min and not more than temp_max')
def step_impl(context):
    for i in range(96):
        # print(context.List[i]['main']['temp'])
        # print(context.List[i]['main']['temp_min'])
        # print(context.List[i]['main']['temp_max'])

        context.Actual_Temp = context.List[i]['main']['temp']
        context.Min_Temp = context.List[i]['main']['temp_min']
        context.Max_Temp = context.List[i]['main']['temp_max']

        if (context.Actual_Temp >= context.Min_Temp and context.Actual_Temp <= context.Max_Temp):
            assert True
        else:
            assert False


@when('the weather id is 500, the description should be light rain')
def step_impl(context):
    # print(type(context.List[0]['weather'][0]['id']))
    # print(context.List[0]['weather'][0]['description'])

    for i in range(95):
        context.Weather_id = context.List[i]['weather'][0]['id']
        context.Description = context.List[i]['weather'][0]['description']

        if context.Weather_id == 500:
            if context.Description == "light rain":
                assert True
            else:
                assert False





@when('the weather id is 800, the description should be a clear sky')
def step_impl(context):
    for i in range(95):
        context.Weather_id = context.List[i]['weather'][0]['id']
        context.Description = context.List[i]['weather'][0]['description']

        if context.Weather_id == 800:
            if context.Description == "clear sky":
                assert True
            else:
                assert False

