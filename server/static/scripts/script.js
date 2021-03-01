/* --------------------- Read page form hiding/unhiding --------------------- */
function changeOptions(selectEl) {
    let selectedValue = selectEl.options[selectEl.selectedIndex].value;
    let subForms = document.getElementsByClassName('schema');
    for (let i = 0; i < subForms.length; i += 1) {
      if (selectedValue === subForms[i].id)
        subForms[i].setAttribute('style', 'display:block');
      else
        subForms[i].setAttribute('style', 'display:none');
    }
  }

/* ------------- Dynamic Select page dropdown options switching ------------- */
let county_select = document.getElementById('county');
let city_select = document.getElementById('city');
let zip_select = document.getElementById('zip');

function submitForm(form) {
    const submitFormFunction = Object.getPrototypeOf(form).submit;
    submitFormFunction.call(form);
}

county_select.onchange = function(){changeCity();}
city_select.onchange = function(){changeZip();}


function changeCity() {
    county = county_select.value;
    fetch('/sectors/county/' + county).then(function(response){
        response.json().then(function(data){
            // console.table(data);
            let optionHTML = '';
            for (let city of data.cities) {
                optionHTML += '<option value="' + city.option + '">' + city.option + '</option>';
            }
            city_select.innerHTML = optionHTML;
            changeZip();    
        });
    });
}


function changeZip() {
    county = county_select.value;
    city = city_select.value;
    fetch(`/sectors/county/${county}/city/${city}`).then(function(response){
        response.json().then(function(data){
            // console.table(data);
            let optionHTML = '';
            optionHTML += zip.option;
            for (let zip of data.zip_codes) {
                optionHTML += '<option value="' + zip.option + '">' + zip.option + '</option>';
            }
            zip_select.innerHTML = optionHTML;
        });
    });
}
