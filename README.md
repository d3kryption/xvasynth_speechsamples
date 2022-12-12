# xVaSynth Speech Sample Generator

This is a quick Python app I wrote to bulk export samples from the models installed in your xVaSynth. I am not a Python programmer but happy to hear feedback :D

## Why?

I have a lot of voice models I use for mocking games and demos. Sometimes its hard to find a voice that matches a line you want. Using this app, you can quickly create entire CSV's of all models you have with some minor filtering.

## Example
I am working on a game where I need a voice for a bouncer NPC. I don't know which voice to use but I know its male.

I run the code with the filter of gender=male applied. This will return all male voices (and other) that are defined in the config of each voice. 

I can then stick this in the sample csv and run batch mode in xVaSynth.

## 🧐 Features

- Can filter by gender (gender=male/female/other)
- Can pick a random voice
- Can print out to CSV in the terminal
- Can demo to show list all voices and their game

## 🛠️ Installation Steps - development

1) Clone the repo / download the speechsamples.py

```bash
git clone https://github.com/d3kryption/xvasynth_speechsamples
```

2. Move the python file to the models dir:

```bash
mv speechsamples.py ~/steam/steamapps/common/xVASynth/resources/app/models
```

3. Run the app with any command you wish

- Random voice - shows you a random model voice
```python
python speechsamples.py random
```

- Csv return - prints out the name|name_raw||hifi|csv|1
```python
python speechsamples.py csv
```

- filter - pulls in gender so you can filter however you wish name|name_raw|gender|hifi|filter|1
```python
python speechsamples.py filter
```

- demo - prints out some random text of all the voices Hello, my name is {name['name']}, I am from {name['game']} and I am {name['gender']
```python
python speechsamples.py demo
```

- demomcsv - prints out the above in CSV format ready to import
```python
python speechsamples.py democsv
```

Each command can be appended with an optional gender filter:

```python
gender=male/female/other
```

E.g.

```python
python speechsamples.py democsv gender=male
```
