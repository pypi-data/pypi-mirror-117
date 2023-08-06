# sys-vars

> Access system variables in your code as native Python data types.

## Usage

Requires Python 3.7+

Prefers the Linux Docker secrets directory (`/run/secrets`)
over system environment variables.
If an alternate sys vars path is required,
set the following key-value in your OS environment:
`SYS_VARS_PATH="<directory-path-to-vars>"`

```python
import sys_vars


# Returns <class 'str'>
# Default values can be specified if the key is missing
sys_vars.get("HOST_ADDRESS", default="localhost")

# Returns <class 'bool'>
# Default values are supported for casting methods too
# Also treats "t", "true", "y", "yes" as True value
sys_vars.get_bool("DEBUG_MODE", default=False)

# Returns <class 'datetime.datetime'>
sys_vars.get_datetime("LAST_SYNC_RUN")

# Returns <class 'float'>
sys_vars.get_float("pi")

# Returns <class 'int'>
sys_vars.get_int("THE_MEANING_OF_LIFE")

# Returns <class 'dict'> or <class 'list'>
# Automatically decodes JSON strings into dictionaries/lists
sys_vars.get_json("CONFIGURED_TERMS")

# Returns <class 'pathlib.Path'>
sys_vars.get_path("CONFIG_PATH")
```

## Building

1. Install [Poetry](https://python-poetry.org/)

1. Run `poetry install`

1. Run `poetry build`

The .whl file will be located at `./dist/sys_vars-<x.y.z>-py3-none-any.whl`
