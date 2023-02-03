---
layout: default
title: Map and Weather API
permalink: /mapweather
type: pbl
week: 21
---
<!-- HTML table fragment for page -->


<body>
<br>
<br>

<h1><strong style="color:black">Weather Forecast</strong></h1>

<!-- <a href="#astronomybutton"><button> Weather API </button></a>

    
<!-- HTML table fragment for page -->

<script>
    // alert('Enter city of destination and click on "Get Location & Weather Forecast"');

    function cityButtonClick(city) {
        
        if (!city.trim()) {
            alert("Enter a city in San Diego County.");
            return;
        }  

//alert("yo momma!:  " + city);

        // prepare HTML result container for new output
//        const resultContainer = document.getElementById("test");

        //clear contents of astronomy table
//        resultContainer.innerHTML = "<i>hhhhhh</>";

//alert("1: " + resultContainer);

        // prepare fetch options
        const url = 'https://weatherapi-com.p.rapidapi.com/forecast.json?q=' + city + '&days=3';

//alert(url);
//alert("2: " + url);
            
        const headers = {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached 
            credentials: 'omit', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json',
                'X-RapidAPI-Key': '0b6ef107f7msh5606de624633ceap17521ejsn27566d20ff5b',
		        'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
            },
        };

//alert("3: " + headers)

