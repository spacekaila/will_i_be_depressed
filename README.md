# Will I Be Depressed???

I taught myself how to use APIs by writing a program that tells you if the weather is going to make you depressed.

## To Run

```bash
git clone git@github.com:spacekaila/will_i_be_depressed.git
```
```bash
cd will_i_be_depressed
python main.py
```

## Details

If it's before 12:00pm, it tells you if the weather today is going to make you depressed. If it's after 12:00pm, it tells you if the weather tomorrow is going to make you depressed.


You can input your ZIP code (US only at the moment, sorry!) or have it detect your location automatically (worldwide).

Conditions to not be depressed:
- Not cloudy
- Chance of rain < 15%
- Temperature >= 60 F (~16 C)
- Wind <= 18 mph (~30 kmh)