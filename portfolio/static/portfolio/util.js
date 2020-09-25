/* Toggle between adding and removing the "responsive" class to base_nav when the user clicks on the icon */

function toggle() {
      var navbar = document.getElementById("Basenav");
      if (navbar.className === "base_nav") {
      navbar.className += " responsive";
      } else {
      navbar.className = "base_nav";
      }
  }

var projecten_array;

function projectsort(){
    // dit stuk haalt de titel en datum van ieder project en maakt hiervan een object en zet het weer in de  nodelist
    projecten = document.getElementsByClassName("project");
    data = [].map.call(projecten, project => {
        return(
            {
            "titel" : project.querySelector(".title").textContent ,
            "startmaand": project.querySelector(".date").textContent.split(".")[0].trim(), 
            "startjaar": project.querySelector(".date").textContent.split(".")[1].split("-")[0].trim()}
            );
    });

    // vertaalt nodelist naar array van data [{titel, startmaand, startjaar}]
    projecten_array = Array.from(data);

    // maand vertalen naar een nummer 1 tm 12 
    for (let i = 0; i < projecten_array.length; i++){
        
        projecten_array[i].startmaand = date_index(projecten_array[i].startmaand);
    }
    sortBy("nieuw -> oud");
}


// zet een maand om naar de nummer representatie
function date_index(maand) {
    indexen= {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "mei": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "okt": 10, "nov": 11, "dec": 12
    }
    
    return indexen[maand.toLowerCase()];
}

// wordt geactiveert als op sorteer knop gedrukt wordt.
function sortDate(){
    const radiobuttons = document.querySelectorAll('input[name="sortDate"]');
    let selectedValue;
    for (const radiobutton of radiobuttons) {
        if (radiobutton.checked) {
            selectedValue = radiobutton.value;
            break;
        }
    }

    sortBy(selectedValue);
}

function sortBy(condition){
    // sorteer de projecten eerst op jaar daarna op maand

    if(condition==="nieuw -> oud"){
        projecten_array.sort((a,b) => {return a.startjaar - b.startjaar});
        projecten_array.sort((a,b) => {return a.startmaand - b.startmaand});
    }
    else{
        projecten_array.sort((a,b) => {return b.startjaar - a.startjaar});
        projecten_array.sort((a,b) => {return b.startmaand - a.startmaand});
    }

    // positie van de project geeft de order aan waar de project in terecht moet komen. // style= order :

    for (let i = 0; i < projecten_array.length; i++){
        for(let project of projecten){
            if(project.querySelector(".title").textContent === projecten_array[i].titel){
                project.setAttribute("style", "order: " + i);
                break;
            }
        }
    }
}
