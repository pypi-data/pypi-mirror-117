# eazyprofiler
-------------------------------------------
Lazy Profiler is a simple utility to collect CPU, GPU, RAM and GPU Memory stats while the program is running.

This project is forked from shankarpandala's repository [shankarpandala/lazyprofiler](https://github.com/shankarpandala/lazyprofiler) to append recording interval argument. More feature and usage will be appended for simpler and faster profiling.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install eazyprofiler
```

## Usage
logging interval can be set in start_log as seconds. Shorter interval than a second can be set with decimal expression (ex. 0.2=200 milliseconds)

```python
import eazyprofiler.GetStats as gs
pid = gs.start_log("test",2)
"""
Do something in between
"""
gs.stop_log(pid=pid)
gs.plot_stats('test')
```
![Sample Output](/images/sample.PNG)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
