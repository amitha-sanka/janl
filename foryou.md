<!--- This section is Cascading Style Sheet (CSS) and applies to HTML -->
<style>
/* "row style" is flexible size and aligns pictures in center */
.row {
  align-items: center;
  display: flex;
}

/* "column style" is one-third of the width with padding */
.column {
  flex: 33.33%;
  padding: 5px;
}

.hobbies {
  position: fixed;
  right: 400px;
  top: 10px;
}

.budgets {
  position: relative;
  right: 300px;
}

.durations {
  position: relative;
  right: 700px;
}

.hobby {
  position: relative;
}

.budget {
  position: relative;
}

.duration {
  position: relative;
}

</style>



<h1 id="hobbies"><u>Choose a Hobby</u></h1>
<div class="hobby">
  <button onclick="myFunction()" class="dropbtn">Hobby</button>
  <div id="myDropdown" class="dropdown-content">
   <p><a href="#">Amusement Park</a></p>
  </div>
</div>


<h1 id="budgets"><u>Choose a Budget</u></h1>
<div class="budget">
  <button onclick="myFunction()" class="dropbtn">Price Range</button>
  <div id="myDropdown" class="dropdown-content">
  </div>
</div>

<h1 id="durations"><u>Choose the Duration</u></h1>
<div class="duration">
  <button onclick="myFunction()" class="dropbtn">Duration of Activity</button>
  <div id="myDropdown" class="dropdown-content">
  </div>
</div>

<script>
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

</script>
