# Reviews
> choose you rating to see other peoples thoughts or personally blog your own opinions


<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.dropbtn {
  background-color: #253f61;
  margin-top: 10px;
  margin-left: 650px;
  color: white;
  padding: 16px;
  font-size: 16px;
  min-width: 180px;
  border: none;
  cursor: pointer;
}

.dropbtn:hover, .dropbtn:focus {
  background-color: #253f61;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  margin-bottom: 10px;
  margin-left: 650px;
  display: none;
  position: absolute;
  background-color: #31614d;
  min-width: 180px;
  overflow: auto;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown a:hover {background-color: #ddd;}

.show {display: block;}
</style>
</head>
    <title>Text alignment</title>
<body>
    <h1 align="center">Reviews</h1>


<h2>Which activty would you like to view</h2>
<p>Click on the activity to view ratings</p>

<div class="activity">
  <button onclick="myFunction()" class="dropbtn">Activity</button>
  <div id="myDropdown" class="dropdown-content">
    <p><a href="seaworld.html">Seaworld</a></p>
    <p><a href="balboapark.html">Balboa Park</a></p>
    <p><a href="delmar.html">Del Sur</a></p>
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

</body>
</html>