//alert("3a: pre-fetch" + headers);

        // fetch the API
        fetch(url, headers)
        // response is a RESTful "promise" on any successful fetch
        .then(response => {
            // check for response errors
            if (response.status !== 200) {

                const errorMsg = 'Database response error: ' + response.status;
                console.log(errorMsg);
                const tr = document.createElement("tr");
                const td = document.createElement("td");
                td.innerHTML = errorMsg;
                tr.appendChild(td);
                resultContainer.appendChild(tr);

                return;
            }
            // valid response will have json data
            response.json().then(data => {
                console.log(data);
                console.log(data.location)
                console.log(data.current)
                console.log(data.condition)
                console.log(data.forecast)

                // Weather Data
                document.getElementById("name").innerHTML = data.location.name;
                document.getElementById("region").innerHTML = data.location.region;
                document.getElementById("country").innerHTML = data.location.country;                
                document.getElementById("tz_id").innerHTML = data.location.tz_id;
                document.getElementById("localtime_epoch").innerHTML = data.location.localtime_epoch;
                document.getElementById("localtime").innerHTML = data.location.localtime;

                // Current Conditions
                document.getElementById("temp_f").innerHTML = data.current.temp_f;
                document.getElementById("wind_mph").innerHTML = data.current.wind_mph;
                document.getElementById("humidity").innerHTML = data.current.humidity;                
                document.getElementById("cloud").innerHTML = data.current.cloud;
                document.getElementById("feelslike_f").innerHTML = data.current.feelslike_f;
                document.getElementById("condition_text").innerHTML = data.current.condition.text;

                // Weather Forecast
                // day 1
                document.getElementById("date_1").innerHTML = data.forecast.forecastday[0].date;
                document.getElementById("maxtemp_f_1").innerHTML = data.forecast.forecastday[0].day.maxtemp_f;
                document.getElementById("mintemp_f_1").innerHTML = data.forecast.forecastday[0].day.mintemp_f;
                document.getElementById("avgtemp_f_1").innerHTML = data.forecast.forecastday[0].day.avgtemp_f;
                document.getElementById("maxwind_mph_1").innerHTML = data.forecast.forecastday[0].day.maxwind_mph;
                document.getElementById("totalprecip_in_1").innerHTML = data.forecast.forecastday[0].day.totalprecip_in;
                document.getElementById("daily_will_it_rain_1").innerHTML = data.forecast.forecastday[0].day.daily_will_it_rain;
                document.getElementById("daily_chance_of_rain_1").innerHTML = data.forecast.forecastday[0].day.daily_chance_of_rain;
                document.getElementById("forecast_text_1").innerHTML = data.forecast.forecastday[0].day.condition.text;
                // day 2
                document.getElementById("date_2").innerHTML = data.forecast.forecastday[1].date;
                document.getElementById("maxtemp_f_2").innerHTML = data.forecast.forecastday[1].day.maxtemp_f;
                document.getElementById("mintemp_f_2").innerHTML = data.forecast.forecastday[1].day.mintemp_f;
                document.getElementById("avgtemp_f_2").innerHTML = data.forecast.forecastday[1].day.avgtemp_f;
                document.getElementById("maxwind_mph_2").innerHTML = data.forecast.forecastday[1].day.maxwind_mph;
                document.getElementById("totalprecip_in_2").innerHTML = data.forecast.forecastday[1].day.totalprecip_in;
                document.getElementById("daily_will_it_rain_2").innerHTML = data.forecast.forecastday[1].day.daily_will_it_rain;
                document.getElementById("daily_chance_of_rain_2").innerHTML = data.forecast.forecastday[1].day.daily_chance_of_rain;
                document.getElementById("forecast_text_2").innerHTML = data.forecast.forecastday[1].day.condition.text;
                // day 3 
                document.getElementById("date_3").innerHTML = data.forecast.forecastday[2].date;
                document.getElementById("maxtemp_f_3").innerHTML = data.forecast.forecastday[2].day.maxtemp_f;
                document.getElementById("mintemp_f_3").innerHTML = data.forecast.forecastday[2].day.mintemp_f;
                document.getElementById("avgtemp_f_3").innerHTML = data.forecast.forecastday[2].day.avgtemp_f;
                document.getElementById("maxwind_mph_3").innerHTML = data.forecast.forecastday[2].day.maxwind_mph;
                document.getElementById("totalprecip_in_3").innerHTML = data.forecast.forecastday[2].day.totalprecip_in;
                document.getElementById("daily_will_it_rain_3").innerHTML = data.forecast.forecastday[2].day.daily_will_it_rain;
                document.getElementById("daily_chance_of_rain_3").innerHTML = data.forecast.forecastday[2].day.daily_chance_of_rain;
                document.getElementById("forecast_text_3").innerHTML = data.forecast.forecastday[2].day.condition.text;


                //alert("data.astronomy" + data.astronomy.astro.sunrise);
                // tr for each row
/*
                const tr = document.createElement("tr");

                // td for each column
                const temp_f = document.createElement("td"); 
                const wind_mph = document.createElement("td"); 
                const humidity = document.createElement("td"); 
                const cloud = document.createElement("td"); 
                const feelslike_f = document.createElement("td"); 
                const condition_text = document.createElement("td");
                const condition_icon = document.createElement("td"); 

                const date = document.createElement("td"); 
                const maxtemp_f = document.createElement("td");                
                const mintemp_f = document.createElement("td"); 
                const avgtemp_f = document.createElement("td");                 
                const maxwind_mph = document.createElement("td");                 
                const totalprecip_in = document.createElement("td");                
                const daily_will_it_rain = document.createElement("td"); 
                const daily_chance_of_rain = document.createElement("td");                 
                const forecast_text = document.createElement("td");                
                const forecast_icon = document.createElement("td"); 
*/
                // data is specific to the API
/*
                temp_f.innerHTML = data.current.temp_f;
                wind_mph.innerHTML = data.condition.wind_mph;
                humidity.innerHTML = data.condition.humidity;
                cloud.innerHTML = data.condition.cloud;                 
                feelslike_f.innerHTML = data.condition.feelslike_f;
                condition_text.innerHTML = data.condition.text;
                condition_icon.innerHTML = data.condition.icon;
                date.innerHTML = data.forecast.forecastday.date;
                maxtemp_f.innerHTML = data.forecast.forecastday[0].day.maxtemp_f;
                mintemp_f.innerHTML = data.forecast.forecastday[0].day.mintemp_f;
                avgtemp_f.innerHTML = data.forecast.forecastday[0].day.avgtemp_f;
                maxwind_mph.innerHTML = data.forecast.forecastday[0].day.maxwind_mph;
                totalprecip_in.innerHTML = data.forecast.forecastday[0].day.totalprecip_in;
                daily_will_it_rain.innerHTML = data.forecast.forecastday[0].day.daily_will_it_rain;
                daily_chance_of_rain.innerHTML = data.forecast.forecastday[0].day.daily_chance_of_rain;
                forecast_text.innerHTML = data.forecast.forecastday[0].day.condition.text;
                forecast_icon.innerHTML = data.forecast.forecastday[0].day.condition.icon;
*/
                // this builds td's into tr
/*                
                tr.appendChild(temp_f);
                tr.appendChild(wind_mph);
                tr.appendChild(humidity);
                tr.appendChild(cloud);
                tr.appendChild(feelslike_f);
                tr.appendChild(condition_text);
                tr.appendChild(condition_icon);

                tr.appendChild(date);
                tr.appendChild(maxtemp_f);
                tr.appendChild(mintemp_f);
                tr.appendChild(avgtemp_f);
                tr.appendChild(maxwind_mph);
                tr.appendChild(totalprecip_in);             
                tr.appendChild(daily_will_it_rain);
                tr.appendChild(daily_chance_of_rain);
                tr.appendChild(forecast_text);
                tr.appendChild(forecast_icon);

                // add HTML to container
                resultContainer.appendChild(tr);
*/

            })
        })
    }
