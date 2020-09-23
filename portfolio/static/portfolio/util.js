    /* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
    function toggle() {
      var navbar = document.getElementById("Basenav");
      if (navbar.className === "base_nav") {
      navbar.className += " responsive";
      } else {
      navbar.className = "base_nav";
      }
  }