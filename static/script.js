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
