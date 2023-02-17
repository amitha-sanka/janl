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
  right: 100px;
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
<h1 id="budgets"><u>Choose a Budget</u></h1>
<h1 id="durations"><u>Choose the Duration</u></h1>

<div class="hobby">
  <button onclick="myFunction()" class="dropbtn">Activity</button>
  <div id="myDropdown" class="dropdown-content">
  </div>
</div>

<div class="budget">
  <button onclick="myFunction()" class="dropbtn">Activity</button>
  <div id="myDropdown" class="dropdown-content">
  </div>
</div>

<div class="duration">
  <button onclick="myFunction()" class="dropbtn">Activity</button>
  <div id="myDropdown" class="dropdown-content">
  </div>
</div>

<script>
    // URL for deployment
    var url = "https://amitha-sanka.github.io/janl/"
    // Comment out next line for local testing
    //url = "http://localhost:8731"
    // Authenticate endpoint
    const activities_url = url + '/api/activities';
</script>
