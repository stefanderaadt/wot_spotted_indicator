# Wot Spotted Status mod

A simple mod to keep track of who has been spotted in the enemy team

## Installation

Within the example's directory execute command:

```bash
python setup.py bdist_wotmod
```

This will produce `klokklokz.spotted_status.00.01.00.wotmod` file to `dist` subdirectory.
Copy the file to `mods/<current version>` directory under game's directory.

You may also install the wotmod to the game with one command by changing the
default dist directory:

```bash
    python setup.py bdist_wotmod --dist-dir='<game dir>/mods/<current version>'
```

Now start following `python.log` to see what the mods prints.

In Powershell:

```powershell
    Get-Content <game dir>\python.log -Tail 3 -Wait
```

Or in bash:

```bash
    tail -f '<game dir>/python.log'
```

## License

This example is licensed under WTFPL license, for more info, see:
http://www.wtfpl.net/about/
