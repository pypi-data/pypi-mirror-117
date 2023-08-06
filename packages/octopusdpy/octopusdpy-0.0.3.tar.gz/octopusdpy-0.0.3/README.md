# octopusdpy


WIP Python package for interacting with Octopus Deploy's API. Currently this provides for read only access.

## Usage
You'll need two items:

* octopusdpy_url: The URL used to interact with your instance of octopusdpy.
* api_key: An API key used to authenticate with octopusdpy.

```python
import octopusdpy

octopusdpy_api = octopusdpy.API(octopusdpy_url="XXX", api_key="YYY")
```

When the octopusdpy API returns multiple values an iterator is used:

A new item is returned each iteration. The iterator is exhausted once all items have been returned from the API.
```python
environments = api.get_environments():

for environment in environments:
    print(environment.Name)
```

You can do simple gathering of information like:

Get all the machines assigned to an environment and the roles of those machines.

```python
import octopusdpy


api = octopusdpy.API("XXX", "YYY")
environment_pages = api.get_environments()
for environments in environment_pages:

    for environment in environments:
        machine_pages = environment.machines

        for machines in machine_pages:
            for machine in machines:
                print(environment.Name, machine.Name, machine.Roles)
```

Clone a Library Variable Set

```python
source_library_variable_set = api.get_library_variable_set('LibraryVariableSets-123')
destination_library_variable_set = api.get_library_variable_set('LibraryVariableSets-456')
source_variable_set = source_library_variable_set.variable_set
destination_variable_set = destination_library_variable_set.variable_set
destination_variable_set.Variables = source_variable_set.Variables
destination_variable_set.save()
```

Find all your long running currently executing tasks

```python
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
tasks = api.get_tasks({'states':'executing'})

for task in tasks:
    time_delta = now - task.start_time
    if time_delta.total_seconds() > 86400:
        hours, remainder = divmod(time_delta.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(task.Id, task.Description, f"{hours} hours, {minutes} minutes")
```

Find all the variables in a Library Variable Set that are scoped to a role

```python
import octopusdpy
import re
nightly_re = re.compile(r'.*nightly.*', re.IGNORECASE)

library_variable_set = api.get_library_variable_set('LibraryVariableSets-123')
variable_set = library_variable_set.variable_set

for variable in variable_set.Variables:
    roles = variable['Scope'].get('Role', [])
    for role in roles:
        if nightly_re.match(role):
            print(variable)
```
