

function reset () {

	// set the icon to greyscale 
	chrome.browserAction.setIcon({path : "../../icons/Logo_greyscale.png"});

	// clean the local storage
	chrome.storage.local.clear(function () {
		console.log("Comments reset");
	});
}

reset();

// API server IP
var api_server = "http://34.204.73.22:8000/";

// Add a listenser when DOM is loaded.
chrome.webNavigation.onDOMContentLoaded.addListener(function (details) {
    reset();
/*
	var url = details.url;
	reset();

	// If en.wikipedia.org is nativaged.
	if (true) {

		//var topic = url.replace("https://www.youtube.com/watch?v=", "");

		// URL for http requests
		var req_url = api_server + "submission/?url=" + url;

		// Send http requests
		fetch(req_url)
		.then(r => r.text())
		.then(function(result) {
			result_json = JSON.parse(result);
			if (true) {
				// Store the fetched data into local memory for display
				chrome.storage.local.set({url: result_json.url}, function() {
					console.log("Podcasts Found!");
					// Change to colored icon
					chrome.browserAction.setIcon({path : "../../icons/Logo.png"});
        		});
			}
		});
	}*/
});