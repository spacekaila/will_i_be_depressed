# Will I Be Depressed???

I taught myself how to use APIs by writing a program that tells you if the weather is going to make you depressed.

If it's before 12:00pm, it tells you if the weather today is going to make you depressed. If it's after 12:00pm, it tells you if the weather tomorrow is going to make you depressed.

## To Run

```bash
git clone git@github.com:spacekaila/will_i_be_depressed.git
cd will_i_be_depressed
python main.py
```

You can input your ZIP code (US only at the moment, sorry!) or have it detect your location automatically.

Conditions to not be depressed:
- Sunny or clear day
- Chance of rain < 15%
- Temperature >= 60 F
- Wind <= 18 mph