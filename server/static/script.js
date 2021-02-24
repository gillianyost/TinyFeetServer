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

/* ------------- dynamic Select page dropdown options switching ------------- */
let county_select = document.getElementById('county');
let city_select = document.getElementById('city');
let zip_select = document.getElementById('zip');

county_select.onchange = function() {
    county = county_select.value;
    fetch('/sectors/' + county).then(function(response){
        response.json().then(function(data){
            console.table(data);
            let optionHTML = '';
            for (let city of data.cities) {
                optionHTML += '<option value="' + city.name + '">' + city.name + '</option>';
            }
            city_select.innerHTML = optionHTML;
        });
    });
}

city_select.onchange = function() {
    // document.getElementById('getData').type = "submit";
    county = county_select.value;
    city = city_select.value;
    fetch(`/sectors/${county}/${city}`).then(function(response){
        response.json().then(function(data){
            console.table(data);
            let optionHTML = '';
            for (let zip of data.zip_codes) {
                optionHTML += '<option value="' + zip.zip + '">' + zip.zip + '</option>';
            }
            zip_select.innerHTML = optionHTML;
        });
    });
}
