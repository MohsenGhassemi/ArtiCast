function load() {

  // Get the event_list container
  var event_list = document.getElementById("event_list");

  // Retrieve data from local memory
  chrome.storage.local.get("info", function(data) {

    // If the data is updated
    if(typeof(data.info) !== "undefined") {
      console.log("inside load")  
      event_list.innerHTML = "";

      // Generate list for each event entry
      data.info.forEach(function(event, idx, array) {

        // Check if the element is the last one. Use a different css style if true.
        if (idx === (array.length - 1)) {
          var elmnt = document.createElement("ul")
        } else {
          var elmnt = document.createElement("li")
        }

        // Obtain the event name, venue and link.
        var episode_title = event.title;
        var episode_url = event.url;
        

       /* // Container for the event venue.
        var div = document.createElement("div");
        div.innerHTML = event_venue;
        div.setAttribute("class", "venue");*/

        var a = document.createElement("a");

        a.innerHTML = episode_title;
        // Open a blank tab when the link is clicked.
        a.setAttribute("target", "_blank");
        a.setAttribute("href", episode_url);

        // Put the event venue and link to the element
       // elmnt.appendChild(div);
        elmnt.appendChild(a);

        // Append the new element to the list.
        event_list.appendChild(elmnt);

      });
    }
  });
}

function reset () {

	// set the icon to greyscale 
	chrome.browserAction.setIcon({path : "../../icons/Logo_greyscale.png"});

	// clean the local storage
	chrome.storage.local.clear(function () {
		console.log("Comments reset");
	});
}


function get_podcasts(url){
    if (true) {

        var api_server = "http://34.204.73.22:8000/";
		// URL for http requests
		var req_url = api_server + "submission/?url=" + url;
        
		// Send http requests
		fetch(req_url)
		.then(r => r.text())
		.then(function(result) {
			result_json = JSON.parse(result);
			if (result_json.found) {
				// Store the fetched data into local memory for display
				chrome.storage.local.set({info: result_json.info}, function() {
					console.log("Podcasts Found!");
					// Change to colored icon
					chrome.browserAction.setIcon({path : "../../icons/Logo.png"});
					load();
        		});
			}
		});
	}
}


document.getElementById('submit').onclick = function(){
    reset();
    chrome.tabs.query({'active':true,'lastFocusedWindow':true},function(tabs){
    url = tabs[0].url;
    get_podcasts(url)});
    };
/*
// Trigger the function when DOM of the pop-up is loaded.
document.addEventListener('DOMContentLoaded', function() {


  load();

});
*/