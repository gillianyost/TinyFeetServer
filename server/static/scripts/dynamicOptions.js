/* ------------- Dynamic Select page dropdown options switching ------------- */

document.getElementById('countyField').onchange = function(){changeCity('countyField', 'cityField', 'zipField');}
document.getElementById('cityField').onchange = function(){changeZip('countyField', 'cityField', 'zipField');}

document.getElementById('countyField2').onchange = function(){changeCity('countyField2', 'cityField2', 'zipField2');}
document.getElementById('cityField2').onchange = function(){changeZip('countyField2', 'cityField2', 'zipField2');}

function changeCity(countyId, cityId, zipId) {
    county = document.getElementById(countyId).value;
    city = document.getElementById(cityId);
    fetch('/emissions/' + county).then(function(response){
        response.json().then(function(data){
            // console.table(data);
            let optionHTML = '';
            for (let city of data.cities) {
                optionHTML += '<option value="' + city.option + '">' + city.option + '</option>';
            }
            city.innerHTML = optionHTML;
            changeZip(countyId, cityId, zipId);    
        });
    });
}


function changeZip(countyId, cityId, zipId) {
    county = document.getElementById(countyId).value;
    city = document.getElementById(cityId).value;
    zip = document.getElementById(zipId);

    fetch(`/emissions/${county}/${city}`).then(function(response){
        response.json().then(function(data){
            // console.table(data);
            let optionHTML = '';
            optionHTML += zip.option;
            for (let zip of data.zip_codes) {
                optionHTML += '<option value="' + zip.option + '">' + zip.option + '</option>';
            }
            zip.innerHTML = optionHTML;
        });
    });
}