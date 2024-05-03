#!/bin/bash

sed -i 's\input\handleInput\g' ./output/res/rpg.py
sed -i 's\output\handleOutput\g' ./output/res/rpg.py
sed '$r ./src_brower/to_merge.py' ./output/res/rpg.py
