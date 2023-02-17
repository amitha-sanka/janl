## Del Mar

<p>Del Mar</p>

<table>
  <thead>
  <tr>
    <th>Name</th>
    <th>Rating</th>
    <th>Review</th>
    <th>Recommend</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>

<p>Write a Review</p>

<form action="javascript:create_seaworld()">
    <p><label>
        Name:
        <input type="text" name="name" id="name" required="" />
    </label></p>
    <p><label>
        Rating:
        <input type="text" name="rating" id="rating" required="" />
    </label></p>
    <p><label>
        Review:
        <input type="text" name="review" id="review" required="" />
    </label></p>
    <p><label>
        Recommend:
        <input type="text" name="recommend" id="recommen" required="" />
    </label></p>
    <p>
        <button>Post</button>
    </p>
</form>

<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  //const url = "http://localhost:8086/api/users"
  const url = "https://sdc.nighthawkcodingsociety.com/api/seaworld"
  const create_fetch = url + '/create';
  const read_fetch = url + '/';

  // Load users on page entry
  read_seaworld();


  // Display User Table, data is fetched from Backend Database
  function read_seaworld() {
    // prepare fetch options
    const read_options = {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'omit', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
      },
    };

    // fetch the data from API
    fetch(read_fetch, read_options)
      // response is a RESTful "promise" on any successful fetch
      .then(response => {
        // check for response errors
        if (response.status !== 200) {
            const errorMsg = 'Database read error: ' + response.status;
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
            for (let row in data) {
              console.log(data[row]);
              add_row(data[row]);
            }
        })
    })
    // catch fetch errors (ie ACCESS to server blocked)
    .catch(err => {
      console.error(err);
      const tr = document.createElement("tr");
      const td = document.createElement("td");
      td.innerHTML = err;
      tr.appendChild(td);
      resultContainer.appendChild(tr);
    });
  }

  function create_seaworld(){
    //Validate Password (must be 6-20 characters in len)
    //verifyPassword("click");
    const body = {
        name: document.getElementById("name").value,
        name: document.getElementById("name").value,
        password: document.getElementById("password").value,
        dob: document.getElementById("dob").value
    };
    const requestOptions = {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            "content-type": "application/json",
            'Authorization': 'Bearer my-token',
        },
    };

    // URL for Create API
    // Fetch API call to the database to create a new user
    fetch(create_fetch, requestOptions)
      .then(response => {
        // trap error response from Web API
        if (response.status !== 200) {
          const errorMsg = 'Database create error: ' + response.status;
          console.log(errorMsg);
          const tr = document.createElement("tr");
          const td = document.createElement("td");
          td.innerHTML = errorMsg;
          tr.appendChild(td);
          resultContainer.appendChild(tr);
          return;
        }
        // response contains valid result
        response.json().then(data => {
            console.log(data);
            //add a table row for the new/created userid
            add_row(data);
        })
    })
  }

  function add_row(data) {
    const tr = document.createElement("tr");
    const name = document.createElement("td");
    const rating = document.createElement("td")
    const review = document.createElement("td");
    const recommend = document.createElement("td");
  

    // obtain data that is specific to the API
    name.innerHTML = data.name; 
    rating.innerHTML = data.rating.length;
    review.innerHTML = data.review; 
    recommend.innerHTML = data.recommend; 

    // add HTML to container
    tr.appendChild(name);
    tr.appendChild(rating);
    tr.appendChild(review);
    tr.appendChild(recommend);

    resultContainer.appendChild(tr);
  }

</script>