</script>

If you choose a city, it will list out the weather forecast and location details.

<div id="astronomybutton">

<br>
<label for="city">Enter city name:</label>
<input type="text" id="city" name="city">&nbsp;&nbsp;<input type="button" value="Get Details" onclick="cityButtonClick(document.getElementById('city').value)">
<br><br>

<table>

<style>

table, th, td {
  border: 1px solid;
  border-collapse: collapse;

}

th, td {
  padding: 10px;
  text-align: center;
  color: black;
}


</style>
  <thead><u>Location Details</u>
  <tr>
    <th style="color:#00008B;">City</th>
    <th style="color:#00008B;">Region</th>
    <th style="color:#00008B;">Country</th>
    <th style="color:#00008B;">Time Zone</th>
    <th style="color:#00008B;">Local Time Epoch</th>
    <th style="color:#00008B;">Local Date and Time</th>
  </tr>
  </thead>
  <tbody>
    <td id="name"></td>
    <td id="region"></td>
    <td id="country"></td>
    <td id="tz_id"></td>
    <td id="localtime_epoch"></td>
    <td id="localtime"></td>
  </tbody>
</table>


<table>
    <thead><u>Current Conditions</u>
    <tr>
        <th style="color:#00008B;">Temperature (F)</th>
        <th style="color:#00008B;">Wind (mph)</th>
        <th style="color:#00008B;">Humidity</th>
        <th style="color:#00008B;">Cloud</th>
        <th style="color:#00008B;">Feels Like (F)</th>
        <th style="color:#00008B;">Overall Condition</th>
    </tr>
    </thead>
    <tbody> 
        <td id="temp_f"></td>
        <td id="wind_mph"></td>
        <td id="humidity"></td>        
        <td id="cloud"></td>
        <td id="feelslike_f"></td>
        <td id="condition_text"></td>
    </tbody>
</table>

<table>
    <thead><u>Weather Forecast</u> for the next 3 days
    <tr>
        <th style="color:#00008B;">Date</th>
        <th style="color:#00008B;"> Max Temperature (F)</th>
        <th style="color:#00008B;">Min Temperature (F)</th>
        <th style="color:#00008B;"> Average Temperature (F)</th>
        <th style="color:#00008B;">Max Wind (mph)</th>
        <th style="color:#00008B;">Total Precipitation (in)</th>
        <th style="color:#00008B;">Will it Rain?</th>
        <th style="color:#00008B;">Chance of Rain</th>
        <th style="color:#00008B;">Overall Condition</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td id="date_1"></td>        
        <td id="maxtemp_f_1"></td>
        <td id="mintemp_f_1"></td>
        <td id="avgtemp_f_1"></td>
        <td id="maxwind_mph_1"></td>
        <td id="totalprecip_in_1"></td>
        <td id="daily_will_it_rain_1"></td>
        <td id="daily_chance_of_rain_1"></td>
        <td id="forecast_text_1"></td>
        <!-- generated rows -->
    </tr>
    <tr>
        <td id="date_2"></td>        
        <td id="maxtemp_f_2"></td>
        <td id="mintemp_f_2"></td>
        <td id="avgtemp_f_2"></td>
        <td id="maxwind_mph_2"></td>
        <td id="totalprecip_in_2"></td>
        <td id="daily_will_it_rain_2"></td>
        <td id="daily_chance_of_rain_2"></td>
        <td id="forecast_text_2"></td>
        <!-- generated rows -->
    </tr>
    <tr>
        <td id="date_3"></td>        
        <td id="maxtemp_f_3"></td>
        <td id="mintemp_f_3"></td>
        <td id="avgtemp_f_3"></td> 
        <td id="maxwind_mph_3"></td>
        <td id="totalprecip_in_3"></td>
        <td id="daily_will_it_rain_3"></td>
        <td id="daily_chance_of_rain_3"></td>
        <td id="forecast_text_3"></td>
        <!-- generated rows -->
    </tr>
    </tbody>
</table>    

<script>



