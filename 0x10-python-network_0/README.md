# 0x10-python-network_0

#### Task 0: cURL body size
- **File:** `0-body_size.sh`
- **Description:** Bash script to take a URL, send a request, and display the body size of the response in bytes using `curl`.
- **Testing Command:** `./0-body_size.sh 0.0.0.0:5000`

#### Task 1: cURL to the end
- **File:** `1-body.sh`
- **Description:** Bash script to send a GET request to a URL, displaying the body of a 200 status code response using `curl`.
- **Testing Command:** `./1-body.sh 0.0.0.0:5000/route_1`

#### Task 2: cURL Method
- **File:** `2-delete.sh`
- **Description:** Bash script to send a DELETE request to a URL, displaying the body of the response using `curl`.
- **Testing Command:** `./2-delete.sh 0.0.0.0:5000/route_3`

#### Task 3: cURL only methods
- **File:** `3-methods.sh`
- **Description:** Bash script to take a URL and display all HTTP methods the server will accept using `curl`.
- **Testing Command:** `./3-methods.sh 0.0.0.0:5000/route_4`

#### Task 4: cURL headers
- **File:** `4-header.sh`
- **Description:** Bash script to take a URL, send a GET request with header X-School-User-Id: 98, and display the body of the response using `curl`.
- **Testing Command:** `./4-header.sh 0.0.0.0:5000/route_5`

#### Task 5: cURL POST parameters
- **File:** `5-post_params.sh`
- **Description:** Bash script to take a URL, send a POST request with specific parameters, and display the body of the response using `curl`.
- **Testing Command:** `./5-post_params.sh 0.0.0.0:5000/route_6`

#### Task 6: Find a peak
- **Files:** `6-peak.py`, `6-peak.txt`
- **Description:** Function `find_peak` in Python to find a peak in an unsorted list of integers with complexity analysis.
- **Testing Command:** `./6-main.py`

#### Task 7: Only status code
- **File:** `100-status_code.sh`
- **Description:** Bash script to send a request to a URL and display only the status code of the response using `curl`.
- **Testing Command:** `./100-status_code.sh 0.0.0.0:5000`

#### Task 8: cURL a JSON file
- **File:** `101-post_json.sh`
- **Description:** Bash script to send a JSON POST request to a URL with file content and display the body of the response using `curl`.
- **Testing Command:** `./101-post_json.sh 0.0.0.0:5000/route_json my_json_file`

#### Task 9: Catch me if you can!
- **File:** `102-catch_me.sh`
- **Description:** Bash script to make a request to cause the server to respond with a specific message using `curl`.
- **Testing Command:** `./102-catch_me.sh`
