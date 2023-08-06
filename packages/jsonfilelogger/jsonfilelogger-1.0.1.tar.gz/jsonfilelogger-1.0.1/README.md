# 📖 A Python json-filelogger

![Lint code and run tests](https://github.com/ManuDeBuck/python-json-filelogger/workflows/Lint%20code%20and%20run%20tests/badge.svg)
[![pypi](https://img.shields.io/pypi/v/jsonlogger?color=%234d84f5&style=flat-square)](https://pypi.org/project/jsonlogger)

A simple way to log data to json-files from within your code.

## Installation

You can use the python package manager (`pip`) to install the file-logger:

```bash
pip install jsonfilelogger
```

## Usage

Create a `LogWriter`:

```python
from jsonfilelogger.logger import LogWriter

writer = LogWriter(folder="./", filename="log.json", threshold=10)
```

Log data to the logfile:

```python
writer.log({"key_int": 1,
            "key_string": "logger",
            "key_boolean": True,
            "key_double": 1.337,
            "key_list": ["element1", "element2"],
            "key_none": None})
```

Create a `LogReader`:

```python
from jsonfilelogger.logger import LogReader

reader = LogReader(folder="./", filename="log.json")
```

Read data from the logfile:

```python
data = reader.retrieve()
```

Other methods:

| Class |  Method  | Explanation |
|:-----|:--------|:------|
| LogReader, LogWriter | `.reset()` | This method clears the contents of the logfile. |
| LogReader, LogWriter | `.remove()` | This methode removes the logfile. |
| LogWriter | `.with_datetime(folder: str, threshold: int)` | This method creates a logfile in the folder with the current timestamp as filename. |
| LogWriter | `.log(data)` | This method logs the data (dictionary) in the logfile. |
| LogWriter | `.flush()` | This method flushes the buffer in the writer. The threshold of the buffer is given in the constructor |
| LogReader | `.retrieve()` | This method retrieves all the data from the logfile and returns it as a list of dictionaries. |

## Example usage

An example of how to use this logger is given. Imagine one has created a [major breakthrough AI system](https://i.pinimg.com/originals/ae/fb/01/aefb01c27ddfdfa2cef723f5056252f7.jpg) that still has to be trained. 
During training one want's to keep an eye on the performance of the progress. To do this, the LogWriter can be added in the learning iterations (e.g. in one Jupyter notebook). 
In another process (e.g. in another Jupyter notebook) it is then possible to read in the data and make amazing visualisations (yay, visualisations!) of how your breakthrough model is performing...

```python
from jsonfilelogger.logger import LogWriter

writer = LogWriter.with_datetime(folder="./", threshold=10)

super_great_ai_model = ...
iteration = 0
while iteration < 100_000:
    score, other_data = super_great_ai_model.do_iteration()
    writer.log({
        score: score,
        other_data: other_data
    })
    iteration += 1
writer.flush()
```

```python
from jsonfilelogger.logger import LogReader
import glob

logs_files = sorted(glob.glob("./[0-9]*.json"))
reader = LogReader(folder="./", filename=logs_files[-1])

data = reader.retrieve()

# Make awesome visualisations!
...
```

There may also be other use cases, you can use this logger as you want!

## Tests

You can run the tests yourselves by:

```bash
cd tests
pip3 install -r requirements.txt
pytest
```

## License

This software is licensed under the [MIT](LICENSE) license.

## Bugs/ Ideas?

In case of questions, ideas or bugs you can always create an issue or [contact me](https://mdebuck.org).