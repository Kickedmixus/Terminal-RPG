((Get-Content -path .\output\res\rpg.py -Raw) -replace 'input','handleInput') | Set-Content -Path .\output\res\rpg.py
((Get-Content -path .\output\res\rpg.py -Raw) -replace 'output','handleOutput') | Set-Content -Path .\output\res\rpg.py
Get-Content .\src_browser\to_merge.py, .\output\res\rpg.py | Set-Content .\output\res\rpg.py
